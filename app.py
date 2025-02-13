from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/saudacao', methods=['GET'])
def saudacao():
    nome = request.args.get('name')
    if nome:
        return f"Olá, {nome}!"
    else:
        return "Olá, Recursos Humanos do Hospital Albert Einstein!"

@app.route('/soma', methods=['POST'])
def soma():
    try:
        data = request.get_json()
        num1 = data['num1']
        num2 = data['num2']
        resultado = num1 + num2
        return jsonify({'soma': resultado})
    except (TypeError, KeyError):
        return jsonify({'erro': 'Parâmetros inválidos'})

if __name__ == '__main__':
    app.run(debug=True)
