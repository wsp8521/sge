from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView
from django.urls import reverse_lazy
from sge.models import Product, Category, Brand
from sge.forms import ProductForms
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from sge.metric import metric_product

#READ
class ProductRender(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    template_name='products/list.html'
    context_object_name='lists'
    ordering = '-title'
    paginate_by=10
    permission_required = 'sge.view_product'
    
    #sistema de filtragem
    def get_queryset(self):
        get_product = super().get_queryset().order_by('title')
        filter = self.request.GET.get('name')
        filterCategory = self.request.GET.get('category')
        filterBrand = self.request.GET.get('brand')
        
        if filter:
            get_product=get_product.filter(title__icontains=filter)
            
        if filterCategory:
            get_product=get_product.filter(Category__id=filterCategory)
            
        if filterBrand:
            get_product=get_product.filter(brand__id=filterBrand)
            
        return get_product
    
    #reescrevenco context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context["brands"] = Brand.objects.all()
        context["product_metrics"] = metric_product()
        return context
    
#DETAIL
class ProductDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model=Product
    template_name='products/detail.html'
    context_object_name='lists'
    permission_required = 'sge.view_product'
     
#CREATE
class ProductCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForms
    template_name='products/form.html'
    success_url = reverse_lazy('list_product')
    success_message='Cadastro realizado com sucesso'
    permission_required = 'sge.add_product'

#UPDATE
class ProductUpdate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Product
    template_name ='products/form.html'
    form_class = ProductForms
    success_url = reverse_lazy('update_product')
    success_message ='Atualizada realizado com sucesso'
    permission_required = 'sge.change_product'
    
    #reescrevendo propriedade sucess_url
    def get_success_url(self):
        return reverse_lazy('update_product',kwargs={'pk':self.object.pk})
    
#DELETE
class ProductDelete(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model=Product
    success_url = reverse_lazy('list_product')
    success_message='Cadastro excluído com sucesso.'
    permission_required = 'sge.delete_product'
        
    
