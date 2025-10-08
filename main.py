from dotenv import load_dotenv
from pydanic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChataPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agent import create_openai_tools_agent, AgentExecutor
load_dotenv()

class PoemaResponse(BaseModel):
    poema: str
    autor: str
    tema: str
    data_de_criacao: str


# Initialize LLMs - choose one or both - depending on your use case
llm = ChatOpenAI(model = "gpt-4o-mini", temperature=0)
llmTwo = ChatAnthropic(model = "claude-4", temperature=0) 

parse = PydanticOutputParser(pydantic_object=PoemaResponse)

prompt = ChataPromptTemplate.from_messages(
    [
        ("system", """Você é um poeta renomado.
         Escreva um poema com base no tema fornecido.
         Escreva a saida no seguinte formato e não forneça mais nada além disso\n{format_instructions}         
         """,)

    ]).partial(format_instructions=parse.get_format_instructions())

agent = create_too_calling_agent(
    llm=llm,
    tools=[],
    prompt=prompt,
    output_parser=parse,
   
)
agente_executor = AgentExecutor(agent=agent, tools=[], verbose=True)
response = agente_executor.invoke({})
print(response)