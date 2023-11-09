import requests
def download(file):
    if 'http' not in file:
        url='https://community-wscdn.xmwol.com/picture/'+file
    else:
        url=file
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
    return response.content
