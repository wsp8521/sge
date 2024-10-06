from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from sge.models import Outflow
from sge.forms import OutflowForms
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from sge.metric import metric_sales

#READ
class OutflowRender(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Outflow
    template_name='outflow/list.html'
    context_object_name='lists'
    ordering = '-created_at'
    paginate_by=10
    permission_required = 'sge.view_outflow'
    
    #sistema de filtragem
    def get_queryset(self):
        get_outflow = super().get_queryset().order_by('product')
        filter = self.request.GET.get('product')
        if filter:
            get_outflow=Outflow.objects.filter(product__title__icontains=filter)
        return get_outflow
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_metrics'] = metric_sales()
        
        return context
        
#DETAIL
class OutflowDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model=Outflow
    template_name='outflow/detail.html'
    context_object_name='lists'
    permission_required = 'sge.view_outflow'
     
#CREATE
class OutflowCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Outflow
    form_class = OutflowForms
    template_name='outflow/form.html'
    success_url = reverse_lazy('list_outflow')
    success_message='Cadastro realizado com sucesso'
    permission_required = 'sge.add_outflow'

