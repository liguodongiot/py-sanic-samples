from sanic import Blueprint
from .content import content
from .info import info
from .swagger import swagger

api = Blueprint.group(content, info, swagger, url_prefix="/api")

