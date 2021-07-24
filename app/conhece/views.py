"""Dummy views module."""

from app.conhece.model import initial_setup
from flask import Blueprint
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
    """Dummy resource."""

    @staticmethod
    def get():
        """Conhece get."""
        
        initial_setup()
        return "Conhece"
