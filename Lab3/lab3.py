from strands import Agent
from strands_tools import http_request
import logging

logging.getLogger("strands").setLevel(logging.DEBUG)

# Add a handler to see the logs
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s", 
    handlers=[logging.StreamHandler()]
)

system_prompt = """
Whether information
 - you can make http requests to the national weather service API.
 - Process and display wether data for locations in India.
 - You can also read and write files to current directory.
"""

local_agent = Agent(
    system_prompt=system_prompt,
    tools=[http_request]
)

local_agent("what is whether in seattle?")