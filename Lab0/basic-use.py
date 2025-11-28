###########################################################################
# Commands to run before running this agent.
#
# [Create python virtual environment]
# python3 -m venv venv 
# source venv/bin/activate
#
# [Install strands SDK for agent implmentation]
# pip install strands-agents 
# pip install strands-agents-tools
#
# [Assume IAM role with access to Bedrock models for local testing - assumes for 1 hour]
# ada credentials update --account=803817916307 --provider=conduit --role=support-agent-poc --once
#
# Strands Documentation - https://strandsagents.com/latest/documentation/docs/
#
###########################################################################
from strands import Agent

agent = Agent()

response = agent("What is agentic AI?")