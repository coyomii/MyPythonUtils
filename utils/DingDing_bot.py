import requests
import hmac
import hashlib
import time
import base64

def create_sign(secret, timestamp):
    """生成签名"""
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = base64.b64encode(hmac_code).decode('utf-8')
    return sign

def send_dingtalk_message_with_sec(webhook_url, secret, message):
    timestamp = str(round(time.time() * 1000))
    sign = create_sign(secret, timestamp)
    
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",
        "text": {
            "content": message
        },
        "timestamp": timestamp,
        "sign": sign
    }
    
    url_with_sec = f"{webhook_url}&timestamp={timestamp}&sign={sign}"
    response = requests.post(url_with_sec, json=data, headers=headers)
    
    if response.status_code == 200:
        print("消息发送成功")
    else:
        print(f"消息发送失败，错误码：{response.status_code}")

# 替换为你的Webhook地址（不包含后面的查询字符串）
webhook_base_url = "your_webhook_base_url"
secret = "your_secret_key"  # 这里填入你在钉钉机器人设置中配置的密钥
message_content = "Hello, 钉钉群！这是一条启用安全设置后的测试消息。"


# if __name__ == '__main__':
#     send_dingtalk_message_with_sec(webhook_base_url, secret, message_content)

