
"""
from app import db

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    feito = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Tarefa {self.titulo}>'
    """




"""
        
         Explicação dos ajustes:
Construtor (__init__): Adicionei o construtor para garantir que, ao criar uma nova tarefa, o título seja atribuído e o campo feito seja configurado como False por padrão. Isso ajuda a garantir que o valor feito seja tratado de maneira consistente.

Uso do nullable=False para o título: Isso já estava correto. Ele garante que o título da tarefa seja obrigatório.

"""

from app import db

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Define a chave primária (ID)
    titulo = db.Column(db.String(100), nullable=False)  # O título não pode ser nulo
    feito = db.Column(db.Boolean, default=False)  # O campo feito tem valor padrão False

    def __repr__(self):
        return f'<Tarefa {self.titulo}>'
    
    def __init__(self, titulo):
        self.titulo = titulo
        self.feito = False 
         # Por padrão, a tarefa não está feita


