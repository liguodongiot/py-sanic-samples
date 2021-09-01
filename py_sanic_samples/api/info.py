from sanic import Blueprint
from sanic.log import logger
from sanic.response import json, text, HTTPResponse
import logging

info = Blueprint("info", url_prefix="/info")


# http://127.0.0.1:8000/api/info/user
@info.route("/user/<param>")
async def user_route(request, param):
    logger.info("蓝图测试：user")
    # logging.info("----xxxxx-----")
    return text(param)

