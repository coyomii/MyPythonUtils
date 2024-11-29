import json

import requests

# 详细使用可以参考下列两个网站
# 网站1-https://v1.jinrishici.com/
# 网站2-https://developer.hitokoto.cn/sentence/

# 目前在用
def fetch_daily_sentence():
    url = 'https://v1.jinrishici.com/all.json' 
    # url = 'https://v1.hitokoto.cn/?c=i' 
    try:
        response = requests.get(url)
        data = response.json()
        return f"「{data['content']}」 —— {data['author']}"
    except requests.exceptions.RequestException:
        # 如果请求失败，返回固定的诗词
        return "「月落乌啼霜满天，江枫渔火对愁眠」"
    
# 不同实现手段
def sentence1():
    url = 'https://v1.jinrishici.com/all.json'
    # url = 'https://v1.hitokoto.cn/?c=i'
    r = requests.get(url)
    return r.text

def sentence():
    url = 'https://v1.jinrishici.com/all.json'
    r = requests.get(url)
    data = json.loads(r.text)  # 解析返回的 JSON 数据
    content = data["content"]
    author = data["author"]

    return f"「{content}」 —— {author}"

if __name__ ==  "__main__":
    sici = sentence()
    print(sici)