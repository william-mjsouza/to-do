from pathlib import Path
import os   # Biblioteca para usar o método path.join

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v8h9+6d@n-15gaow*3zw=pe4*7#!1kypjv7xb89$$0m7=b*89_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True    # Trocar pra False quando for fazer o deploy!

ALLOWED_HOSTS = []


# Application definition
# Toda vez que uma app for criada, ela deve ser adicionada a essa lista (nome_da_app.apps.nome_da_classe_de_confguraçao)
INSTALLED_APPS = [
    'django.contrib.admin',                 # Admin do Django
    'django.contrib.auth',                  # Autenticação e controle de usuários
    'django.contrib.contenttypes',          # Content types para compatibilidade de models
    'django.contrib.sessions',              # Gerenciamento de sessões
    'django.contrib.messages',              # Sistema de mensagens
    'django.contrib.staticfiles',           # Gerenciamento de arquivos estáticos

    # Aplicações customizadas do projeto
    'core.apps.CoreConfig',                 # Adiciona a app core
    'primeira_app.apps.PrimeiraAppConfig',  # Adiciona a primeira app
    'segunda_app.apps.SegundaAppConfig',    # Adiciona a segunda app
    'terceira_app.apps.TerceiraAppConfig',  # Adiciona a terceira app

    # Adiciona a API RESTful
    'rest_framework',                       # Django REST framework para criação de APIs
    'corsheaders',                          # Adiciona o suporte a CORS
    'primeira_api_rest',                    # Sua app de API
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',                        # Adiciona a middleware do corsheaders para CORS
]

ROOT_URLCONF = 'meu_projeto_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Agora comaça a olhar a pasta templates que está global no projeto
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'meu_projeto_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'             # Idioma português do Brasil

TIME_ZONE = 'America/Sao_Paulo'     # Horário de São Paulo

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'                      # Para poder criar arquivos .css para estilizar os templates locais das apps
STATICFILES_DIRS = [BASE_DIR / "static"]    # Para poder usar o arquivo .css global para estilizar o template global

# Configuração padrão para desenvolvimento
if DEBUG:
    # Armazenamento de arquivos estáticos
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
    # Toda vez que for modificado algum arquivo .css, deve-se usar o comando: 
    # python manage.py collectstatic

    # ALLOWED_HOSTS
    ALLOWED_HOSTS = ['*']  # Permite qualquer host para testes em desenvolvimento
# Configuração para produção
else:
    # Arquivos estáticos
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

    # ALLOWED_HOSTS
    ALLOWED_HOSTS = ['meusite.com', 'www.meusite.com']  # Defina os hosts reais da sua aplicação em produção

    # Desativa o painel amigável do DRF que permite testar se a API está funcionando (+ segurança) 
    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': [
            'rest_framework.renderers.JSONRenderer',
        ],
    }

 

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#CORS_ALLOW_ORIGINS_ALL = True  # Opção perigosa, qualquer domínio (site) poderia consumir nossa API

# Define quais domínios podem fazer requisições para a sua API
CORS_ALLOW_ORIGINS = [
    'http://localhost:8080',
    # Outros endereços durante o deploy (Azure, AWS ou qualquer outro, basta adicionar o endereço de hospedagem à lista)
    "https://example.com",          # Trocar depois
    "https://anotherdomain.com",    # Trocar depois
]