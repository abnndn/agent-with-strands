from strands import Agent

from strands.tools.mcp.mcp_client import MCPClient
from mcp.client.streamable_http import streamablehttp_client

import asyncio

import logging

logging.getLogger("strands").setLevel(logging.INFO)

streamable_http_mcp_client = MCPClient(
    lambda: streamablehttp_client(
        url = "http://localhost:8123/mcp"
    )
)


async def process_streaming_response():
    with streamable_http_mcp_client:
        tools = streamable_http_mcp_client.list_tools_sync()

        agent = Agent(
            system_prompt="You are weather expert, provide weather details by using the available tools",
            tools=tools
        )

        agent_stream = agent.stream_async("What is the weather in New York City?")
        async for event in agent_stream:
            # Track event loop lifecycle
            if event.get("init_event_loop", False):
                print("🔄 Event loop initialized")
            elif event.get("start_event_loop", False):
                print("▶️ Event loop cycle starting")
            elif event.get("start", False):
                print("📝 New cycle started")
            elif "message" in event:
                print(f"📬 New message created: {event['message']['role']}")
            elif event.get("complete", False):
                print("✅ Cycle completed")
            elif event.get("force_stop", False):
                print(
                    f"🛑 Event loop force-stopped: {event.get('force_stop_reason', 'unknown reason')}"
                )

asyncio.run(process_streaming_response())