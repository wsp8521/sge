from django.views.generic import ListView, CreateView, DetailView

from django.urls import reverse_lazy
from sge.models import Inflow
from sge.forms import InflowForms
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

#READ
class InflowRender(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Inflow
    template_name='inflow/list.html'
    context_object_name='lists'
    ordering = '-created_at'
    paginate_by=10
    permission_required = 'sge.view_inflow'
    
    #sistema de filtragem
    def get_queryset(self):
        get_inflow = super().get_queryset().order_by('product')
        filter = self.request.GET.get('product')
        if filter:
            get_inflow=Inflow.objects.filter(product__title__icontains=filter)
        return get_inflow
   
#DETAIL
class InflowDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model=Inflow
    template_name='inflow/detail.html'
    context_object_name='lists'
    permission_required = 'sge.view_inflow'
     
#CREATE
class InflowCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Inflow
    form_class = InflowForms
    template_name='inflow/form.html'
    success_url = reverse_lazy('list_inflow')
    success_message='Cadastro realizado com sucesso'
    permission_required = 'sge.add_inflow'

