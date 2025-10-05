from dotenv import load_dotenv
from pydanic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

# Initialize LLMs - choose one or both - depending on your use case
llm = ChatOpenAI(model = "gpt-4o-mini", temperature=0)
llmTwo = ChatAnthropic(model = "claude-4", temperature=0) 