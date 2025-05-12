# db.py
# Este módulo contém funções para gerenciar a conexão com o banco de dados SQLite
# e inicializar o esquema do banco de dados para o sistema de inclusão digital.
# Importações necessárias
import sqlite3
from datetime import datetime


def get_conn():
    """
    Retorna conexão com o banco SQLite 'inclusion.db'.
    Usa Row factory para mapeamento de colunas por nome.
    """
    conn = sqlite3.connect('inclusion.db')
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Inicializa o esquema do banco, criando tabelas se não existirem.
    """
    sql = """
    CREATE TABLE IF NOT EXISTS Usuario (
      usuario_id    INTEGER PRIMARY KEY AUTOINCREMENT,
      nome          TEXT NOT NULL,
      email         TEXT UNIQUE NOT NULL,
      senha_hash    TEXT NOT NULL,
      data_cadastro TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Curso (
      curso_id      INTEGER PRIMARY KEY AUTOINCREMENT,
      titulo        TEXT NOT NULL,
      descricao     TEXT
    );

    CREATE TABLE IF NOT EXISTS Modulo (
      modulo_id     INTEGER PRIMARY KEY AUTOINCREMENT,
      fk_curso      INTEGER NOT NULL,
      titulo        TEXT NOT NULL,
      conteudo_texto TEXT,
      FOREIGN KEY(fk_curso) REFERENCES Curso(curso_id)
    );

    CREATE TABLE IF NOT EXISTS Inscricao (
      inscricao_id  INTEGER PRIMARY KEY AUTOINCREMENT,
      fk_usuario    INTEGER NOT NULL,
      fk_curso      INTEGER NOT NULL,
      data_inscricao TEXT NOT NULL,
      FOREIGN KEY(fk_usuario) REFERENCES Usuario(usuario_id),
      FOREIGN KEY(fk_curso)   REFERENCES Curso(curso_id)
    );

    CREATE TABLE IF NOT EXISTS Progresso (
      progresso_id  INTEGER PRIMARY KEY AUTOINCREMENT,
      fk_usuario    INTEGER NOT NULL,
      fk_modulo     INTEGER NOT NULL,
      concluido     INTEGER NOT NULL DEFAULT 0,
      data          TEXT,
      FOREIGN KEY(fk_usuario) REFERENCES Usuario(usuario_id),
      FOREIGN KEY(fk_modulo)  REFERENCES Modulo(modulo_id)
    );
    """
    conn = get_conn()
    conn.executescript(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    init_db()
    print("Banco de dados inicializado com sucesso.")