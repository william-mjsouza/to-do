# Deve-se criar este arquivo!
from django.urls import path
from . import views  # importa todas as views da app

# Aqui devem ficar todas as rotas da app
urlpatterns = [
    path('', views.get_users, name='api_rest'),    # api_rest = http://127.0.0.1:8000/api/
    path('user/<str:nick>', views.get_by_nick,),   # URL dinâmica! http://127.0.0.1:8000/api/user/will_nick, http://127.0.0.1:8000/api/user/leal_nick, ...
]
