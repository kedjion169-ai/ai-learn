import requests

response = requests.get("https://www.baidu.com")

print(f"请求状态码: {response.status_code}")

if response.status_code == 200:
    print("🎉 恭喜！API调用测试成功！")
else:
    print("❌ 调用失败，请检查网络连接")
    