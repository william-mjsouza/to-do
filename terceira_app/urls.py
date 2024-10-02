# Deve-se criar este arquivo!
from django.urls import path
from . import views  # importa todas as views da app

# Aqui devem ficar todas as rotas da app
urlpatterns = [
    path('', views.custom_template_based_on_ip, name='meu_ip'),    # meu_ip = http://127.0.0.1:8000/meu-ip/
]
