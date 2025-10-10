# AI Assistant Project - Copilot Instructions

## Project Overview
This is a Portuguese-language AI assistant built with LangChain, supporting both OpenAI (GPT-4o-mini) and Anthropic (Claude-4) models. The current implementation focuses on poem generation with structured output using Pydantic models.

## Architecture
- **main.py**: Primary application entry point with LLM initialization and prompt templates
- **tools.py**: Empty placeholder for LangChain tools and agent functions
- **requirements.txt**: Core dependencies including langchain, openai, anthropic, and search tools
- **.env**: Environment variables for API keys (create from template below)

## Key Patterns & Conventions

### LLM Configuration
```python
# Dual LLM setup pattern used in main.py
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
llmTwo = ChatAnthropic(model="claude-4", temperature=0)
```

### Structured Output with Pydantic
All LLM responses use Pydantic models for type safety:
```python
class PoemaResponse(BaseModel):
    poema: str
    autor: str
    tema: str
    data_de_criacao: str
```

### Portuguese Prompts
System prompts are written in Portuguese. Follow this pattern:
```python
("system", """Você é um [role]. 
Escreva [task] com base no [input].
Escreva a saida no seguinte formato...""")
```

## Environment Setup
Required `.env` file with API keys:
```
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
```

## Current Issues to Address
1. **Incomplete imports**: `from langchain.agent import` line needs completion
2. **Undefined variables**: `create_tool` and `agente` implementation missing
3. **Empty tools.py**: Needs tool definitions for search capabilities (wikipedia, duckduckgo)

## Development Workflow
1. Use virtual environment: `python -m venv venv && source venv/bin/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Create `.env` file with API keys
4. Test LLM connections before implementing agents

## Dependencies
Core libraries indicate intent for:
- **langchain**: Agent framework and LLM orchestration
- **langchain-openai/anthropic**: Model providers
- **wikipedia/duckduckgo-search**: External knowledge sources
- **pydantic**: Response validation and parsing

## Next Development Steps
Based on incomplete code analysis:
1. Complete agent imports and tool creation
2. Implement search tools in `tools.py`
3. Create agent workflow combining poem generation with research capabilities
4. Add error handling and input validation
