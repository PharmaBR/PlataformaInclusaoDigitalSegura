# Inclusão Digital Segura – Console MVP

Uma aplicação de linha de comando em Python para cadastro de usuários, inscrição em cursos, navegação por módulos e acompanhamento de progresso.

---

## Índice

1. [Funcionalidades](#funcionalidades)  
2. [Tecnologias](#tecnologias)  
3. [Pré-requisitos](#pré-requisitos)  
4. [Instalação](#instalação)  
5. [Inicializando o Banco de Dados](#inicializando-o-banco-de-dados)  
6. [Uso](#uso)  
7. [Estrutura do Projeto](#estrutura-do-projeto)  
8. [Contribuindo](#contribuindo)  
9. [Licença](#licença)  

---

## Funcionalidades

- 🚀 Cadastro e login de usuários  
- 📚 Listagem de cursos disponíveis  
- 📝 Inscrição de usuários em cursos  
- 📖 Listagem de módulos de cada curso  
- ✅ Marcação de módulos como concluídos  
- 📊 Relatório de progresso de cada usuário  

---

## Tecnologias

- Python 3.7+  
- SQLite (via módulo `sqlite3`)  
- [Rich](https://pypi.org/project/rich) para interface de console colorida  
- Outras dependências listadas em [`requirements.txt`](requirements.txt)  

---

## Pré-requisitos

- macOS, Linux ou Windows  
- Python 3.7 ou superior  
- Git  

---

## Instalação

```bash
# 1. Clone este repositório
git clone <URL_DO_REPOSITORIO>
cd PIM

# 2. (Opcional) Crie e ative um ambiente virtual
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows

# 3. Instale as dependências
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Inicializando o Banco de Dados

```bash
# Cria o arquivo inclusion.db e as tabelas
python -m inclusion_console.db

# (Opcional) Popula cursos e módulos a partir de JSON
python -m inclusion_console.seed_data
```

---

## Uso

```bash
# Inicie a aplicação
python -m inclusion_console.app
```

### Menu Anônimo

1. Cadastrar usuário  
2. Login  
3. Sair  

### Menu Após Login

1. Listar cursos  
2. Inscrever em curso (informe ID do curso)  
3. Meus módulos  
4. Ver conteúdo de módulo (informe ID do módulo)  
5. Marcar módulo como concluído (informe ID do módulo)  
6. Ver progresso  
7. Logout  

---

## Estrutura do Projeto

```
PIM/
├── inclusion_console/
│   ├── app.py             # Loop principal e menus
│   ├── db.py              # Conexão e inicialização SQLite
│   ├── models.py          # CRUD e mapeamento ORM simples
│   ├── services.py        # Lógica de negócio
│   ├── seed_data.py       # Script de importação de `data/courses.json`
│   └── data/
│       └── courses.json   # Dados iniciais de cursos e módulos
├── inclusion.db           # Banco SQLite (ignorado pelo Git)
├── requirements.txt       # Dependências do projeto
└── README.md              # Este arquivo
```

---

## Contribuindo

1. Abra uma _issue_ para discutir mudanças ou melhorias.  
2. Faça um _fork_ do repositório.  
3. Crie uma _branch_ (`git checkout -b feature/nova-funcionalidade`).  
4. Faça _commit_ das suas alterações (`git commit -m 'Adiciona nova funcionalidade'`).  
5. Envie para o _branch_ remoto (`git push origin feature/nova-funcionalidade`).  
6. Abra um _Pull Request_ descrevendo suas mudanças.  

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).  
