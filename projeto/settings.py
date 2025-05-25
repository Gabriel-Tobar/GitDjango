#Importa arquivos: Path caminho para algum aquivo
from pathlib import Path 
#Importa .env para segurança do meu site
from decouple import config


# Chama arquivos BASE DIR:significa que tudo que vem depois de BASE_DIR ele busca algun aruivo com o caminho path
BASE_DIR = Path(__file__).resolve().parent.parent

#De forma simples BASE_DIR: Buscar

# Chave de segurança do site, subir para .env
SECRET_KEY = config('SECRET_KEY')  # Deixa minha chave segura e puxa ela do .env

# Erros do site, subir para .env
DEBUG = config('DEBUG', cast=bool)  #Deixe meus erros seguros e puxa do .env

#Adicionar dominio de site, após finalização
ALLOWED_HOSTS = []


# Apps instalados
#Adicionar novo app se houver
INSTALLED_APPS = [
    'django.contrib.admin',     # Painel administrativo
    'django.contrib.auth',      # Sistema de autenticação (login, senhas)
    'django.contrib.contenttypes', 
    'django.contrib.sessions',  # Controle de sessões
    'django.contrib.messages',  # Mensagens entre telas
    'django.contrib.staticfiles', # Arquivos estáticos (CSS, JS, imagens)
    'app', #Meu app
]

# Seguranaça de padrão do Django
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',       # Segurança básica
    'django.contrib.sessions.middleware.SessionMiddleware', # Gerencia sessão do usuário (login)
    'django.middleware.common.CommonMiddleware',            # Regras comuns de acesso
    'django.middleware.csrf.CsrfViewMiddleware',            # Proteção contra ataques CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Lida com usuário autenticado
    'django.contrib.messages.middleware.MessageMiddleware',  # Gerencia mensagens entre páginas
]

# Nome do projeto django (Alterar se vc mudar o nome)
ROOT_URLCONF = 'projeto.urls'

# Template para HTML 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], #Vai procurar uma pasta chamada templates onde vai ficar meu HTML
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Rodar django em produção
WSGI_APPLICATION = 'projeto.wsgi.application'

# Tipo do banco: SQLite3 (Se nao for, alterar)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Tipo do banco
        'NAME': BASE_DIR / 'db.sqlite3',         # Caminho do arquivo do banco
    }
}

# Validação de senha do django, para ter senhas seguras
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

# Tipo de site 
LANGUAGE_CODE = 'pt-br' #Alterar para seu idioma

TIME_ZONE = 'America/Sao_Paulo' #Alterar para seu fuso-horario(pesquisar)

USE_I18N = True

USE_TZ = True

# Arquivos CSS, JS e Imagens são adicionados aqui para ligar com o back

#Caminho que o navegador vai usar para chegar em arquivos staticos
STATIC_URL = 'static/'

#Local onde vão ficar meus arquivos staticos tanto quanto (IMG, JS E CSS) tudo dentro de uma pasta static
STATICFILES_DIRS = [BASE_DIR / 'static']

# Define o tipo padrão das chaves primárias em modelos.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
