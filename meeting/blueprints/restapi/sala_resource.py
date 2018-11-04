from flask import current_app as app
from flask_restful import reqparse, Resource

sala_post_parser = reqparse.RequestParser()
sala_post_parser.add_argument('nome', required=True)
sala_post_parser.add_argument('capacidade', required=True)


class SalaList(Resource):
    def get(self):
        return {'salas': list(app.db['salas'].find())}

    def post(self):
        sala = sala_post_parser.parse_args()
        nova_sala = app.db['salas'].insert({'nome': sala.nome, 'capacidade': sala.capacidade})
        return {'sala criada': nova_sala.inserted_id}, 201


class Sala(Resource):

    def put(self, sala_id):
        sala = sala_post_parser.parse_args()
        app.db['salas'].update_one({'_id': sala_id}, {"$set": sala})

        return {'sala atualizada': sala_id}, 200

    def delete(self, sala_id):
        app.db['salas'].delete_one({'_id': sala_id})

        return {'sala excluida': sala_id}, 200
