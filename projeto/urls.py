#Importa funcionalidades do DJANGO e dentro dela o Admin (painel admistrativo do django)
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
]
