import requests,json,re,os,random
from bs4 import BeautifulSoup

def get_json_info(page_html):
    print(page_html)
    soup=BeautifulSoup(page_html,'html.parser')
    original_json=soup.find_all(id='__NEXT_DATA__')
    print(original_json)
    pattern = re.compile(r'<[^>]+>',re.S)
    result = pattern.sub('', str(original_json[0]))
    return result
    
def get_page(url):
    x=requests.get(url)
    return x.text
    
def get_source(uid,headers={}):
    url='https://community-api.xiaomawang.com/api/v1/comment/get-list?mainId='+uid+'&mainType=4&page=1'
    x = requests.get(url,headers=headers)
    return x.text
    
def download(url):
    
    headers={
        'Host': 'community-wscdn.xmwol.com',
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99","HuaweiBrowser";v="99"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Safari/537.36',
        'sec-ch-ua-platform':'"Windows"',
        'Accept': '*/*',
        'Origin': 'https://world.xiaomawang.com',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://world.xiaomawang.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response=requests.get(url=url,headers=headers)
    return response.text

def getProjectJson(url):
        print('/////'+url)
        data=json.loads(get_json_info(get_page(url)))
        projectobj=data['props']['initialState']['detail']['composeInfo']
        sb3=os.path.basename(projectobj['fileKey'])
        url='https://community-wscdn.xmwol.com/composition/'+sb3+'?key=0acc53e04200657243c48f0d19108cd6&time=1670416906956'
        #print('[i] 文件已标记，开始下载...... '+sb3)
        return {
            'data':download(url),
            'name':sb3
        }