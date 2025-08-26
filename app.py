from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/soma', methods=['GET'])
def soma():
    """
    Soma dois números
    ---
    parameters:
      - name: a
        in: query
        type: number
        required: true
        description: Primeiro número
      - name: b
        in: query
        type: number
        required: true
        description: Segundo número
    responses:
      200:
        description: Resultado da soma
        schema:
          type: object
          properties:
            resultado:
              type: number
    """
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))

    return jsonify({'resultado': a + b})

@app.route('/subtracao', methods=['GET'])
def subtracao():
    """
    Subtrai dois números
    ---
    parameters:
      - name: a
        in: query
        type: number
        required: true
        description: Primeiro número
      - name: b
        in: query
        type: number
        required: true
        description: Segundo número
    responses:
      200:
        description: Resultado da subtração
        schema:
          type: object
          properties:
            resultado:
              type: number
    """
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))

    return jsonify({'resultado': a - b})

@app.route('/multiplicacao', methods=['GET'])
def multiplicacao():
    """
    Multiplica dois numeros
    ---
    parameters:
      - name: a
        in: query
        type: number
        required: true
        description: Primeiro número
      - name: b
        in: query
        type: number
        required: true
        description: Segundo número
    responses:
       200:
        description: Resultado da multiplicação
        schema:
          type: object 
          properties:
            resultado:
              type: number
    """

    a = float(request.args.get('a'))
    b = float(request.args.get('b'))

    return jsonify({'resultado': a * b})

@app.route('/divisao', methods=['GET'])
def divisao():
    """
    Divide dois números
    ---
    parameters:
      - name: a
        in: query
        type: number
        required: true
        description: Primeiro número
      - name: b
        in: query
        type: number
        required: true
        description: Segundo número
    responses:
      200:
        description: Resultado da divisão
        schema:
          type: object
          properties:
            resultado:
              type: number
      400:
        description: Erro de divisão por zero
        schema:
          type: object
          properties:
            error:
              type: string
    """
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))

    if b == 0:
        return jsonify({'error': 'Divisao por zero nao e permitida'}), 400

    return jsonify({'resultado': a / b})

if __name__ == '__main__':
    app.run(debug=True)