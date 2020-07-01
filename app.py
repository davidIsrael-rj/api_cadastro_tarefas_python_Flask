from flask import Flask, jsonify, request
import json
app = Flask(__name__)

tarefas =[
    {
        'id':0,
        'responsavel': 'David',
        'tarefa': 'Desenvolver método GET',
        'status': 'concluido'
    },
    {
        'id':1,
        'responsavel':'Israel',
        'tarefa':'Desenvolver método POST',
        'status':'pendente'
    }
]

@app.route('/tarefa/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def tarefa(id):
    if request.method =='GET':
        try:
            response = tarefas[id]
        except IndexError:
            mensagem = 'Tarefa de de ID {} não existe'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return jsonify(response)
    elif request.method =='PUT':
        dados = json.loads(request.data)
        tarefas[id]['status'] = dados['status']
        #return jsonify(dados)
        return jsonify(tarefas[id])
    elif request.method =='DELETE':
        tarefas.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluído'})

@app.route('/tarefa/', methods = ['POST', 'GET'])
def lista_tarefas():
    if request.method =='POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao
        tarefas.append(dados)
        return jsonify(tarefas[posicao])
    elif request.method =='GET':
        return  jsonify(tarefas)

if __name__ == '__main__':
    app.run(debug=True)