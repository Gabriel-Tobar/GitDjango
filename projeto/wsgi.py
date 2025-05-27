#WSGI.PY: Tradutor antigo mas faz coisas pequenas e projetos pequenos...
#Nunca mexer pois ja estão configurados...

#Importa sistema operacional (chefe cargo)
import os

#Junta django com WSGI
from django.core.wsgi import get_wsgi_application

#Use o arquivo de configurações meuprojeto/settings.py como base do projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')

#os.environ.: Ativação para deixar algo como base do projeto
#setdefault: evita erro
#DJANGO_SETTINGS_MODULE: Onde esta settings para ele chegar la
#nome.settings: Nome da pasta e dento do arquivo

# Gunicorn é o que roda seu Django quando você publica ele na internet.

#Aplica tudo e roda o site
application = get_wsgi_application()