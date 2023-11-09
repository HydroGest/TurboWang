
# TurboWang

在线运行使用 Turbowarp 编译的小码王社区作作品。支持无视克隆体限制，高清画笔。

## 部署

### 环境准备

在开始之前，请确保您已经安装Python3.7及以上、NodeJS18.18.0及以上和对应的npm。

构建Python3虚拟环境：

```
# Linux & MacOS
python3 -m venv .venv
. .venv/bin/activate #每次启动前运行此命令

# Windows
py -3 -m venv .venv
.venv\Scripts\activate #每次启动前运行此命令

```

安装依赖库

```
pip install flask
pip install requests
pip install Beautifulsoup4
```
安装NodeJS依赖
```
npm install
```

### 启动

```
flask run --port=25433 --host=0.0.0.0
```
其中`port`参数是开放的端口号，你现在可以在浏览器启动`http://localhost:25433`来访问TurboWang。




