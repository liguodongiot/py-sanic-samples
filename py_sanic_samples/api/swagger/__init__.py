
from .simple_view import bp
from .composition_view import composition_bp
from .params import params
from sanic import Blueprint

swagger = Blueprint.group(bp, composition_bp, params, url_prefix="/swagger")

