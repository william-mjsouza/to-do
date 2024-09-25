# Deve-se criar este arquivo!
from django.urls import path
from . import views  # importa todas as views da app

# Aqui devem ficar todas as rotas da app
urlpatterns = [
    path('', views.render_index_template, name='primeira_app'), # Apelidei essa URL de primeira_app (primeira_app = http://127.0.0.1:8000/primeira_app/)
    path('pagina_estatica', views.render_static_template, name='pagina_estatica'), # pagina_estatica = http://127.0.0.1:8000/primeira_app/pagina_estatica
    path('pagina_dinamica', views.render_dinamic_template, name='pagina_dinamica') # pagina_dinamica = http://127.0.0.1:8000/primeira_app/pagina_dinamica
]
