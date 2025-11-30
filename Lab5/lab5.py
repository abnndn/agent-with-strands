from strands import Agent
from strands.tools.mcp import MCPClient
from mcp import stdio_client, StdioServerParameters
from strands_tools import file_read, file_write

import logging

logging.getLogger("strands").setLevel(logging.INFO)

# Initializing MCP server
stdio_mcp_client = MCPClient(lambda: stdio_client(
    StdioServerParameters(
        command="uvx",
        args=["awslabs.aws-documentation-mcp-server@latest"]
    )
))

with stdio_mcp_client:
    tools = stdio_mcp_client.list_tools_sync()

    local_agent = Agent(
        system_prompt= """
            You're an AWS documentation expert. Use the aws documentation tools available to you to provide information and architecture proposals.
            You can also read and write files to current directory.
            """,
        tools = [tools, file_read, file_write]
    )

    response = local_agent("Create an architecture for async events processing using aws services. Append the response in architecture.md file in the local directory.")
    print(f"Metrics : {response.metrics}") # publish token usage metrics
