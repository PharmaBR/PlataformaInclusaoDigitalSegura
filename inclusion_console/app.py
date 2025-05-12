from db import init_db
from services import (
    login,
    register_user,
    list_cursos,
    enroll,
    list_modulos_enrolled,
    mark_complete,
    show_progress, 
    view_module_content
)
from getpass import getpass
from hashlib import sha256
from rich.console import Console
from rich.prompt import Prompt

# Inicializa console Rich
console = Console()


def hash_password(pw):
    return sha256(pw.encode()).hexdigest()


def menu_anonimo():
    console.print("\n[bold cyan]Inclusão Digital Segura[/bold cyan]")
    console.print("1) Cadastrar  2) Login  3) Sair")
    return Prompt.ask("Escolha", choices=["1","2","3"])


def menu_logado(user):
    console.print(f"\n[bold green]Olá, {user['nome']}![/bold green]")
    console.print("1) Listar cursos  2) Inscrever  3) Meus módulos")
    console.print("4) Ver conteúdo de módulo  5) Marcar concluído  6) Ver progresso  7) Logout")
    return Prompt.ask("Escolha", choices=["1","2","3","4","5","6","7"])


def main():
    init_db()
    user = None
    while True:
        if not user:
            choice = menu_anonimo()
            if choice == '1':
                nome = Prompt.ask("Nome")
                email = Prompt.ask("Email")
                pw = Prompt.ask("Senha", password=True)
                register_user(nome, email, hash_password(pw))
            elif choice == '2':
                email = Prompt.ask("Email")
                pw = Prompt.ask("Senha", password=True)
                user = login(email, hash_password(pw))
                if not user:
                    console.print("[red]Credenciais inválidas.[/red]")
            else:
                console.print("Saindo...")
                break
        else:
            choice = menu_logado(user)
            if choice == '1':
                list_cursos()
            elif choice == '2':
                cid = int(Prompt.ask("ID do curso"))
                enroll(user['usuario_id'], cid)
            elif choice == '3':
                list_modulos_enrolled(user['usuario_id'])
            elif choice == '4':
                mid = int(Prompt.ask("ID do módulo"))
                view_module_content(mid)
            elif choice == '5':
                mid = int(Prompt.ask("ID do módulo"))
                mark_complete(user['usuario_id'], mid)
            elif choice == '6':
                show_progress(user['usuario_id'])
            else:
                user = None
                console.print("[yellow]Logout realizado.[/yellow]")


if __name__ == '__main__':
    main()