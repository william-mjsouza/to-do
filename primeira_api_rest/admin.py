from django.contrib import admin
from .models import User

# Registre aqui os modelos desta app para poder editar as instâncias dele no painel de administração do Django (loacalhost/admin).
admin.site.register(User)
