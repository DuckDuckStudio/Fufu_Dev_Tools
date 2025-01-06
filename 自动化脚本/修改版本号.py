import os
import sys

# GitHub Action - Windows 竟然只能输出英文 :(

if len(sys.argv) != 2:
    print("[ERROR] Usage: python xxx.py <New-version>")
    sys.exit(1)

新版本号 = sys.argv[1]
if not 新版本号:
    print("[ERROR] Version cannot be empty")
    sys.exit(1)
print(f"[INFO] New version: {新版本号}")

文件 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))), "开发工具-打包", "Script", "ffdev.py")
try:
    # 读取文件内容
    with open(文件, 'r', encoding='utf-8') as f:
        内容 = f.read()

    # 替换文本
    内容 = 内容.replace('version = "develop"', f'version = "{新版本号}"')

    # 写回文件
    with open(文件, 'w', encoding='utf-8') as f:
        f.write(内容)
except Exception as e:
    print(f"[ERROR] A error occurred when processing {文件}: {e}")
    sys.exit(1)

文件 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))), "开发工具-源码", "Script", "ffdev.ps1")
try:
    # 读取文件内容
    with open(文件, 'r', encoding='utf-8') as f:
        内容 = f.read()

    # 替换文本
    内容 = 内容.replace('$version = "develop"', f'$version = "{新版本号}"')

    # 写回文件
    with open(文件, 'w', encoding='utf-8') as f:
        f.write(内容)
except Exception as e:
    print(f"[ERROR] A error occurred when processing {文件}: {e}")
    sys.exit(1)

文件 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))), "pack.iss")
try:
    # 读取文件内容
    with open(文件, 'r', encoding='utf-8') as f:
        内容 = f.read()

    # 替换文本
    内容 = 内容.replace('develop', 新版本号)

    # 写回文件
    with open(文件, 'w', encoding='utf-8') as f:
        f.write(内容)
except Exception as e:
    print(f"[ERROR] A error occurred when processing {文件}: {e}")
    sys.exit(1)

# 请勿使用表情，GitHub Action 会有意见的 :(
print("[INFO] Version number processing is complete for all files!")
sys.exit(0)
