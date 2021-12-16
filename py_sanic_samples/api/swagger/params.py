from datetime import date
from sanic import Blueprint
from sanic.response import json, text, HTTPResponse
from sanic_openapi import doc
from dataclasses import dataclass,field
from dataclasses_json import dataclass_json

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


class ResponseJson:
    code = doc.Integer(description='响应码')
    message = doc.String(description='响应消息')
    data = doc.JsonBody(description='响应结果')

    def config2dict(class_instance):
        config_dict = {}

        for key in dir(class_instance.__class__):
            value = getattr(class_instance, key)
            if not key.startswith('__') and not callable(value) and not key.startswith('_'):
                config_dict[key] = value
        return config_dict


class DataResponseJson(ResponseJson):
    code = 10000
    message = "ok"

    


@params.get("/deltail_test_json")
@doc.produces(ResponseJson)
async def test_json(request):
    result = {'zzz':'xxx', 'yyy':'xxx', 'zzz':[1,2,3]}
    respon_json = DataResponseJson()
    # respon_json.code=100
    # respon_json.message="dddd"
    respon_json.data= result
    result_dict = DataResponseJson.config2dict(respon_json)
    print(result_dict)
    return json(result_dict)


class Respnse:
    code = doc.Integer(description='响应码')
    message = doc.String(description='响应消息')
    data = doc.JsonBody(description='响应结果')


@dataclass_json
@dataclass(init=True)
class BaseResponseData(Respnse):
    code : int = field(default="10")
    message : str = field(default="ok")
    data : object = field(default=None)

@dataclass_json
@dataclass(init=True)
class ResponseDataClass(BaseResponseData):
    code : int = field(default="100000")
    message : str = field(default="ok2")


@params.get("/deltail_test_dataclass")
@doc.produces(Respnse)
async def test_data_class(request):
    result = {'zzz':'xxx', 'yyy':'xxx', 'zzz':[1,2,3]}
    respon_json = ResponseDataClass(code=100000, message='okok', data = result)
    print(respon_json.to_json())
    return json(respon_json.to_dict())