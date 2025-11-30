from strands import Agent
from strands.tools.mcp import MCPClient
from mcp import stdio_client, StdioServerParameters
from bedrock_agentcore.runtime import BedrockAgentCoreApp

app = BedrockAgentCoreApp()

import logging

logging.getLogger("strands").setLevel(logging.INFO)

@app.entrypoint
def invoke(payload):

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
                You also provide the references when you giving factual details. 
                """,
            tools = [tools]
        )

        response = local_agent(payload.get("prompt"))

        print(f"Metrics : {response.metrics}") # publish token usage metrics
        print(f"Response : {response}")

        return response.message

if __name__ == "__main__":
    print("The agent is Live...")
    app.run(host="0.0.0.0", port=8080)