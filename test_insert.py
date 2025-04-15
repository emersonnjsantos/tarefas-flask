
"""
from app import db, app
from app.tarefas import Tarefa

with app.app_context():
    nova = Tarefa(titulo='Estudar Flask')
    db.session.add(nova)
    db.session.commit()
    print(f"Tarefa criada: id={nova.id}, titulo={nova.titulo}, feito={nova.feito}")
"""