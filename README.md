ShoppeCenter – Sistema Interno de Gerenciamento de Tarefas

Sistema desenvolvido para otimizar a comunicação e organização entre os setores da empresa fictícia ShoppeCenter, criada para o setor de varejo online.

Objetivo
Organizar e monitorar tarefas internas dos setores:
- Marketing
- Logística
- Atendimento
- TI

Funcionalidades principais

Autenticação
- Login de usuários com validação
- Apenas usuários autenticados acessam o painel de tarefas
  
- Criar, editar, excluir e listar tarefas
- Definir setor, prioridade e status
- Atribuir responsáveis
- Visualização dinâmica no painel

Tecnologias

Integração
- Frontend conectado à API Flask via Fetch API
- Dados persistidos no banco MySQL (porta 3305)

  DevOps & Qualidade
- Pipeline CI com GitHub Actions (testes automatizados)
- Kanban gerenciado via GitHub Projects
- Versionamento com Git e boas práticas de commits
- 
Backend
-Python 3.11
- Flask (API REST)
- MySQL (porta 3305)
- ORM manual com conexão via mysql-connector
- Flask-CORS

Frontend
- HTML, CSS, JavaScript
- Layout responsivo

DevOps
- Git & GitHub
- GitHub Projects (Kanban)
- GitHub Actions (testes CI)
  
Metodologia
Projeto desenvolvido seguindo metodologia ágil baseada em Kanban.


Estrutura Atual do Projeto
ShoppeCenter/
├── app.py
├── database.py
├── models/
│   ├── tarefa.py
│   └── usuario.py
├── routes/
│   ├── tarefa_routes.py
│   └── auth_routes.py
├── frontend/
│   ├── index.html
│   ├── tarefas.html
│   ├── login.html
│   ├── style.css
│   ├── script.js
│   └── login.js
├── tests/
│   └── test_app.py
├── docs/
│   ├── schema.sql
│   ├── schema_usuarios.sql
│   └── create_usuarios_with_example.sql
├── .github/
│   └── workflows/
│       └── tests.yml
├── requirements.txt
└── README.md


Configuração e Execução
Clonar o repositório
- git clone https://github.com/Trixbeadev/ShoppeCenter-TaskManager.git
cd ShoppeCenter-TaskManager

Criar e ativar o ambiente virtual
- python -m venv venv
source venv/Scripts/activate  # Windows (Git Bash)

Instalar dependências
- pip install -r requirements.txt

Configurar o banco MySQL (porta 3305, dentro da pasta docs)
- source docs/schema.sql;
source docs/schema_usuarios.sql;
source docs/create_usuarios_with_example.sql;

Iniciar a API
- python app.py

http://127.0.0.1:5000/login.html

 (email: usuario@exemplo.com, senha: Senha123!)

Metodologia de Desenvolvimento

O projeto foi desenvolvido com base no Kanban, seguindo:


Planejamento	Requisitos e backlog - via GitHub Projects
Desenvolvimento	Implementação incremental - (frontend + backend)
Testes	Automatização - via GitHub Actions
Deploy	Entregas versionadas - via GitHub
Melhorias	Ajustes contínuos conforme demanda

Requisito adicional atendido:

Adição do campo prazo de entrega
Inclusão no banco, frontend e API
Exibição no layout e persistência no MySQL

 Desenvolvedora

Beatriz França
GitHub: @Trixbeadev
TechFlow Solutions

Obs:
Este projeto foi desenvolvido para fins acadêmicos, aplicando conceitos de:
Engenharia de Software
Clean Code
API REST
SQL
Versionamento e CI/CD
Metodologias ágeis

