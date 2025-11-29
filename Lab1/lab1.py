from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import file_read, file_write, http_request

# Configure the Ollama model
# Other model providers can be configured as well:
# e.g. 
# Amazon Bedrock: https://strandsagents.com/latest/documentation/docs/user-guide/concepts/model-providers/amazon-bedrock/
# OpenAI: https://strandsagents.com/latest/documentation/docs/user-guide/concepts/model-providers/openai/
# Antrhopic: https://strandsagents.com/latest/documentation/docs/user-guide/concepts/model-providers/anthropic/
# LiteLLM: https://strandsagents.com/latest/documentation/docs/user-guide/concepts/model-providers/litellm/

# ollama_model = OllamaModel(
#     model_id="gpt-oss:20b", # Make sure this is the model you downloaded from Ollama
#     host="http://localhost:11434",
#     params={
#         "max_tokens": 2048,  # Adjust based on your model's capabilities
#         "temperature": 0.7,  # Lower for more deterministic responses, higher for more creative
#         "top_p": 0.9,        # Nucleus sampling parameter
#         "stream": True,      # Enable streaming responses
#     },
# )

system_prompt = """
Whether information
 - you can make http requests to the national weather service API.
 - Process and display wether data for locations in India.
 - You can also read and write files to current directory.
 - When retrieving weather information, first get coordinates using https://api.weather.gov/points/{latitude},{longitude},  or
 - https://api.weather.gov/points/{zipcode}, then use the returned forecast URL. You can make additional http requests as well.
"""

# Create the agent with tools
local_agent = Agent(
    system_prompt=system_prompt, # Define a system Prompt
    tools=[file_read, file_write, http_request],  # Add your custom tools here
)

local_agent("what is whether in seattle?")
local_agent("get the temperature for bangalore with other whether related details, add those details in a whether.md file in human readable format in same folder")
