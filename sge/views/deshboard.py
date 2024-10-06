import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from sge import metric


@login_required(login_url='login') #bloqueando acesso
def desh(request):

    context = {
        'product_metrics':metric.metric_product(),
        'sales_metrics':metric.metric_sales(),
        'chart_metrics_sales':json.dumps(metric.chart_value_sales()),
        'chart_metric_daily_sales':json.dumps(metric.chart_daily_sales()),
        'chart_metric_product_category':json.dumps(metric.chart_produc_category()),
        'chart_metric_product_brand':json.dumps(metric.chart_produc_brand())
        
        }
    return render(request,'deshboard/desh.html', context)

