from flask_restful import Resource
from api import api
from ..schemas import professor_schema
from flask import request, make_response, jsonify
from ..entidades import professor
from ..services import professor_service


class ProfessorList(Resource):
    def get(self):
        professor = professor_service.listar_professores()
        ps = professor_schema.ProfessorSchema(many=True)
        return make_response(ps.jsonify(professor), 200)

    def post(self):
        ps = professor_schema.ProfessorSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            idade = request.json["idade"]

            novo_professor = professor.Professor(nome=nome, idade=idade)
            resultado = professor_service.cadastrar_professor(novo_professor)
            x = ps.jsonify(resultado)
            return make_response(x, 201)


class ProfessorDetail(Resource):
    def get(self, id):
        professor = professor_service.listar_professores_id(id)
        if professor is None:
            return make_response(jsonify("Professor não foi encontrado"), 404)
        ps = professor_schema.ProfessorSchema()
        return make_response(ps.jsonify(professor), 200)

    def put(self, id):

        professor_bd = professor_service.listar_professores_id(id)
        if professor_bd is None:
            return make_response(jsonify("O professor não foi encontrado"), 404)
        ps = professor_schema.ProfessorSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            idade = request.json["idade"]

            novo_professor = professor.Professor(nome=nome, idade=idade)
            professor_service.atualizar_professor(professor_bd, novo_professor)
            professor_atualizada = professor_service.listar_professores_id(id)
            return make_response(ps.jsonify(professor_atualizada), 200)

    def delete(self, id):
        professor_db = professor_service.listar_professores_id(id)
        if professor_db is None:
            return make_response(jsonify("Professor não encontrado"), 404)
        professor_service.remove_professor(professor_db)
        return make_response("Professor excluído com sucesso", 204)

api.add_resource(ProfessorList, '/professores')
api.add_resource(ProfessorDetail, '/professores/<int:id>')
