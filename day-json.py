import json

# 模拟AI返回的内容
ai_response = {
    "role": "温柔御姐",
    "voice": "女",
    "text": "早安呀，今天也要加油哦\~",
    "speed": 1.0,
    "emotion": "happy"
}

# 转成JSON并打印
print("AI返回的JSON数据：")
print(json.dumps(ai_response, ensure_ascii=False, indent=4))