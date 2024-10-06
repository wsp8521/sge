from rest_framework import serializers
from sge import models

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Brand
        fields='__all__'
        
class CagegorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Category
        fields='__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Supplier
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Product
        fields='__all__'


class InflowSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Inflow
        fields='__all__'

class OutflowSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Outflow
        fields='__all__'