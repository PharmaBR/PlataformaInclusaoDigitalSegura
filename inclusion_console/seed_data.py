import json
from db import init_db, get_conn

def seed_data():
    init_db()  # garante esquema criado
    conn = get_conn()
    cur = conn.cursor()

    # Carrega cursos e módulos do arquivo JSON
    with open('data/courses.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for course in data.get('courses', []):
        titulo = course['titulo']
        descricao = course.get('descricao', '')
        # Insere curso e obtém ID
        cur.execute(
            'INSERT OR IGNORE INTO Curso(titulo, descricao) VALUES (?, ?)',
            (titulo, descricao)
        )
        cur.execute('SELECT curso_id FROM Curso WHERE titulo = ?', (titulo,))
        curso_id = cur.fetchone()[0]

        # Insere módulos associados
        for mod in course.get('modulos', []):
            cur.execute(
                'INSERT OR IGNORE INTO Modulo(fk_curso, titulo, conteudo_texto) VALUES (?, ?, ?)',
                (curso_id, mod['titulo'], mod.get('conteudo_texto', ''))
            )

    conn.commit()
    conn.close()
    print('Dados de curso e módulos importados de JSON com sucesso.')

if __name__ == '__main__':
    seed_data()