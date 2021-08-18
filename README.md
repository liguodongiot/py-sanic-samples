# py-sanic-samples


## poetry-包管理


```
# 使用在线脚本进行安装，是最为推荐的安装方式
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

source $HOME/.poetry/env




```

### 创建项目

```
# 已有项目-初始化

poetry init

创建一个 pyproject.toml 文件

# 新项目
poetry new demo-priject


如果要把项目代码放入到 src 目录下，在创建项目时，可以加上 --src 参数。

poetry new demo-priject --src 

使用 poetry install 命令创建虚拟环境（确保当前目录有 pyproject.toml 文件）：


poetry install

这个命令会读取 pyproject.toml 中的所有依赖（包括开发依赖）并安装，如果不想安装开发依赖，可以附加 --no-dev 选项。
如果项目根目录有 poetry.lock 文件，会安装这个文件中列出的锁定版本的依赖。
如果执行 add/remove 命令的时候没有检测到虚拟环境，也会为当前目录自动创建虚拟环境。


```


### 使用虚拟环境

```
使用虚拟环境创建虚拟环境后，如果想要在虚拟环境下执行命令，比如去执行脚本，去使用 pip list 等等。
可以在项目目录下，使用如下命令$ poetry run <commands>

比如我查看该虚拟环境中安装了哪些包

$ poetry run pip list

再比如我想在该虚拟环境下执行 app.py$ poetry run python app.py每次在虚拟环境下做点啥事，命令前面都要加上 poetry run，有点太麻烦了。这时可以使用下面这条命令，直接激活当前的虚拟环境$ poetry shell



```