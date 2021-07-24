"""Dummy views module."""

from app.conhece.model import initial_setup
from flask import Blueprint,request
from flask_restx import Api, Resource
import json

from .model import *

conhece = Blueprint("conhece", __name__)

api = Api(
    conhece,
    title="Amizade API object",
    description="Endpoit responsavel pelo grafo"
)


@api.route("/")
class ConheceResource(Resource):
    @staticmethod
    def get():
        return get_all_nodes()

@api.route("/<string:name>")
class ConheceResource(Resource):
    def get(self,name):
        return get_friends(name)

@api.route("/nao/<string:name>")
class ConheceResource(Resource):
    def get(self,name):
        return get_not_friends(name)

@api.route("/cadastrar")
class ConheceResource(Resource):
    def post(self):
        content = request.json
        for name in content:
            insert_person(name,content[name])
        return "ok"