from django.contrib import admin
from django.urls import path, include  # 👈 importante: incluir include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # 👈 esta línea conecta tu app core
]