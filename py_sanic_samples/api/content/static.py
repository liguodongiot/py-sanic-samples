from sanic import Blueprint
from sanic.response import json, text, HTTPResponse


static = Blueprint("content_static", url_prefix="/static")
 

# http://127.0.0.1:8000/api/content/static/xxx
@static.route("/<param>")
async def bp2_route(request, param):
    print("蓝图测试：static")
    return text(param)





 