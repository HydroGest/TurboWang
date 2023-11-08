> 本人在将此项目上传至Github之前误删了一个关键文件，此文件关于Turbowarp编译，此操作不可逆。本人或将于寒假重新对此致命错误进行修复。

# TurboWang

在线运行使用 Turbowarp 编译的小码王社区作作品。支持无视克隆体限制，高清画笔。

## 部署

### 环境准备

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

### 启动

```
flask run --port=25433 --host=0.0.0.0
```
其中`port`参数是开放的端口号，你现在可以在浏览器启动`http://localhost:25433`来访问TurboWang。




