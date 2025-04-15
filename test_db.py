"""
from app import db, app

with app.app_context():
    db.create_all()
    print("✅ Banco de dados 'tarefas.db' criado com sucesso!")


#Se você quiser que o banco fique diretamente na raiz do projeto, mude isso assim:

"""

"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'tarefas.db')}

"""
