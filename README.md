# README.md

# Inclusão Digital Segura - Console MVP

## Visão Geral

Este projeto fornece uma aplicação de console em Python para inclusão digital segura. O objetivo é oferecer um ambiente simples para cadastro de usuários, inscrição em cursos, navegação por módulos e registro de progresso.

## Funcionalidades do MVP

* Cadastro e login de usuários
* Listagem de cursos disponíveis
* Inscrição de usuários em cursos
* Listagem de módulos de cada curso
* Marcação de módulos como concluídos
* Relatório de progresso de cada usuário

## Estrutura de Pastas

```
inclusion_console/
├─ db.py            # Conexão e inicialização do SQLite
├─ models.py        # Funções CRUD para cada entidade
├─ services.py      # Lógica de negócio (login, inscrição, progresso)
├─ app.py           # Menu principal e loop de comandos
└─ README.md        # Este arquivo de instruções
```

## Requisitos

* Python 3.7+
* Módulo `sqlite3` (builtin)

## Instalação

1. Clone o repositório:

   ```bash
   ```

git clone \<URL\_DO\_REPOSITORIO>
cd inclusion\_console

````
2. (Opcional) Crie e ative um ambiente virtual:
   ```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate   # Windows
````

3. Instale dependências (não há externas, mas mantenha `requirements.txt` atualizado):

   ```bash
   ```

pip install -r requirements.txt

````
4. Inicialize o banco de dados:
   ```bash
python db.py
````

## Uso

1. Execute a aplicação:

   ```bash
   ```

python app.py

```
2. Menu anônimo:
   - `1` Cadastrar usuário
   - `2` Login
   - `3` Sair
3. Após login, utilize as opções para navegar em cursos, inscrever-se, marcar progresso e visualizar relatório.

---

# .gitignore
```

# Byte-compiled / optimized / DLL files

**pycache**/
\*.py\[cod]
\*\$py.class

# C extensions

\*.so

# Distribution / packaging

.Python
build/
develop-eggs/
dist/
downloads/
.eggs/
.eggs-info/
lib/
lib64/
parts/
sdist/
var/
\*.egg-info/
.installed.cfg
\*.egg

# Virtual environments

venv/
.env
.venv/
env/

# IDEs and editors

.vscode/
.idea/
\*.sublime-project
\*.sublime-workspace

# SQLite database file

inclusion.db

# OS files

.DS\_Store
Thumbs.db

```
```
