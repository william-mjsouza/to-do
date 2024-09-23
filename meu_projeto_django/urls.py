from django.contrib import admin
from django.urls import include, path

# Aqui ficam todas as rotas do projeto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Inclui as URLs da app 'core' para a home page
    path('nome_app/', include('nome_app.urls')),  # Inclui as URLs da app
]
