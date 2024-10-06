from django.db import models

class Brand(models.Model):
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering=['name']
        
    name = models.CharField(max_length=500,verbose_name='Marca')
    description = models.TextField(blank=True, null=True,verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
    update_at = models.DateTimeField(auto_now=True, verbose_name='atualizado em')
    
    def __str__(self):
        return self.name
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

class Category(models.Model):
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering=['name']
        
    name = models.CharField(max_length=500,verbose_name='Categoria')
    description = models.TextField(blank=True, null=True,verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
    update_at = models.DateTimeField(auto_now=True, verbose_name='atualizado em')
    
    def __str__(self):
        return self.name
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

class Supplier(models.Model):
    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
        ordering=['name']
        
    name = models.CharField(max_length=500,verbose_name='Fornecedor')
    description = models.TextField(blank=True, null=True,verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
    update_at = models.DateTimeField(auto_now=True, verbose_name='atualizado em')
    
    def __str__(self):
        return self.name
 #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   
 
class Product(models.Model):
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering=['title']
    
    title = models.CharField(max_length=200, verbose_name='Nome do produto')  
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="brand", verbose_name='Marca') 
    Category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="category", verbose_name='Categoria') 
    description = models.TextField(blank=True, null=True,verbose_name='Descrição')
    serial_number=models.CharField(max_length=20, blank=True, null=True, verbose_name='Número de serie')
    cost_price = models.DecimalField(max_digits=20, decimal_places=2,verbose_name='Preço de custo')
    selling_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Prelo de venda')
    quantily = models.IntegerField(verbose_name='Quantidade em estoque', default=0)
    image = models.ImageField(upload_to='product',verbose_name='imagens',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
    update_at = models.DateTimeField(auto_now=True, verbose_name='atualizado em')
    
    def __str__(self):
        return self.title
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  

class Inflow(models.Model):
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering=['-created_at']
        
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="suplier", verbose_name='Fornecedor') 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_inflow", verbose_name='Produto') 
    quantily = models.IntegerField(verbose_name='Quantidade')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
    update_at = models.DateTimeField(auto_now=True, verbose_name='atualizado em')
    
    def __str__(self):
        return str(self.product)
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  

class Outflow(models.Model):
    class Meta:
        verbose_name = "Saída"
        verbose_name_plural = "Saídas"
        ordering=['-created_at']
        
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_outflow", verbose_name='Produto') 
    quantily = models.IntegerField(verbose_name='Quantidade')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
    update_at = models.DateTimeField(auto_now=True, verbose_name='atualizado em')
    
    def __str__(self):
        return str(self.product)
    
        
        