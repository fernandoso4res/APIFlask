from ..models import professor_model
from api import db

def cadastrar_professor(professor):
    professor_db = professor_model.Professor(nome=professor.nome, idade=professor.idade)
    db.session.add(professor_db)
    db.session.commit()
    return professor_db

def listar_professores():
    professores = professor_model.Professor.query.all()
    return professores

def listar_professores_id(id):
    professor = professor_model.Professor.query.filter_by(id=id).first()
    return professor

def atualizar_professor(professor_anterior, professor_nova):
    professor_anterior.nome = professor_nova.nome
    professor_anterior.idade = professor_nova.idade
    db.session.commit()

def remove_professor(professor):
    db.session.delete(professor)
    db.session.commit()