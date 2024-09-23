from django.apps import AppConfig

# Classe de configuração da app que deve ser colocada na lista de apps instaladas em settings.py do meu_projeto_django
class PrimeiraAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'primeira_app'