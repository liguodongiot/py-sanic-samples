from sanic import Blueprint
from sanic.response import json, text, HTTPResponse


statics = Blueprint("content_statics", url_prefix="/statics")


# http://127.0.0.1:8000/api/content/statics/bp2/xxx
@statics.route("/bp2/<param>")
async def bp2_route(request, param):
    print("蓝图测试：static")
    return text(param)


@statics.route("/bp3")
async def bp3_route(request):
    print("蓝图测试：authors")
    return text("bp1")



 