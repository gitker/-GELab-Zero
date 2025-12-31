import json
import sys
import os
from collections import OrderedDict
from copy import deepcopy

from copilot_tools.base_parser import BaseParser
from copilot_tools.tool_definitions import tools
from copilot_tools.action_tools import action_assertion

class FunctionCallParser(BaseParser):
    def __init__(self, parser_config: dict = None):
        super().__init__(parser_config if parser_config else {})

    def action_assertion(self, action: dict):
        action_assertion(action)

    def action2str(self, action: dict) -> str:
        return json.dumps(action, ensure_ascii=False)

    def get_tools(self):
        return tools

    def str2action(self, response) -> dict:
        # response is now a message object from openai
        if hasattr(response, 'tool_calls') and response.tool_calls:
            tool_call = response.tool_calls[0]
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            
            action = OrderedDict()
            action["action_type"] = function_name
            action.update(arguments)
            
            if "explain" in action:
                action["summary"] = action["explain"]
            
            # Capture content as CoT
            if hasattr(response, 'content') and response.content:
                action["cot"] = response.content
            else:
                action["cot"] = ""
            
            # Handle specific fields mapping if needed
            if function_name == "CLICK":
                if "point" in action:
                    action["point"] = action["point"]
            
            return action
        else:
            # Fallback or error handling if no tool call
            content = response.content if hasattr(response, 'content') else str(response)
            return {"action_type": "ABORT", "value": f"Model did not call a function. Content: {content}", "explain": "Model failure", "summary": "Model failure"}

    def env2messages4ask(self, task, environments, actions, return_sft=False, hints=[]) -> list:
        
        system_prompt = """You are a mobile GUI Agent expert. You need to interact with the mobile phone based on the user's task, screen screenshots, and interaction history to complete the user's task.
Please keep in mind that the mobile screen coordinate system has the top-left corner as the origin, the x-axis to the right, and the y-axis down, with values ranging from 0-1000.

# Action Principles:
1. You need to strictly follow the user's instructions.
2. You must use the provided tools to interact with the device.
3. Before calling a tool, you MUST analyze the current state and plan your action. Output your thought process first, then call the tool.
"""
        
        messages = [
            {"role": "system", "content": system_prompt}
        ]
        
        # Add history
        # environments has one more element than actions (the current environment)
        num_history = len(actions)
        
        for i, (env, action) in enumerate(zip(environments[:-1], actions)):
            # User message with screenshot and comment
            user_content = []
            
            # Add task info to the first message
            if i == 0:
                user_content.append({"type": "text", "text": f"Task: {task}"})

            if env.get("user_comment"):
                user_content.append({"type": "text", "text": env["user_comment"]})
            
            # Only keep the last historical image
            if i == num_history - 1:
                if env.get("image"):
                    user_content.append({"type": "image_url", "image_url": {"url": env["image"]}})
            else:
                # If image is omitted and no other content, add a placeholder
                if not user_content:
                    user_content.append({"type": "text", "text": "(Screenshot omitted)"})
                
            messages.append({"role": "user", "content": user_content})
            
            # Assistant message (previous action)
            tool_call_id = f"call_{i}"
            function_name = action.get("action_type", action.get("action"))
            
            # Filter arguments to match tool definition
            arguments = {}
            for k, v in action.items():
                if k not in ["action_type", "action", "cot", "summary"]:
                    arguments[k] = v
            
            # Ensure explain is present
            if "explain" not in arguments and "summary" in action:
                arguments["explain"] = action["summary"]
            
            content = action.get("cot")

            messages.append({
                "role": "assistant",
                "content": content,
                "tool_calls": [{
                    "id": tool_call_id,
                    "type": "function",
                    "function": {
                        "name": function_name,
                        "arguments": json.dumps(arguments)
                    }
                }]
            })
            
            # Tool output
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call_id,
                "content": "success"
            })

        # Current step
        current_env = environments[-1]
        user_content = []
        
        task_text = ""
        if len(environments) == 1:
             task_text += f"Task: {task}\n"

        if hints:
            task_text += "Hints:\n" + "\n".join([f"- {h}" for h in hints]) + "\n"
            
        if current_env.get("user_comment"):
            task_text += f"\nUser Comment: {current_env['user_comment']}"
            
        if task_text:
            user_content.append({"type": "text", "text": task_text})
        
        if current_env.get("image"):
            user_content.append({"type": "image_url", "image_url": {"url": current_env["image"]}})
            
        messages.append({"role": "user", "content": user_content})
        
        if return_sft:
            # SFT not implemented for this parser yet
            return messages, []
        else:
            return messages
