from sanic import Blueprint
from .static import static
from .authors import authors

# 蓝图组(Blueprint group)
content = Blueprint.group(static, authors, url_prefix="/content")
 

@content.middleware("request")
async def group_middleware(request):
    print("使用蓝图组能够将中间件应用给同组中的所用蓝图（static和authors）。")


