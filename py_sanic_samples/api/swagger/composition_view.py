from sanic.response import text
from sanic.views import CompositionView
from sanic import Blueprint


composition_bp = Blueprint("组合视图", url_prefix="/composition_view")


def get_handler(request):
    return text("I am a get method")


view = CompositionView()
view.add(["GET"], get_handler)
view.add(["POST", "PUT"], lambda request: text("I am a post/put method"))

composition_bp.add_route(view, "/")

