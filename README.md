# AI Assistant Project

Este projeto é um assistente de IA em português, construído com LangChain, que utiliza os modelos OpenAI (GPT-4o-mini) e/ou Anthropic (Claude-4) para geração de poemas com saída estruturada via modelos Pydantic.

## Funcionalidades

- Geração de poemas personalizados em português
- Respostas estruturadas e validadas por Pydantic
- Suporte a múltiplos modelos de linguagem (OpenAI e Anthropic)
- Arquitetura pronta para integração de ferramentas de busca (Wikipedia, DuckDuckGo)

## Estrutura do Projeto

- `main.py`: Ponto de entrada da aplicação, inicialização dos LLMs e prompts
- `tools.py`: Definição de ferramentas externas (em desenvolvimento)
- `requirements.txt`: Dependências principais
- `.env`: Variáveis de ambiente para chaves de API

## Como executar

1. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv && source venv/bin/activate
    ```
2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3. Crie o arquivo `.env` com suas chaves de API:
    ```
    OPENAI_API_KEY=your_openai_key_here
    ANTHROPIC_API_KEY=your_anthropic_key_here
    ```
4. Execute o projeto conforme instruções no `main.py`.

## Escalabilidade

Este projeto pode ser facilmente escalado para uma API dinâmica, permitindo integração com frontends web ou mobile. A arquitetura modular facilita a reutilização dos fluxos de geração de conteúdo em diferentes interfaces.

## Documentações de Base Utilizadas

Este projeto foi desenvolvido utilizando as seguintes documentações oficiais como referência:

### LangChain Framework
- **LangChain Documentation**: https://python.langchain.com/docs/
- **LangChain Agents**: https://python.langchain.com/docs/modules/agents/
- **LangChain Prompts**: https://python.langchain.com/docs/modules/model_io/prompts/
- **LangChain Output Parsers**: https://python.langchain.com/docs/modules/model_io/output_parsers/

### Modelos de Linguagem
- **OpenAI API Documentation**: https://platform.openai.com/docs/
- **LangChain OpenAI Integration**: https://python.langchain.com/docs/integrations/llms/openai/
- **Anthropic Claude API**: https://docs.anthropic.com/
- **LangChain Anthropic Integration**: https://python.langchain.com/docs/integrations/llms/anthropic/

### Validação e Estrutura de Dados
- **Pydantic Documentation**: https://docs.pydantic.dev/
- **Pydantic BaseModel**: https://docs.pydantic.dev/latest/concepts/models/
- **LangChain Pydantic Parser**: https://python.langchain.com/docs/modules/model_io/output_parsers/pydantic/

### Ferramentas e Utilitários
- **Python-dotenv**: https://python-dotenv.readthedocs.io/
- **Wikipedia Python Library**: https://wikipedia.readthedocs.io/
- **DuckDuckGo Search**: https://pypi.org/project/duckduckgo-search/

### Recursos Adicionais
- **LangChain Agent Executors**: https://python.langchain.com/docs/modules/agents/agent_executors/
- **LangChain Tools**: https://python.langchain.com/docs/modules/agents/tools/
- **Environment Variables Best Practices**: https://12factor.net/config

## Próximos Passos

- Implementar ferramentas de busca externas
- Criar endpoints de API para consumo dinâmico
- Integrar com aplicações frontend
- Mudar o objetivo da busca para algo mais aplicável a um chatbot com frontend.

---
Desenvolvido para facilitar a criação de assistentes de IA em português, com foco em extensibilidade e integração.

