from strands import Agent, tool

from strands.tools.mcp.mcp_client import MCPClient
from mcp.client.streamable_http import streamablehttp_client

import logging

logging.getLogger("strands").setLevel(logging.INFO)

streamable_http_mcp_client = MCPClient(
    # Local MCP server, can be replaced with the remove mcp server.
    lambda: streamablehttp_client(
        url = "http://localhost:8123/mcp"
    )
)

with streamable_http_mcp_client:
    tools = streamable_http_mcp_client.list_tools_sync()

    agent = Agent(
        system_prompt="""
            You are a weather expert, provide weather information using the available tools to you.
        """,
        tools = tools
    )

    response = agent("What is the weather in New york city?")
