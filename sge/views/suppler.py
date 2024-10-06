from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView
from django.urls import reverse_lazy
from sge.models import Supplier
from sge.forms import SupplierForms
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

#READ
class SupplierRender(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Supplier
    template_name='supplier/list.html'
    context_object_name='lists'
    ordering = '-name'
    paginate_by=10
    permission_required = 'sge.view_supplier'
    
    #sistema de filtragem
    def get_queryset(self):
        get_supplier = super().get_queryset().order_by('name')
        filter = self.request.GET.get('name')
        if filter:
            get_supplier=Supplier.objects.filter(name__icontains=filter)
        return get_supplier
   
#DETAIL
class SupplierDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model=Supplier
    template_name='supplier/detail.html'
    context_object_name='lists'
    permission_required = 'sge.view_supplier'
     
#CREATE
class SupplierCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Supplier
    form_class = SupplierForms
    template_name='supplier/form.html'
    success_url = reverse_lazy('list_supplier')
    success_message='Cadastro realizado com sucesso'
    permission_required = 'sge.add_supplier'

#UPDATE
class SupplierUpdate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Supplier
    template_name ='supplier/form.html'
    form_class = SupplierForms
    success_url = reverse_lazy('update_Supplier')
    success_message ='Atualizada realizado com sucesso'
    permission_required = 'sge.change_supplier'
    
    #reescrevendo propriedade sucess_url
    def get_success_url(self):
        return reverse_lazy('update_supplier',kwargs={'pk':self.object.pk})
    
#DELETE
class SupplierDelete(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model=Supplier
    success_url = reverse_lazy('list_supplier')
    success_message='Cadastro excluído com sucesso.'
    permission_required = 'sge.delete_supplier'
        
    
