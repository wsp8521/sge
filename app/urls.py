from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sge.urls')),
    path('api/v1/', include('sge_api.urls')),
]
