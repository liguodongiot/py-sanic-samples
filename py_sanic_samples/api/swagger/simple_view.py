from sanic.views import HTTPMethodView
from sanic.response import text
from sanic import Blueprint


bp = Blueprint("简单视图", url_prefix="/simple_view")


class SimpleView(HTTPMethodView):
    def get(self, request):
        return text("I am get method")

    def post(self, request):
        return text("I am post method")

    def put(self, request):
        return text("I am put method")

    def patch(self, request):
        return text("I am patch method")

    def delete(self, request):
        return text("I am delete method")

    def options(self, request): # This will not be documented.
        return text("I am options method")


bp.add_route(SimpleView.as_view(), "/")

