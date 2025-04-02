import os
from dotenv import load_dotenv
from django.shortcuts import render
from django.http import StreamingHttpResponse
from langchain_openai import ChatOpenAI
from django.views.decorators.csrf import csrf_exempt
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain import hub
from chatbot.tools.metrica_vendas import MetricasVendas
from chatbot.tools.consulta_produto_tool import ConsultaProduto

#Classe de manipulação de base de dados
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities.sql_database import SQLDatabase
from sqlalchemy import create_engine

load_dotenv()

# Configurando a chave da API do OpenAI
os.environ['OPENAI_API_KEY'] = os.getenv('TOKEN_OPENAI')

PROMPT = '''
Você é um assistente pessoal de um logista. Quando alguem disser "Olá", responda com "Olá, como posso ajudar?".
Analise o banco de dados de acordo com as perguntas do usuário. Retorne as respostas
no formtoa Markdwon
'''


@csrf_exempt
def agent_ia(request):
    
    if  request.method == 'POST':
        question = request.POST.get('message')
        return StreamingHttpResponse(stream_gpt(question), content_type="text/plain") 
    return render(request, 'agent.html')
  


# Função para stream de mensagens do GPT
def stream_gpt(question):
    # Configurando o modelo de linguagem
    model = ChatOpenAI(model='gpt-4o-mini', streaming=True)
    #model = ChatGroq(model='llama-3.3-70b-versatile', api_key=os.getenv('TOKEN_GROQ'), streaming=True)
    memory = ConversationBufferMemory(return_messages=True, memory_key='chat_history')

    # Caminho para o banco de dados SQLite
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    db_path = f"sqlite:///{os.path.join(project_root, 'db.sqlite3')}"
    
    # Configurando a conexão com o banco de dados
    engine = create_engine(db_path)
    db = SQLDatabase(engine)

    # Configurando o Toolkit
    toolkit = SQLDatabaseToolkit(db=db, llm=model)

    # Obtendo ferramentas do Toolkit
    tools = [
    MetricasVendas(),
    ConsultaProduto(),
        ] #+ toolkit.get_tools()


    # Inicializando o agente
    agent = initialize_agent(
        llm=model,
        tools=tools,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        memory=memory
    )

    # Mensagens para o modelo
    system_message = "Você é um assistente de banco de dados inteligente. Responda as consultas SQL de forma eficiente."
    messages = [
        {"role": "system", "content": system_message + PROMPT},
        {"role": "user", "content": question}
    ]

    # Streaming da resposta do GPT
    try:
        response = agent.stream(messages)
        for chunk in response:
            if 'output' in chunk:  # Verifica se 'output' está presente
                yield chunk['output']
    except Exception as e:
        yield f"Erro durante a execução: {e}"


# Caminho absoluto para a pasta raiz do projeto



        
# def stream_gpt_2(question):
#     # Inicializando o cliente ChatOpenAI
#     chat = ChatGroq(model='llama-3.3-70b-versatile', api_key=os.getenv('TOKEN_GROQ'), streaming=True)
#      # Enviando mensagens para o modelo
#     messages = [
#                 {"role": "system", "content": "Você é um assistente pessoal que responde as perguntas do usuáiro"},
#                 {"role": "user", "content": question}
#             ] 
#     # Criando o stream
#     response = chat.stream(messages)
    
#     # Streaming das respostas do GPT
#     for chunk in response:
#         if chunk.content:  # Apenas processa o conteúdo válido
#             yield chunk.content  # Retorna o conteúdo em tempo real
       