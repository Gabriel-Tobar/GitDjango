#Adiciono tabelas de banco de dados no painel de admin para eu controlar ela

#De django importa admin (painel)
from django.contrib import admin

#De models importa minha tabela Usuario
from .models import Usuario

#Cria um painel com meu banco de dados (tabela)
class UsuarioAdmin(admin.ModelAdmin):
    #Exibe informações como colunas e etc para deixar mais bonito

    list_display = ('nome_usuario', 'email')  # Colunas mostradas na lista
    search_fields = ('nome_usuario', 'email')  # Campo para buscar rápido
    list_filter = ('email',)  # Filtros na lateral para segmentar dados

#Registra tudo no painel
admin.site.register(Usuario, UsuarioAdmin)

