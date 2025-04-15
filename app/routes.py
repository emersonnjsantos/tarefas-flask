from flask import jsonify, request
from app import app, db
from app.tarefas import Tarefa
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    tarefas = Tarefa.query.all()  # Busca todas as tarefas do banco
    return jsonify([
        {'id': t.id, 'titulo': t.titulo, 'feito': t.feito} for t in tarefas
    ])

@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    data = request.get_json()
    if 'titulo' not in data:
        return jsonify({'erro': 'O título é obrigatório'}), 400  # Verifica se o título foi enviado
    nova_tarefa = Tarefa(titulo=data['titulo'])
    db.session.add(nova_tarefa)
    db.session.commit()
    return jsonify({'id': nova_tarefa.id, 'titulo': nova_tarefa.titulo, 'feito': nova_tarefa.feito}), 201

@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)  # Caso a tarefa não seja encontrada, retorna erro 404
    data = request.get_json()
    
    # Atualiza os valores de título e feito
    if 'titulo' in data:
        tarefa.titulo = data['titulo']
    if 'feito' in data:
        tarefa.feito = data['feito']
    
    db.session.commit()
    return jsonify({'id': tarefa.id, 'titulo': tarefa.titulo, 'feito': tarefa.feito})

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)  # Caso a tarefa não seja encontrada, retorna erro 404
    db.session.delete(tarefa)
    db.session.commit()
    return jsonify({'mensagem': 'Tarefa removida com sucesso'})







"""

from flask import jsonify, request
from app import app, db
from app.tarefas import Tarefa
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    tarefas = Tarefa.query.all()
    return jsonify([
        {'id': t.id, 'titulo': t.titulo, 'feito': t.feito} for t in tarefas
    ])

@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    data = request.get_json()
    nova = Tarefa(titulo=data['titulo'])
    db.session.add(nova)
    db.session.commit()
    return jsonify({'id': nova.id, 'titulo': nova.titulo, 'feito': nova.feito}), 201

@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)
    data = request.get_json()
    tarefa.titulo = data.get('titulo', tarefa.titulo)
    tarefa.feito = data.get('feito', tarefa.feito)
    db.session.commit()
    return jsonify({'id': tarefa.id, 'titulo': tarefa.titulo, 'feito': tarefa.feito})

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)
    db.session.delete(tarefa)
    db.session.commit()
    return jsonify({'mensagem': 'Tarefa removida com sucesso'})
"""