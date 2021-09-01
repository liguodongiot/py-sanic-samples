from sanic import Blueprint
from sanic.response import json, text, HTTPResponse
from sanic_openapi import doc

authors = Blueprint("content_authors", url_prefix="/authors")

@authors.middleware
async def print_on_request(request):
    print("该蓝图的中间件仅用于authors")

@authors.middleware("request")
async def halt_request(request):
    print("-----authors request----")
    return text("I halted the request")

@authors.middleware("response")
async def halt_response(request, response):
    print("-----authors response----")
    return text("I halted the response")

# http://127.0.0.1:8000/api/content/authors
@authors.route("/bp")
@doc.summary("获取学生信息")
@doc.tag("学生")
async def bp1_route(request):
    print("蓝图测试：authors")
    return text("bp1")

