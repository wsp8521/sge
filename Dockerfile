#Definindo sistema de base
FROM python:3.12-slim

#Definindo o diretório de trabalho
WORKDIR /sge 

#impede que o arquivo .pyc seja criado
#O valor 1 desabilita a criação de arquivos .pyc, que são arquivos de bytecode gerados pelo Python para otimizar a execução de scripts.
ENV PYTHONDONTWRITEBYTECODE 1

#Definindo váriavel de ambiente para depuração
#O valor 1 desabilita o buffer de saída do Python, o que significa que a saída do programa será exibida imediatamente, sem esperar por um buffer ser preenchido.
ENV PYTHONUNBUFFERED 1

#Copiando os arquivos para o contêiner
COPY . . 

#Instalando as dependências
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

#definindo a porta onde rodará a aplicaççao
EXPOSE 8000

#comando para executar a aplicação
CMD python manage.py runserver  0.0.0.0:8000