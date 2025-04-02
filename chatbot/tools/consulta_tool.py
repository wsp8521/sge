from langchain.tools import BaseTool
from sge.models import Outflow
from django.db.models import Q

class ConsultaTool(BaseTool):
    name: str = "Consulta_Estoque"
    description: str = '''
        Realiza a consulta no banco de dados usando o Django ORM e retorna os resultados.
        A consulta é feita com base nas instruções passadas pelo usuário.
    '''

    def __init__(self):
        super().__init__()
      
    def _run(self, query:str): 
             
        try:
            consulta = Outflow.objects.filter(product__title__icontains=query)
            if not consulta.exists():
                return "Nenhuma venda com o critério de pesquisa."
            return consulta
            
        except Exception as e:
            return f"Ocorreu um erro ao realizar a consulta: {str(e)}"
        
        
    # Assinatura obrigatória exigida pela classe BaseTool
    async def _arun(self, query:str) -> str:
        raise NotImplementedError("Execução assíncrona não suportada.")


