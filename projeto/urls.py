#Importa funcionalidades do DJANGO e dentro dela o Admin (painel admistrativo do django)
from django.contrib import admin

#Importa Caaminhos para acessar arquivos e paginas
#INCLUDE: Eu acesso a urls.py do meu app
from django.urls import path, include

#Nome da lista onde ficam minhas rotas
urlpatterns = [
    #Vai criar um caminho admin/ onde quando eu executo ele faz um painel
    path('admin/', admin.site.urls),

    #Cria um caminho onde vai deste urls.py para o urls.py do meu app (cria um caminho daqui para lá)
    path('app/', include('app.urls'))
]
