import requests,re,os,json,time,base64,threading,urllib.parse
from bs4 import BeautifulSoup

def get_json_info(page_html):
    soup=BeautifulSoup(page_html,'html.parser')
    original_json=soup.find_all(id='__NEXT_DATA__')
    #print(original_json[0])
    pattern = re.compile(r'<[^>]+>',re.S)
    result = pattern.sub('', str(original_json[0]))
    return result

def matche(url,headers={},resType="text"):
    x = requests.get(url,headers=headers)
    if resType=="text":
        return x.text
    elif resType=="img":
        return x.content

def getProps(url):
    jsons=json.loads(get_json_info(matche(url)))
    project=jsons['props']['initialState']['detail']['composeInfo']
    return project