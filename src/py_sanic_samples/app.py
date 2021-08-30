from sanic import Sanic
from py_sanic_samples.api import api
from py_sanic_samples.config.log import LOGGING_CONFIG
from sanic.exceptions import NotFound
from sanic.response import json, text, HTTPResponse
import logging.config
import logging

# 自定义日志使用python自带的logging打印
# 默认的使用sanic日志打印

# logging.config.dictConfig(LOGGING_CONFIG)
# logger = logging.getLogger('root')
# logger.info("---------")

# app = Sanic(__name__, log_config=LOGGING_CONFIG)
app = Sanic(__name__)

# logging.info("---------")

# 所有的蓝图都会被注册。
app.blueprint(api)

# Sanic 的默认日志配置
# sanic.log.LOGGING_CONFIG_DEFAULTS

# Sanic 默认的访问日志格式
# %(asctime)s - (%(name)s)[%(levelname)s][%(host)s]: %(request)s %(message)s %(status)d %(byte)d

# 异常处理
@app.exception(NotFound)
def ignore_404s(request, exception):
    return text("Yep, I totally found the page: {}".format(request.url))

if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=8000, debug=True, access_log=False)
    app.run(host="127.0.0.1", port=8000)

