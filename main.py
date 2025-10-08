from dotenv import load_dotenv
from pydanic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChataPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

class PoemaResponse(BaseModel):
    poema: str
    autor: str
    tema: str
    data_de_criacao: str


# Initialize LLMs - choose one or both - depending on your use case
llm = ChatOpenAI(model = "gpt-4o-mini", temperature=0)
llmTwo = ChatAnthropic(model = "claude-4", temperature=0) 

response =llm.invoke("Escreva um poema de amor para minha namorada.")
print(response)


