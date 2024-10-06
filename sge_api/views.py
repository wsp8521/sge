from rest_framework import generics
from sge import models
from sge_api import serializer


#BRAND
class BrandCreateRead(generics.ListCreateAPIView): #View and create
    queryset = models.Brand.objects.all()
    serializer_class = serializer.BrandSerializer
    
class BrandUpdateViewDelete(generics.RetrieveUpdateDestroyAPIView): #detail, Update, delete
    queryset = models.Brand.objects.all()
    serializer_class = serializer.BrandSerializer
    
#CATEGORY
class CategoryCreateRead(generics.ListCreateAPIView): #View and create
    queryset = models.Category.objects.all()
    serializer_class = serializer.CagegorySerializer
    
class CategoryUpdateViewDelete(generics.RetrieveUpdateDestroyAPIView): #View and create
    queryset = models.Category.objects.all()
    serializer_class = serializer.CagegorySerializer

#SUPPLIER
class SupplierCreateRead(generics.ListCreateAPIView): #View and create
    queryset = models.Supplier.objects.all()
    serializer_class = serializer.SupplierSerializer

class SupplierUpdateViewDelete(generics.RetrieveUpdateDestroyAPIView): #View and create
    queryset = models.Supplier.objects.all()
    serializer_class = serializer.SupplierSerializer
    
#PRODUCT
class ProductCreateRead(generics.ListCreateAPIView): #View and create
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer  
    
class ProductUpdateViewDelete(generics.RetrieveDestroyAPIView): #View and create
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer  

#INFLOW
class InflowCreateRead(generics.ListCreateAPIView): #View and create
    queryset = models.Inflow.objects.all()
    serializer_class = serializer.InflowSerializer  

class InflowUpdateViewDelete(generics.RetrieveUpdateDestroyAPIView): #View and create
    queryset = models.Inflow.objects.all()
    serializer_class = serializer.InflowSerializer  

#OUTFLOW
class OutflowCreateRead(generics.ListCreateAPIView): #View and create
    queryset = models.Outflow.objects.all()
    serializer_class = serializer.OutflowSerializer  
    
class OutflowUpdateViewDelete(generics.RetrieveUpdateDestroyAPIView): #View and create
    queryset = models.Outflow.objects.all()
    serializer_class = serializer.OutflowSerializer  
    
    
    
    