from flask import Flask
from flask import render_template,url_for,request
import main,os,getassets,projectInfo
import traceback
app = Flask(__name__)
#app.config['STATIC_URL_PATH'] = '/statics'

def getGoodProjects():
    return [
        projectInfo.getProps('https://world.xiaomawang.com/community/main/compose/N0KU666J'),
        projectInfo.getProps('https://world.xiaomawang.com/community/main/compose/ooFj666J'),
        projectInfo.getProps('https://world.xiaomawang.com/community/main/compose/3RYj666J'),
        projectInfo.getProps('http://world.xiaomawang.com/community/main/compose/AJYD666J'),
        projectInfo.getProps('http://world.xiaomawang.com/community/main/compose/PNnk666J'),
        projectInfo.getProps('http://world.xiaomawang.com/community/main/compose/dj4C666J')
    ]

@app.route("/projects/<url>")
def getproject(url):
    try:
        static=main.createProject(url)
        files = os.listdir('./static/tmp/')   # 读入文件夹
        num= len(files)     
        return render_template('project.html', url=static,pdata=main.getProjectData(url),projectNum=num,projects=getGoodProjects())
    except Exception as e:
        return traceback.format_exc()
#
@app.route("/")
def hello_world():
    return "<script>document.location.href ='/projects/N0KU666J'</script>"

@app.route("/getasset")
def getasset():
    url = request.args.get('url', '')
    return getassets.download(url)
