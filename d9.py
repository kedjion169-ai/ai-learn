# Day9：用Python写入文本文件
with open("audio.txt", "w", encoding="utf-8") as f:
    f.write("语音内容：你好，我正在学习Python文件操作！")

print("✅ 文本已经成功写入 audio.txt 文件啦！")