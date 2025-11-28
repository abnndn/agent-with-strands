# agent-with-strands

#### Strands Documentation - https://strandsagents.com/latest/documentation/docs/

----------------------------------

##### Follows 
- https://www.youtube.com/watch?v=NomS2iLTQ64
- https://github.com/abnndn/strands-agents-copy
- https://github.com/syedair/strands-agents-labs

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
Uses model running locally, through ollama
Uses uv for dependency management.
Basic whether agent.
```
brew services start ollama
curl http://localhost:11434/api/version # confirm if Ollama running, Ollama always runs on this port.
uv run Lab1/lab1.py
```

The local running ollama model was not very helpful.
When tried running on chatgpt20GB model, laptop just hanged.
Finally ended up running it on aws account itself.

---------------------------------------