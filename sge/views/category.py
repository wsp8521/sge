from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView
from django.urls import reverse_lazy
from sge.models import Category
from sge.forms import CategoryForms
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

#READ
class CategoryRender(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Category
    template_name='category/list.html'
    context_object_name='lists'
    ordering = '-name'
    paginate_by = 10
    permission_required = 'sge.view_category'
    
    #sistema de filtragem
    def get_queryset(self):
        get_Category = super().get_queryset().order_by('name')
        filter = self.request.GET.get('name')
        if filter:
            get_Category=Category.objects.filter(name__icontains=filter)
        return get_Category
   
#DETAIL
class CategoryDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model=Category
    template_name='category/detail.html'
    context_object_name='lists'
    permission_required = 'sge.view_category'
     
#CREATE
class CategoryCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    form_class = CategoryForms
    template_name='category/form.html'
    success_url = reverse_lazy('list_category')
    success_message='Cadastro realizado com sucesso'
    permission_required = 'sge.add_category'

#UPDATE
class CategoryUpdate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    template_name ='category/form.html'
    form_class = CategoryForms
    success_url = reverse_lazy('update_Category')
    success_message ='Atualizada realizado com sucesso'
    permission_required = 'sge.change_category'
    
    #reescrevendo propriedade sucess_url
    def get_success_url(self):
        return reverse_lazy('update_category',kwargs={'pk':self.object.pk})
    
#DELETE
class CategoryDelete(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model=Category
    success_url = reverse_lazy('list_category')
    success_message='Cadastro excluído com sucesso.'
    permission_required = 'sge.delete_category'
        
    
