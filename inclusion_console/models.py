from db import get_conn
from datetime import datetime

def create_user(nome, email, senha_hash):
    conn = get_conn()
    cur = conn.cursor()
    data_cadastro = datetime.now().isoformat()
    cur.execute(
        "INSERT INTO Usuario(nome, email, senha_hash, data_cadastro) VALUES (?, ?, ?, ?)",
        (nome, email, senha_hash, data_cadastro)
    )
    conn.commit()
    conn.close()

def get_user_by_email(email):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Usuario WHERE email = ?", (email,))
    user = cur.fetchone()
    conn.close()
    return user

def list_cursos():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Curso")
    cursos = cur.fetchall()
    conn.close()
    for curso in cursos:
        print(f"{curso['curso_id']}: {curso['titulo']} - {curso['descricao']}")

def list_modulos(curso_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Modulo WHERE fk_curso = ?", (curso_id,))
    modulos = cur.fetchall()
    conn.close()
    return modulos

def enroll_user(usuario_id, curso_id):
    conn = get_conn()
    cur = conn.cursor()
    data_inscricao = datetime.now().isoformat()
    cur.execute(
        "INSERT INTO Inscricao(fk_usuario, fk_curso, data_inscricao) VALUES (?, ?, ?)",
        (usuario_id, curso_id, data_inscricao)
    )
    conn.commit()
    conn.close()

def mark_progress(usuario_id, modulo_id):
    conn = get_conn()
    cur = conn.cursor()
    data = datetime.now().isoformat()
    cur.execute(
        "INSERT OR REPLACE INTO Progresso(fk_usuario, fk_modulo, concluido, data) VALUES (?, ?, ?, ?)",
        (usuario_id, modulo_id, 1, data)
    )
    conn.commit()
    conn.close()

def get_progress(usuario_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT M.modulo_id, M.titulo, P.concluido, P.data FROM Modulo M LEFT JOIN Progresso P ON M.modulo_id = P.fk_modulo AND P.fk_usuario = ?",
        (usuario_id,)
    )
    rows = cur.fetchall()
    conn.close()
    return rows