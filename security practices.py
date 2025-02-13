from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configuração de usuário e senha (substitua por um banco de dados)
user = {'username': 'admin', 'password_hash': generate_password_hash('1234')}

@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.form['username']
        password = request.form['password']

        if username == user['username'] and check_password_hash(user['password_hash'], password):
            return jsonify({'message': 'Acesso concedido'})
        else:
            return jsonify({'message': 'Acesso negado'}), 401
    except Exception as e:
        return jsonify({'message': 'Erro ao realizar login'}), 500

if __name__ == '__main__':
    app.run(debug=True)