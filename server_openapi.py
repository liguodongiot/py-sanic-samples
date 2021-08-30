# from sanic import Sanic
# from sanic.response import json, text, HTTPResponse
# from sanic_openapi import openapi3_blueprint
# from sanic.request import Request
# from uuid import UUID

# app = Sanic(name="AwesomeApi")
# app.blueprint(openapi3_blueprint)


# @app.route("/")
# async def test(request):
#     return json({"hello": "world"})


# @app.get("/foo")
# async def foo_handler(request):
#     return text("I said foo!")


# @app.get("/typed")
# async def typed_handler(request: Request) -> HTTPResponse:
#     return text("Done.")


# async def fetch_user_by_token(token):
#     user = {"name": "liguodong", "age": 18, "token": token}
#     return user

# @app.middleware("request")
# async def run_before_handler(request):
#     print("-----run_before_handler------")
#     request.ctx.user = await fetch_user_by_token(request.token)
#     print(f"{request.ctx.user}")
#     if 'name' in request.ctx.user:
#         print(request.ctx.user['name'])



# @app.route('/hi')
# async def hi_my_name_is(request):
#     print("-----hi_my_name_is------")
#     return text("Hi, my name is {}".format(request.ctx.user['name']))


# @app.on_request
# async def increment_foo(request):
#     if not hasattr(request.conn_info.ctx, "foo"):
#         request.conn_info.ctx.foo = 0
#     request.conn_info.ctx.foo += 1

# @app.get("/count_foo")
# async def count_foo(request):
#     return text(f"request.conn_info.ctx.foo={request.conn_info.ctx.foo}")


# ###################


# class Thing:
#     thing_id = 100

# async def do_create(request):
#     new_thing = Thing
#     return new_thing

# @app.get("/create_new")
# async def create_new(request):
#     new_thing = await do_create(request)
#     return json({"created": True, "id": new_thing.thing_id}, status=201)

# # http://127.0.0.1:8000/tag/xxx
# @app.get("/tag/<tag>")
# async def tag_handler(request, tag):
#     return text("Tag - {}".format(tag))

# # http://127.0.0.1:8000/foo/00010203-0405-0607-0809-0a0b0c0d0e0f
# @app.get("/foo/<foo_id:uuid>")
# async def uuid_handler(request, foo_id: UUID):
#     return text("UUID - {}".format(foo_id))
 

# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=8000)
