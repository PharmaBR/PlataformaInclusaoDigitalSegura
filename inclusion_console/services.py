from db import get_conn
from rich.console import Console
from models import (
    create_user,
    get_user_by_email,
    list_cursos as _list_cursos,
    list_modulos,
    enroll_user,
    mark_progress,
    get_progress
)

console = Console()


def login(email, senha_hash):
    """
    Retorna o usuário se credenciais estiverem corretas, senão None.
    """
    user = get_user_by_email(email)
    if user and user['senha_hash'] == senha_hash:
        return user
    return None


def register_user(nome, email, senha_hash):
    """
    Registra novo usuário se email não existir.
    """
    if get_user_by_email(email):
        print("Email já cadastrado.")
        return False
    create_user(nome, email, senha_hash)
    print("Usuário cadastrado com sucesso.")
    return True


def list_cursos():
    """
    Exibe todos os cursos disponíveis.
    """
    print("Cursos Disponíveis:")
    _list_cursos()


def enroll(usuario_id, curso_id):
    """
    Inscreve usuário em um curso.
    """
    enroll_user(usuario_id, curso_id)
    print(f"Inscrição realizada: usuário {usuario_id} no curso {curso_id}.")


def list_modulos_enrolled(usuario_id):
    """
    Lista módulos de todos os cursos em que o usuário está inscrito.
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT C.curso_id, C.titulo FROM Curso C JOIN Inscricao I ON C.curso_id = I.fk_curso WHERE I.fk_usuario = ?",
        (usuario_id,)
    )
    cursos = cur.fetchall()
    conn.close()
    for curso in cursos:
        print(f"Módulos do curso {curso['titulo']}: (ID {curso['curso_id']})")
        modulos = list_modulos(curso['curso_id'])
        for m in modulos:
            print(f"{m['modulo_id']}: {m['titulo']}")


def mark_complete(usuario_id, modulo_id):
    """
    Marca um módulo como concluído para o usuário.
    """
    mark_progress(usuario_id, modulo_id)
    print(f"Módulo {modulo_id} marcado como concluído.")


def show_progress(usuario_id):
    """
    Exibe relatório de progresso do usuário.
    """
    rows = get_progress(usuario_id)
    print("Relatório de Progresso:")
    for row in rows:
        status = "Concluído" if row['concluido'] else "Pendente"
        data = row['data'] if row['data'] else '-'
        print(f"{row['modulo_id']}: {row['titulo']} - {status} - {data}")

def view_module_content(modulo_id):
    """
    Busca e exibe o conteúdo de um módulo a partir do seu ID.
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT titulo, conteudo_texto FROM Modulo WHERE modulo_id = ?",
        (modulo_id,)
    )
    mod = cur.fetchone()
    conn.close()

    if mod:
        console.rule(f"Conteúdo: {mod['titulo']}")
        console.print(mod['conteudo_texto'])
    else:
        console.print("[red]Módulo não encontrado.[/red]")