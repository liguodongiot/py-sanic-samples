from sanic import Sanic
from py_sanic_samples.api import api
from sanic.exceptions import NotFound
from sanic.response import json, text, HTTPResponse

app = Sanic(__name__)
# 所有的蓝图都会被注册。
app.blueprint(api)

# 异常处理
@app.exception(NotFound)
def ignore_404s(request, exception):
    return text("Yep, I totally found the page: {}".format(request.url))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)