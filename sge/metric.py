import locale
from sge.models import Product, Outflow, Category, Brand
from django.db.models import Sum, F
from django.utils import timezone, dateformat


def metric_product():
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  # Define o locale para pt_BR
    products= Product.objects.all()
    qtd_product = sum(produc.quantily for produc in products)
    inventory_cost = sum(produc.quantily * produc.cost_price for produc in products)
    stock_value = sum(produc.selling_price * produc.quantily for produc in products)
    stock_profit = stock_value - inventory_cost

    return dict(
        qtd_product = qtd_product,
        inventory_cost = locale.currency(inventory_cost, grouping=True),
        stock_value = locale.currency(stock_value, grouping=True),
        stock_profit = locale.currency(stock_profit, grouping=True), 
    )
    
    
def metric_sales():
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
    

def chart_value_sales():
    today = timezone.now().date() #pegando a data atual
    dates=[str( today - timezone.timedelta(days=i)) for i in range(6, -1, -1)] #percorrendo os últimos 7 fias
    value = list()
    
    #soamando as vendas dos últimos 7 dias
    for date in dates:
        sales_total =  Outflow.objects.filter(created_at__date=date).aggregate(
            total_sales=Sum(F('product__selling_price')*F('quantily')))['total_sales'] or 0
        value.append(float(sales_total))
        
    return dict(
        date = dates,
        value = value
        )
    
def chart_daily_sales():
    today= today = timezone.now().date() #pegando a data atual
    dates=[str( today - timezone.timedelta(days=i)) for i in range(6, -1, -1)] #percorrendo os últimos 7 fias
    quantities = list()
    
    for date in dates:
        quantities_sales =  Outflow.objects.filter(created_at__date=date).count()
        quantities.append(quantities_sales)
        
    return dict(
        date = dates,
        value = quantities
        )
    
def chart_produc_category():
    categories = Category.objects.all()
    return {category.name:Product.objects.filter(Category=category).count()for category in categories}

def chart_produc_brand():
    brands = Brand.objects.all()
    return {brand.name:Product.objects.filter(brand=brand).count()for brand in brands}