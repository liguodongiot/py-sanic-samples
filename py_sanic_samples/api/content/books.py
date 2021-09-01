from sanic import Blueprint
from sanic.response import json, text, HTTPResponse

books = Blueprint("content_books", url_prefix="/books")


# http://127.0.0.1:8000/api/content/authors
@books.route("/bp101")
async def bp1_route(request):
    print("蓝图测试：authors")
    return text("bp101")

