# Importa a função render, que carrega e exibe um arquivo HTML
from django.shortcuts import render

# Esta função será chamada quando o usuário acessar /app/login/
def login_view(request):
    # O Django vai procurar um arquivo chamado login.html dentro da pasta templates/
    return render(request, 'login.html')

#REQUEST: Requisição do usuario, o usuario tem que requerir algo dentro da pagina

# Esta função será chamada quando o usuário acessar /app/parabens/
def parabens_view(request):
    # O Django vai carregar o arquivo parabens.html e mostrar na tela
    return render(request, 'parabens.html')


# return: devolve uma resposta
# render(...): chama o Django para carregar e mostrar um arquivo HTML
# request: a requisição do usuário
# 'login.html': nome do arquivo HTML que será carregado da pasta templates/

