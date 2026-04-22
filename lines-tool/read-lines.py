import os

# 获取当前脚本所在的目录（不管从哪里运行都能正确找到）
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'lines.txt')

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"❌ 找不到文件：{file_path}")
    print("请确保 lines.txt 和 read-lines.py 在同一个文件夹里。")
    exit()
except Exception as e:
    print(f"读取文件出错：{e}")
    exit()

# 格式化输出
print("★ 今日词句集锦 ★")
print("--" * 30)

for idx, line in enumerate(lines, start=1):
    print(f"{idx}. {line.strip()}")

print("--" * 30)
print(f"共读取 {len(lines)} 句台词")