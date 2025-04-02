from langchain.tools import BaseTool
from sge.models import Product
from django.db.models import Q

from django.conf import settings

class ConsultaProduto(BaseTool):
    name: str = "Consulta_Produto"
    description: str = '''
        Utilize essa ferramenta para realizar a consulta no banco de dados usando o Django ORM e retorna as informações dos produtos.
        A consulta é feita com base nas instruções passadas pelo usuário.
    '''

    def __init__(self):
        super().__init__()

    def _run(self, query: str):
        try:
            consulta = Product.objects.filter(title__icontains=query)
            if not consulta.exists():
                return "Nenhum produto encontrado com o critério de pesquisa."

            # Formatar o retorno com informações detalhadas, incluindo a URL da imagem
            produtos = []
            for produto in consulta:
                produtos.append({
                    "title": produto.title,
                    "description": produto.description,
                    "cost_price": produto.cost_price,
                    "image_url": f"{settings.MEDIA_URL}{produto.image}" if produto.image else None,
                })
            return produtos

        except Exception as e:
            return f"Ocorreu um erro ao realizar a consulta: {str(e)}"

    # Assinatura obrigatória exigida pela classe BaseTool
    async def _arun(self, query: str) -> str:
        raise NotImplementedError("Execução assíncrona não suportada.")