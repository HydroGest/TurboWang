import os,json,time,re
import project,getassets,projectInfo
import shutil
 
def getProjectData(url):
    if 'http' not in url:
        url='http://world.xiaomawang.com/community/main/compose/'+url
    pdata=projectInfo.getProps(url)
    return pdata
    
def gethtml(project):
    command='node index.js %s'%project
    #print(command)
    with os.popen(command) as nodejs:
        result= nodejs.read().replace('\n', '')
    return result

def getAssets(str1,path):
    li = re.findall('"md5ext":(.*?),"', str1)
    #print(li)
    li=list(set(li))
    for i in li:
        i=i.replace('"','')
        i=i.replace('}','')
        i=i.replace(']','')
        i=i[:36]
        #print('Downloading assests %s (%s/%s)'%( i,li.index(i),len(li) ))
        files=getassets.download(i)
        with open(path+'/'+i,"wb") as file:
            file.write(files)

def createProject(url):
    if 'http' not in url:
        url='http://world.xiaomawang.com/community/main/compose/'+url
    projectObj=project.getProjectJson(url)
    path='tmp/'+projectObj['name']
    try:
        if os.path.exists(path):
            f = open('./statics/'+path+'/output.html',encoding = "utf-8")
            html=f.read()
            f.close()
            html=html.replace('\n','')
            return '/tmp/'+projectObj['name']+'/output.html'
    except:
        pass
    try:
        os.mkdir(path)
    except Exception as e:
        print(e)
    with open(path+'/project.json',"w") as file:
        file.write(projectObj['data'])
    getAssets(projectObj['data'],'./'+path)
    makeProject(path)
    gethtml('./statics/'+path)
    f = open('./statics/'+path+'/output.html',encoding = "utf-8")
    html=f.read()
    f.close()
    html=html.replace('\n','')
    return '/tmp/'+projectObj['name']+'/output.html'
    
def makeProject(path):
    shutil.make_archive('./statics/'+path+'/project.sb3', 'zip', path)
if __name__ == '__main__':
    createProject(input('>'))
    