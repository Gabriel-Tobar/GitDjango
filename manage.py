#Configuração do meu site, nao devo alterar nada independende do codigo so se eu mudar o nome do projeto

#Tem a funcionalidade de dar regras ao meu site e deixar eu dar comando no terminal

#Comando utilizados: | Comando           | Função                               |
# | ----------------- | ------------------------------------ |
# | `runserver`       | Roda o servidor                      |
# | `makemigrations`  | Detecta mudanças nos modelos         |
# | `migrate`         | Aplica mudanças no banco             |
# | `createsuperuser` | Cria admin                           |
# | `startapp`        | Cria um app novo                     |
# | `shell`           | Terminal Python com acesso ao Django |
# | `showmigrations`  | Mostra as migrações existentes       |
# | `flush`           | Apaga tudo do banco                  |
# | `test`            | Roda testes automatizados            |




"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
