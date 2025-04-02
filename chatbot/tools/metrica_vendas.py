from langchain.tools import BaseTool
from sge.models import Outflow
from django.db.models import Q
from sge.models import Product, Outflow, Category, Brand
from django.db.models import Sum, F
import locale


class MetricasVendas(BaseTool):
    name: str = "Metrica_de_Vendas"
    description: str = '''
        Use essa ferramenta para calcular as metricas das vendas
    '''

    def __init__(self):
        super().__init__()
      
    def _run(self, query:str): 
             
        try:
            locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  # Define o locale para pt_BR
            sales= Outflow.objects.all()
            qtd_sales = sales.count()
            product_sales = sales.aggregate(product_sales=Sum('quantily'))['product_sales'] or 0
            sales_value = sum(sale.quantily * sale.product.selling_price for sale in sales)
            sales_cost = sum(sale.quantily * sale.product.cost_price for sale in sales)
            sales_profit = sales_value-sales_cost
            
            return dict(
                qtd_sales = qtd_sales,
                product_sales = product_sales,
                sales_value = locale.currency(sales_value, grouping=True),
                sales_profit = locale.currency(sales_profit, grouping=True),
    )
            
        except Exception as e:
            return f"Ocorreu um erro ao realizar a consulta: {str(e)}"
        
        
    # Assinatura obrigatória exigida pela classe BaseTool
    async def _arun(self, query:str) -> str:
        raise NotImplementedError("Execução assíncrona não suportada.")


