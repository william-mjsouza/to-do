# Deve-se criar este arquivo!
from django.urls import path
from . import views  # importa todas as views da app

# Aqui devem ficar todas as rotas da app
urlpatterns = [
    path('', views.render_template, name='app_page'),  # '' = http://127.0.0.1:8000/nome_app/ e apelidei essa URL de app_page
]
