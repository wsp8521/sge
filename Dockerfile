#Definindo sistema de base
FROM python:3.12-slin 

#Definindo o diretório de trabalho
WORKDIR /sge 

#Copiando os arquivos para o contêiner
COPY . . 

#Instalando as dependências
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

#definindo a porta onde rodará a aplicaççao
EXPOSE 8000

#comando para executar a aplicação
CMD python manage.py runserver  0.0.0.0:8000