#importa caminho de django urls
from django.urls import path

#Da pasta atual importa views
from . import views

#Cria uma variavel com o nome do app para nao ter bagunça se houver varios apps
app_name = 'app'

#Começa a lista de rotas
urlpatterns = [

    #Cria um caminho quando eu digitar login/ eu vou para login.html quando eu executo oque aparece vem de views
    path('login/', views.login_view, name='login'),

    #Cria um caminho que foi feito para mostrar com views que ao digitar parabens/ aparece parabens.html
    path('parabens/', views.parabens_view, name='parabens'),

    #views.função_views,
]

#A parte de urls voce precisa inicira com urls e depois views pense que o urls mostra o caminho e views oque aparece quando
# digito o caminho 
