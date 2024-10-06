from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView
from django.urls import reverse_lazy
from sge.models import Brand
from sge.forms import BrandForms
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


#READ
class BrandRender(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Brand
    template_name='brands/list.html'
    context_object_name='lists'
    ordering = '-name'
    paginate_by=10
    permission_required = 'sge.view_brand'
    
    #sistema de filtragem
    def get_queryset(self):
        get_brand = super().get_queryset().order_by('name')
        filter = self.request.GET.get('name')
        if filter:
            get_brand=Brand.objects.filter(name__icontains=filter)
        return get_brand
   
#DETAIL
class BrandDetail(LoginRequiredMixin, PermissionRequiredMixin,  DetailView):
    model=Brand
    template_name='brands/detail.html'
    context_object_name='lists'
    permission_required = 'sge.view_brand'
     
#CREATE
class BrandCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Brand
    form_class = BrandForms
    template_name='brands/form.html'
    success_url = reverse_lazy('list_brand')
    success_message='Cadastro realizado com sucesso'
    permission_required = 'sge.add_brand'

#UPDATE
class BrandUpdate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Brand
    template_name ='brands/form.html'
    form_class = BrandForms
    success_url = reverse_lazy('update_brand')
    success_message ='Atualizada realizado com sucesso'
    permission_required = 'sge.change_brand'
    
    #reescrevendo propriedade sucess_url
    def get_success_url(self):
        return reverse_lazy('update_brand',kwargs={'pk':self.object.pk})
    
#DELETE
class BrandDelete(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model=Brand
    success_url = reverse_lazy('list_brand')
    success_message='Cadastro excluído com sucesso.'
    permission_required = 'sge.delete_brand'
        
    
