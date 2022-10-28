from api import ma
from ..models import professor_model
from marshmallow import fields

class ProfessorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        professor = professor_model.Professor
        load_instance = True
        fields = ("id", "nome", "idade")

    nome = fields.String(required=True)
    idade = fields.Integer(required=True)