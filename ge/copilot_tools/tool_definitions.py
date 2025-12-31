
tools = [
    {
        "type": "function",
        "function": {
            "name": "CLICK",
            "description": "Click on a specific point on the screen.",
            "parameters": {
                "type": "object",
                "properties": {
                    "point": {
                        "type": "array",
                        "items": {
                            "type": "integer",
                            "minimum": 0,
                            "maximum": 1000
                        },
                        "minItems": 2,
                        "maxItems": 2,
                        "description": "The [x, y] coordinates of the click point. Values are 0-1000."
                    },
                    "explain": {
                        "type": "string",
                        "description": "A brief explanation of why this action is being taken."
                    }
                },
                "required": ["point", "explain"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "TYPE",
            "description": "Type text into an input field.",
            "parameters": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "string",
                        "description": "The text to type."
                    },
                    "point": {
                        "type": "array",
                        "items": {
                            "type": "integer",
                            "minimum": 0,
                            "maximum": 1000
                        },
                        "minItems": 2,
                        "maxItems": 2,
                        "description": "The [x, y] coordinates of the input field. Values are 0-1000."
                    },
                    "explain": {
                        "type": "string",
                        "description": "A brief explanation of why this action is being taken."
                    }
                },
                "required": ["value", "point", "explain"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "COMPLETE",
            "description": "Report that the task is complete.",
            "parameters": {
                "type": "object",
                "properties": {
                    "return": {
                        "type": "string",
                        "description": "The result or report to the user."
                    },
                    "explain": {
                        "type": "string",
                        "description": "A brief explanation of why this action is being taken."
                    }
                },
                "required": ["return", "explain"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "WAIT",
            "description": "Wait for a specified duration.",
            "parameters": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "integer",
                        "description": "The duration to wait in seconds."
                    },
                    "explain": {
                        "type": "string",
                        "description": "A brief explanation of why this action is being taken."
                    }
                },
                "required": ["value", "explain"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "AWAKE",
            "description": "Awake or launch a specific application.",
            "parameters": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "string",
                        "description": "The name of the application to awake."
                    },
                    "explain": {
                        "type": "string",
                        "description": "A brief explanation of why this action is being taken."
                    }
                },
                "required": ["value", "explain"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "INFO",
            "description": "Ask the user for more information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "string",
                        "description": "The question to ask the user."
                    },
                    "explain": {
                        "type": "string",
                        "description": "A brief explanation of why this action is being taken."
                    }
                },
                "required": ["value", "explain"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "ABORT",
            "description": "Abort the current task.",
            "parameters": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "string",
                        "description": "The reason for aborting."
                    },
                    "explain": {
                        "type": "string",
                        "description": "A brief explanation of why this action is being taken."
                    }
                },
                "required": ["value", "explain"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "SLIDE",
            "description": "Slide on the screen from one point to another.",
            "parameters": {
                "type": "object",
                "properties": {
                    "point1": {
                        "type": "array",
                        "items": {
                            "type": "integer",
                            "minimum": 0,
                            "maximum": 1000
                        },
                        "minItems": 2,
                        "maxItems": 2,
                        "description": "The [x, y] coordinates of the start point. Values are 0-1000."
                    },
                    "point2": {
                        "type": "array",
                        "items": {
                            "type": "integer",
                            "minimum": 0,
                            "maximum": 1000
                        },
                        "minItems": 2,
                        "maxItems": 2,
                        "description": "The [x, y] coordinates of the end point. Values are 0-1000."
                    },
                    "explain": {
                        "type": "string",
                        "description": "A brief explanation of why this action is being taken."
                    }
                },
                "required": ["point1", "point2", "explain"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "LONGPRESS",
            "description": "Long press on a specific point on the screen.",
            "parameters": {
                "type": "object",
                "properties": {
                    "point": {
                        "type": "array",
                        "items": {
                            "type": "integer",
                            "minimum": 0,
                            "maximum": 1000
                        },
                        "minItems": 2,
                        "maxItems": 2,
                        "description": "The [x, y] coordinates of the press point. Values are 0-1000."
                    },
                    "explain": {
                        "type": "string",
                        "description": "A brief explanation of why this action is being taken."
                    }
                },
                "required": ["point", "explain"]
            }
        }
    }
]
