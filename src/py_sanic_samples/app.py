from sanic import Sanic
from py_sanic_samples.api import api

app = Sanic(__name__)
# 所有的蓝图都会被注册。
app.blueprint(api)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)