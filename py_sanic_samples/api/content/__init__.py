from sanic import Blueprint
from .note import note
from .authors import authors
from .books import books

# 蓝图组(Blueprint group)
content = Blueprint.group(authors, books, note, url_prefix="/content")
 

@content.middleware("request")
async def group_middleware(request):
    print("使用蓝图组能够将中间件应用给同组中的所用蓝图（static和authors）。")


