# Tarefas Flask App

Este é um projeto simples de gerenciamento de tarefas utilizando Flask, SQLite e SQLAlchemy.

## Funcionalidades

- **GET /tarefas**: Retorna todas as tarefas armazenadas no banco de dados.
- **POST /tarefas**: Cria uma nova tarefa.
- **PUT /tarefas/{id}**: Atualiza o status (feito ou não) de uma tarefa existente.
- **DELETE /tarefas/{id}**: Exclui uma tarefa.

## Como rodar o projeto

1. Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/SEU-USUARIO/tarefas-flask.git
Navegue até o diretório do projeto:

bash
Copiar código
cd tarefas-flask
Crie e ative um ambiente virtual:

Windows:

bash
Copiar código
python -m venv venv
venv\Scripts\activate
macOS/Linux:

bash
Copiar código
python3 -m venv venv
source venv/bin/activate
Instale as dependências do projeto:

bash
Copiar código
pip install -r requirements.txt
Crie o banco de dados:

bash
Copiar código
python -c "from app import db; db.create_all()"
Inicie o servidor:

bash
Copiar código
python run.py
O aplicativo estará disponível em http://127.0.0.1:5000.

Tecnologias
Flask: Framework web em Python.

SQLite: Banco de dados utilizado.

SQLAlchemy: ORM (Object Relational Mapper) para interagir com o banco de dados.

Contribuindo
Faça o fork do repositório.

Crie uma branch para a sua feature: git checkout -b minha-feature.

Faça commit das suas alterações: git commit -m 'Adiciona nova feature'.

Envie para o seu repositório: git push origin minha-feature.

Abra um pull request.

Licença
Este projeto está licenciado sob a Licença MIT.
