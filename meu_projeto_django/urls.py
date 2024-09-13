from django.contrib import admin
from django.urls import path
# Importar a view da app que foi criada
from nome_app.views import home


# Aqui ficam todas as rotas de todas as apps
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home), # Quando tiver só o / na URL do site, é chamada a função home
]
