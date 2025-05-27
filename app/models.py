#Models: Cria um modelo da sua tabela, essencial para todo o site backend

#Importa banco de dados do django e pega models dentro dele 
from django.db import models

#Cria a tabela ( class Nome_da_tabela )
class Usuario(models.Model):
    #Cria uma variavel com no maximo 100 caracteres e tem que ser unico
    nome_usuario = models.CharField(max_length=100, unique=True)

    #Cria uma variavel e tem que ser unico 
    email = models.EmailField(unique=True)

    #Cria uma variavel e tem que ter no maximo 100 carcteres
    senha = models.CharField(max_length=100)

    #Mostra um resultado nao ID, ela retorna o nome de usuario nao ID...
    def __str__(self):
        return self.nome_usuario
    
    
    #CharField = Texto pequeno
    # TextField	        Texto grande	            'Descrição longa...'
    # EmailField	    Email validado	            'exemplo@email.com'
    # IntegerField	    Número inteiro	            15, 1000
    # BooleanField	    Verdadeiro ou Falso	        True, False
    # DateTimeField	    Data e hora	2025-05-27      15:30:00
    # ForeignKey	    Relacionamento 1 para N	    Liga uma tabela na outra
    # ManyToManyField	Relacionamento N:N	        Muitas coisas para muitas


