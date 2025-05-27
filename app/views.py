#Faz um caminho para mostrar arquivos HTML
#Caminho para autentificação de login

#Importa render = mostra arquivos HTML e redirect = redireciona arquivos de um para o outro
from django.shortcuts import render, redirect

#Impora o bando de dados para consultalo na autentificação
from .models import Usuario

#Mostra mensagens de erro
from django.contrib import messages

#Cria uma função para quando digitar /algo va para esta pagina
def login_view(request):
    #Se usuario enviou o formulario então:
    if request.method == 'POST':

        #Pega os dados que o usuario digitou
        nome = request.POST['usuario']#[ser igual ao HTML]
        email = request.POST['email']#[ser igual ao HTML]
        senha = request.POST['senha']#[ser igual ao HTML]

        # Se o usuario já existe enão:
        if Usuario.objects.filter(nome_usuario=nome).exists():
            #Mostra mensagem de erro e volta para a tela de login
            messages.error(request, 'Usuário já existe')
            return redirect('login')
        #Se email ja existe volta para a tela de login e fala um erro
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado')
            return redirect('login')
        #Se os dados estão certos ele acessa a pagina parabens
        Usuario.objects.create(nome_usuario=nome, email=email, senha=senha)
        return redirect('parabens') 

    return render(request, 'login.html')  # Abre a tela se for GET

#Cria uma função para quando digitar /algo va para esta pagina
def parabens_view(request):
    return render(request, 'parabens.html')

#GET: Pega info
#POST: Envia info
