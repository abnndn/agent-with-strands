# agent-with-strands

#### Strands Documentation - https://strandsagents.com/latest/documentation/docs/

- Strands tools - https://github.com/strands-agents/tools
----------------------------------

Assume IAM Role:
```
ada credentials update --account=803817916307 --provider=conduit --role=support-agent-poc --once
```

Install UV [For ZSH shell]
```
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.zshrc 
uv --version
uv venv [for virtual environment]
uv init [creates pyproject.toml file]
uv self update
```

Install Ollama
```
brew install ollama
ollama pull llama3.2:latest # Can be found in ~/.ollama/models/
ollama pull gpt-oss:20b
ollama --version
ollama list
ollama run llama3.2:latest # run Ollama locally
brew services start ollama   # runs Ollama in background
```

Install Dependencies
```
uv sync
```

----------

Documentation
```
##### Follows 
- https://www.youtube.com/watch?v=NomS2iLTQ64
- https://github.com/abnndn/strands-agents-copy
- https://github.com/syedair/strands-agents-labs
- https://phonetool.amazon.com/users/syedair
- https://github.com/syedair
```

---------------------------------------

### Lab 0
Uses model running in aws.
Uses pip for dependency management. 
Basic agent.
```
python3 Lab0/basic-use.py
```

---------------------------------------

### Lab 1
(Contains details for Lab 2 as well)
Uses model running locally, through ollama
Uses uv for dependency management.
Basic whether agent.
```
[Not needed when running llm model on bedrock agent] brew services start ollama
curl http://localhost:11434/api/version # confirm if Ollama running, Ollama always runs on this port.
uv run Lab1/lab1.py
```

The local running ollama model was not very helpful.
When tried running on chatgpt20GB model, laptop just hanged.
Finally ended up running it on aws account itself.

---------------------------------------

### Lab 3

```
uv run Lab3/lab3.py
```
Helps log the execution.

----------------------------------------

### Lab 4
```
uv run Lab4/lab4.py
```
Creates a custom tool, which can query duckduckGo search APIs. 
Also publishes metrics around token usage.

----------------------------------------

### Lab 5
```
uv run Lab5/lab5.py
```
Integrates with a MCP server. aws documentation mcp server in this case, using stdio.

------------------------------------------

###Lab 6
```
uv run mcp-streamable-http/server/weather.py <Started MCP server>
uv run Lab6/lab6.py
```

Created a local MCP server connecting to US's national weather service.
Call the MCP server though agent.

------------------------------------------

###Lab 6
```
uv run mcp-streamable-http/server/weather.py <Started MCP server>
uv run Lab6/lab6.py
```

Created a local MCP server connecting to US's national weather service.
Call the MCP server though agent. Async streamable response from MCP.

------------------------------------------