from django.contrib import admin
from django.urls import include, path   # Deve-se usar o iclude para incluir o urls.py das apps

# Aqui ficam todas as rotas do projeto
urlpatterns = [
    path('admin/', admin.site.urls),                        # 'admin/' = http://127.0.0.1:8000/admin/
    path('', include('core.urls')),                         # Inclui as URLs da app 'core' para a home page ('' = http://127.0.0.1:8000/)
    path('primeira_app/', include('primeira_app.urls')),    # Inclui as URLs da app ('primeira_app/' = http://127.0.0.1:8000/primeira_app/)
]
