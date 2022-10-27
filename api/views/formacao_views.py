from flask_restful import Resource
from api import api
from ..schemas import formacao_schema
from flask import request, make_response, jsonify
from ..entidades import formacao
from ..services import formacao_service


class FormacaoList(Resource):
    def get(self):
        formacao = formacao_service.listar_formacao()
        fs = formacao_schema.FormacaoSchema(many=True)
        return make_response(fs.jsonify(formacao), 200)

    def post(self):
        fs = formacao_schema.FormacaoSchema()
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]

            nova_formacao = formacao.Formacao(nome=nome, descricao=descricao)
            resultado = formacao_service.cadastrar_formacao(nova_formacao)
            x = fs.jsonify(resultado)
            return make_response(x, 201)


class FormacaoDetail(Resource):
    def get(self, id):
        formacao = formacao_service.listar_formacao_id(id)
        if formacao is None:
            return make_response(jsonify("Curso não foi encontrado"), 404)
        fs = formacao_schema.FormacaoSchema()
        return make_response(fs.jsonify(formacao), 200)

    def put(self, id):

        formacao_bd = formacao_service.listar_formacao_id(id)
        if formacao_bd is None:
            return make_response(jsonify("O curso não foi encontrado"), 404)
        fs = formacao_schema.FormacaoSchema()
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]

            nova_formacao = formacao.Formacao(nome=nome, descricao=descricao)
            formacao_service.atualizar_formacao(formacao_bd, nova_formacao)
            formacao_atualizada = formacao_service.listar_formacao_id(id)
            return make_response(fs.jsonify(formacao_atualizada), 200)

    def delete(self, id):
        formacao_db = formacao_service.listar_formacao_id(id)
        if formacao_db is None:
            return make_response(jsonify("Curso não encontrado"), 404)
        formacao_service.remove_formacao(formacao_db)
        return make_response("Cursp excluído com sucesso", 204)

api.add_resource(FormacaoList, '/formacoes')
api.add_resource(FormacaoDetail, '/formacoes/<int:id>')
