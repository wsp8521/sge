from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as view_login
from sge import views

urlpatterns = [
   
    #AUTENTICAÇÃO
    path('logout/', view_login.LogoutView.as_view() ,name='logout'),
    path('login/', view_login.LoginView.as_view() ,name='login'),
    
    
    #INDEX
    path('', views.desh, name='desh'),#redireciona para raiz do site  
    
    #CRUD BRAND
    path('marcas/', views.BrandRender.as_view(), name='list_brand'),
    path('marcas/cadastrar', views.BrandCreate.as_view(), name='create_brand'),
    path('marcas/detalhes/<int:pk>', views.BrandDetail.as_view(), name='detail_brand'),
    path('marcas/update/<int:pk>', views.BrandUpdate.as_view(), name='update_brand'),
    path('marcas/delete/<int:pk>', views.BrandDelete.as_view(), name='delete_brand'),
        
    #CRUD CATEGORY
    path('categoria/', views.CategoryRender.as_view(), name='list_category'),#redireciona para raiz do site  
    path('categoria/cadastrar', views.CategoryCreate.as_view(), name='create_category'),
    path('categoria/detalhes/<int:pk>', views.CategoryDetail.as_view(), name='detail_category'),
    path('categoria/update/<int:pk>', views.CategoryUpdate.as_view(), name='update_category'),
    path('categoria/delete/<int:pk>', views.CategoryDelete.as_view(), name='delete_category'),
   
    #CRUD SUPPLIER
    path('fornecedor/', views.SupplierRender.as_view(), name='list_supplier'),#redireciona para raiz do site  
    path('fornecedor/cadastrar', views.SupplierCreate.as_view(), name='create_supplier'),
    path('fornecedor/detalhes/<int:pk>', views.SupplierDetail.as_view(), name='detail_supplier'),
    path('fornecedor/update/<int:pk>', views.SupplierUpdate.as_view(), name='update_supplier'),
    path('fornecedor/delete/<int:pk>', views.SupplierDelete.as_view(), name='delete_supplier'),
   
    #CRUD PRODUCT   
    path('produto/', views.ProductRender.as_view(), name='list_product'),#redireciona para raiz do site  
    
    #CRUD INFLOW
    path('entrada/', views.InflowRender.as_view(), name='list_inflow'),#redireciona para raiz do site  
    path('entrada/cadastrar', views.InflowCreate.as_view(), name='create_inflow'),
    path('entrada/detalhes/<int:pk>', views.InflowDetail.as_view(), name='detail_inflow'),
  
    #CRUD OUTFLOW
    path('saida/', views.OutflowRender.as_view(), name='list_outflow'),#redireciona para raiz do site 
    path('saida/cadastrar', views.OutflowCreate.as_view(), name='create_outflow'),
    path('saida/detalhes/<int:pk>', views.OutflowDetail.as_view(), name='detail_outflow'), 
    
    #CRUD PRODUCT
    path('produto/', views.ProductRender.as_view(), name='list_product'),#redireciona para raiz do site  
    path('produto/cadastrar', views.ProductCreate.as_view(), name='create_product'),
    path('produto/detalhes/<int:pk>', views.ProductDetail.as_view(), name='detail_product'),
    path('produto/update/<int:pk>', views.ProductUpdate.as_view(), name='update_product'),
    path('produto/delete/<int:pk>', views.ProductDelete.as_view(), name='delete_product'),
    
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)