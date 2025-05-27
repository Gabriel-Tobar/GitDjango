#ASGI.PY: Tradutor simultanio com chat ao vivo e muito mais e ele é novo e tem capacidade de fazer multitarefas...
#Nunca mexer pois ja estão configurados...

#Importa sistema operacional (chefe cargo)
import os

#Junta django com WSGI
from django.core.asgi import get_asgi_application

#Use o arquivo de configurações meuprojeto/settings.py como base do projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')

#os.environ.: Ativação para deixar algo como base do projeto
#setdefault: evita erro
#DJANGO_SETTINGS_MODULE: Onde esta settings para ele chegar la
#nome.settings: Nome da pasta e dento do arquivo

# Cria a aplicação ASGI — o servidor (como Uvicorn) vai usar essa variável para rodar seu site moderno

#Aplica tudo e roda o site
application = get_asgi_application()
