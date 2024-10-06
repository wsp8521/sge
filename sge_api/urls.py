from django.urls import path
from sge_api import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [
       #AUTHENTICATION TOKEN
    path('authentication/token', TokenObtainPairView.as_view(), name='token_obtain_pair' ), 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    #ENDPOINT MARCA
    path('marca/', views.BrandCreateRead.as_view(), name='brand_create_read' ),    #Read and crete
    path('marca/<int:pk>', views.BrandUpdateViewDelete.as_view(), name='brand_update_delte_view' ), 
    
   #ENDPOINT CATEGORIA
    path('categoria/', views.CategoryCreateRead.as_view(), name='category_create_read' ),    #Read and crete
    path('categoria/<int:pk>', views.CategoryUpdateViewDelete.as_view(), name='category_update_delte_view' ), 
    
   #ENDPOINT FORNECEDOR
    path('fornecedor/', views.SupplierCreateRead.as_view(), name='supplier_create_read' ),    #Read and crete
    path('fornecedor/<int:pk>', views.SupplierUpdateViewDelete.as_view(), name='supplier_update_delte_view' ), 
    
   #ENDPOINT PRODUTOS
    path('produto/', views.ProductCreateRead.as_view(), name='product_create_read' ),    #Read and crete
    path('produto/<int:pk>', views.ProductUpdateViewDelete.as_view(), name='product_update_delte_view' ), 
    
    #ENDPOINT ENTRADA
    path('entrada/', views.InflowCreateRead.as_view(), name='inflow_create_read' ),    #Read and crete
    path('entrada/<int:pk>', views.InflowUpdateViewDelete.as_view(), name='inflow_update_delte_view' ), 
    
   #ENDPOINT SAIDA
    path('saida/', views.OutflowCreateRead.as_view(), name='outflow_create_read' ),    #Read and crete
    path('saida/<int:pk>', views.OutflowUpdateViewDelete.as_view(), name='outflow_update_delte_view' ), 
    

    
    
    

]