from django.db.models.signals import post_save
from django.dispatch import receiver
from sge.models import Inflow, Outflow


@receiver(post_save, sender=Inflow)#verifica se foi salvo algum registro na tabela inflow
def update_Inflow(sender, instance, created, **kwargs):
    
    if created:#verifica se está sendo criado um novo registro
        if instance.quantily>0: #verifica se foi informado uma quantidade
            product = instance.product
            product.quantily +=instance.quantily #atualizando quantiade na tabela produtos
            product.save() #salvando dados na tabela produtos

  
@receiver(post_save, sender=Outflow)#verifica se foi salvo algum registro na tabela inflow
def update_outflow(sender, instance, created, **kwargs):
    
    if created:#verifica se está sendo criado um novo registro
        if instance.quantily>0: #verifica se foi informado uma quantidade
            product = instance.product
            product.quantily -=instance.quantily #atualizando quantiade na tabela produtos
            product.save() #salvando dados na tabela produtos  