# API
# 1. criar uma api para disponibilizar a consulta, criação , edição e exclusão de um livro
# 2. URL Base - localhost
# 3. EndPoints - 
    # -localhost/livros/ (GET)
    # -localhost/livros/ (POST)
    # - localhost/livros/id (GET)
    # - localhost/livros/id (PUT)
    # - localhost/livros/id (DELETE)
# 4.

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'O Senhor dos Anéis 2',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 3,
        'título': 'O Senhor dos Anéis 3',
        'autor': 'J.R.R Tolkien'
    }
 ]

# CONSULTAR(TODOS)

@app.route('/livros')
def obter_livros():
    return jsonify(livros)


# Consultar (id)

@app.route('/livros/<int:id>', methods=['GET'])
def consultar_livros(id):
    for livro in livros:
       if livro.get('id') == id:
           return jsonify(livro)
# Editar

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
# CRIAR 

@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    
    return jsonify(livros)
# Excluir

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)