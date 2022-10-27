from ..models import formacao_model
from api import db

def cadastrar_formacao(formacao):
    formacao_db = formacao_model.Formacao(nome=formacao.nome, descricao=formacao.descricao)
    db.session.add(formacao_db)
    db.session.commit()
    return formacao_db

def listar_formacao():
    formacaoes = formacao_model.Formacao.query.all()
    return formacaoes

def listar_formacao_id(id):
    formacao = formacao_model.Formacao.query.filter_by(id=id).first()
    return formacao

def atualizar_formacao(formacao_anterior, formacao_nova):
    formacao_anterior.nome = formacao_nova.nome
    formacao_anterior.descricao = formacao_nova.descricao
    db.session.commit()

def remove_formacao(formacao):
    db.session.delete(formacao)
    db.session.commit()