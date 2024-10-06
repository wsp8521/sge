from django import forms
from sge import models

#Brand
class BrandForms(forms.ModelForm):
    class Meta:
        model = models.Brand
        fields=['name','description']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}), #alterando atribuutos do campo
            'description':forms.Textarea(attrs={'class':'form-control', 'rows':5})
        }
     
#Category       
class CategoryForms(forms.ModelForm):
     class Meta:
        model = models.Category
        fields=['name','description']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}), #alterando atribuutos do campo
            'description':forms.Textarea(attrs={'class':'form-control', 'rows':5})
            }
#Supplier       
class SupplierForms(forms.ModelForm):
     class Meta:
        model = models.Supplier
        fields=['name','description']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}), #alterando atribuutos do campo
            'description':forms.Textarea(attrs={'class':'form-control', 'rows':5})
            }
      
#Inflow       
class InflowForms(forms.ModelForm):
     class Meta:
        model = models.Inflow
        fields=['supplier','product','quantily','description']
        widgets={
            'supplier':forms.Select(attrs={'class':'form-control'}), #alterando atribuutos do campo
            'product':forms.Select(attrs={'class':'form-control'}),
            'quantily':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'rows':5})
            
            }
        
#Outflow  
class OutflowForms(forms.ModelForm):
     class Meta:
        model = models.Outflow
        fields=['product','quantily','description']
        widgets={
            'product':forms.Select(attrs={'class':'form-control'}),
            'quantily':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'rows':5})
            }
        
#Product
class ProductForms(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'accept':'image/*'}),required=False,label="imagem")
    class Meta:
        model = models.Product
        fields=['title','brand','Category','description','serial_number','cost_price','selling_price','image']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'brand':forms.Select(attrs={'class':'form-control'}),
            'Category':forms.Select(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'rows':3}),
            'serial_number':forms.TextInput(attrs={'class':'form-control'}),
            'cost_price':forms.NumberInput(attrs={'class':'form-control'}),
            'selling_price':forms.NumberInput(attrs={'class':'form-control'}),
            'quantily':forms.NumberInput(attrs={'class':'form-control'}),            
            }