# Deve-se criar este arquivo!
from django.urls import path
from . import views  # importa todas as views da app

# Aqui devem ficar todas as rotas da app
urlpatterns = [
    path('app_static_page', views.render_static_template, name='app_static_page'),  # Apelidei essa URL de app_static_page
    path('app_dinamic_page', views.render_dinamic_template, name='app_dinamic_page')
]
