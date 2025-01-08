import os
import sys

if len(sys.argv) != 2:
    print("[ERROR] 使用示例: python xxx.py <新版本号>")
    sys.exit(1)

新版本号 = sys.argv[1]
if not 新版本号:
    print("[ERROR] 新版本号不能为空")
    sys.exit(1)
print(f"[INFO] 新版本号: {新版本号}")

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
    print(f"[ERROR] 处理 {文件} 时出错: {e}")
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
    print(f"[ERROR] 处理 {文件} 时出错: {e}")
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
    print(f"[ERROR] 处理 {文件} 时出错: {e}")
    sys.exit(1)

print("[INFO] 🎉 成功处理所有文件")
sys.exit(0)
