import os
from sge.models import Product
from markdown import markdown
from dotenv import load_dotenv
from django.shortcuts import render
from django.http import StreamingHttpResponse
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from django.views.decorators.csrf import csrf_exempt

load_dotenv()

# Configurando a chave da API do OpenAI
os.environ['OPENAI_API_KEY'] = os.getenv('TOKEN_OPENAI')


@csrf_exempt
def chatbot(request):
    if request.method == 'GET':
        return render(request, 'chatbot.html')
    elif request.method == 'POST':
        question = request.POST.get('message')
        
        # Retorna a resposta como StreamingHttpResponse
        return StreamingHttpResponse(stream_gpt(question), content_type="text/plain")




def stream_gpt(question):
    # Inicializando o cliente ChatOpenAI
    chat = ChatOpenAI(
        model="gpt-4o-mini",  # Ajuste para o modelo desejado
        temperature=0.7,
        streaming=True  # Ativando o streaming
    )
    
    # Enviando mensagens para o modelo
    messages = [
        SystemMessage(content="Você é um assistente pessoal. Responda as perguntas no formato markdown."),
        HumanMessage(content=question)
    ]
    
    # Criando o stream
    response = chat.stream(messages)
    
    # Streaming das respostas do GPT
    for chunk in response:
        if chunk.content:  # Apenas processa o conteúdo válido
            yield chunk.content  # Retorna o conteúdo em tempo real
