from sanic import Blueprint
from sanic.response import json, text, HTTPResponse
from sanic_openapi import doc

params = Blueprint("参数描述说明", url_prefix="/params")


class User:
    name = str


class Test:
    user = doc.Object(User)
    hello = doc.String(description='问候语')

class ResponseTest:
    hello = doc.String(description='打招呼')


@params.post("/test")
# tag会覆盖Blueprint的设置的名字
@doc.tag("测试")
@doc.description('This is a test route with detail description.')
# 请求体
@doc.consumes(Test, location="body")
# 响应体
@doc.produces(ResponseTest)
async def test(request):
    return json({"Hello": "World"})

@params.get("/deltail_test")
@doc.consumes(doc.String(name="X-API-VERSION"), location="header", required=True)
@doc.response(401, {"message": str}, description="Unauthorized")
async def test(request):
    return json({"Hello": "World"})
