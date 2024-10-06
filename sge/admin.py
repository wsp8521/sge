from django.contrib import admin
from sge.models import Brand, Product, Category, Supplier, Outflow, Inflow


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display=("id","name","created_at","update_at")
    list_display_links=("name",)
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=("id","title","Category","cost_price","selling_price","quantily","created_at","update_at")
    list_display_links=("title",)
    
@admin.register(Category)
class CategorydAdmin(admin.ModelAdmin):
    list_display=("id","name","created_at","update_at")
    list_display_links=("name",)
    
@admin.register(Supplier)
class SupplierdAdmin(admin.ModelAdmin):
    list_display=("id","name","created_at","update_at")
    list_display_links=("name",)
    
@admin.register(Inflow)
class InflowdAdmin(admin.ModelAdmin):
    list_display=("id","product","supplier","quantily","created_at","update_at")
    list_display_links=("product",)
    
@admin.register(Outflow)
class OutflowdAdmin(admin.ModelAdmin):
    list_display=("id","product","quantily","created_at","update_at")
    list_display_links=("product",)




