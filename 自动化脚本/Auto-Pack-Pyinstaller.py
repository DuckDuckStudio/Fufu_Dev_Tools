import os
import sys
import subprocess

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

print(f"[!] 将使用 Pyinstaller 打包。")

# UPX flag = 1
# 如在本地测试请移除 --upx-dir "upx-latest"
# 在代码中是 --upx-dir \"upx-latest\"

# 计数
fail = 0 # 失败的文件个数
countd = 0 # 已删除的文件个数
acount = 0 # 总文件个数
fcount = 0 # 已打包的文件个数
pyw_acount = 0
py_acount = 0

# 文件夹路径
folder_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))), "src-pack")

if folder_path.startswith(("'", '"')) and folder_path.endswith(("'", '"')):
    folder_path = folder_path[1:-1]

if not folder_path.endswith('\\'):
    folder_path += '\\'

if not os.path.exists(folder_path):
    print(f"[TEST] {folder_path}")
    print(f"[ERROR] 指定的目录路径不存在")
    exit(1)

icon_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))), "Fufu_Tools", "src", "ico.ico")
log_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))))

if icon_path.startswith(("'", '"')) and icon_path.endswith(("'", '"')):
    icon_path = icon_path[1:-1]

if not log_path.endswith('\\'):
    log_path += '\\'

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            print(f'[COUNT INFO] 找到 py 文件: {file_path}')
            py_acount = py_acount + 1
        elif file.endswith('.pyw'):
            file_path = os.path.join(root, file)
            print(f'[COUNT INFO] 找到 pyw 文件: {file_path}')
            pyw_acount = pyw_acount + 1
        
acount = py_acount + pyw_acount
print(f"[COUNT INFO] 一共找到了{acount}个py/pyw文件。\n其中有{py_acount}个py文件/{pyw_acount}个pyw文件。")

# 函数：记录日志并添加分隔线
def log_message(message, log_file):
    # 日志中不应存在颜色
    message = f"{message}"
    log_file.write(message + "\n")
    log_file.write("-" * 50 + "\n") # 添加分隔线

# 函数：打包 Python 文件
def package_py(file_path, file_name, log_file="None"):
    global fcount
    global fail
    try:
        if log_file != "None":
            log_message(f"\n开始打包：{file_path}", log_file)
        print(f"\n[PACK INFO] 开始打包：{file_path}")
        output_dir = os.path.dirname(file_path) # 设置输出目录为 Python 文件所在目录
        if file_name in ["连续push尝试.py", "连续pull尝试.py", "git连续尝试.py"]:
            print(f"[WARNING] 使用notification！")
            if icon_path == "None":
                command = f"pyinstaller --upx-dir \"upx-latest\" --hidden-import plyer.platforms.win.notification --onefile --distpath={output_dir} {file_path}"
            else:
                command = f"pyinstaller --upx-dir \"upx-latest\" --hidden-import plyer.platforms.win.notification --onefile -i \"{icon_path}\" --distpath={output_dir} {file_path}"
        else:
            if icon_path == "None":
                command = f"pyinstaller --upx-dir \"upx-latest\" --onefile --distpath=\"{output_dir}\" \"{file_path}\""
            else:
                command = f"pyinstaller --upx-dir \"upx-latest\" --onefile -i \"{icon_path}\" --distpath=\"{output_dir}\" \"{file_path}\""
        subprocess.run(command, shell=True, check=True)
        if log_file != "None":
            log_message(f"打包完成: {file_path}", log_file)
        print(f"[PACK INFO] 打包完成: {file_path}")
        fcount += 1
        print(f"[PACK INFO] 还剩 {acount-fcount} 个文件待打包。")
    except subprocess.CalledProcessError as e:
        if log_file != "None":
            log_message(f"打包 {file_path} 时出错:\n{e}", log_file)
        print(f"[ERROR] 打包 {file_path} 时出错:\n{e}")
        fail += 1
        fcount += 1
        print(f"[PACK INFO] 还剩 {acount-fcount} 个文件待打包。")
        sys.exit(1)
        return file_path

# 函数：打包 Pythonw 文件
def package_pyw(file_path, file_name, log_file="None"):
    global fcount
    global fail
    try:
        if log_file != "None":
            log_message(f"\n开始打包: {file_path}", log_file)
        print(f"\n[PACK INFO] 开始打包: {file_path}")
        output_dir = os.path.dirname(file_path) # 设置输出目录为 Pythonw 文件所在目录
        if file_name in ["目录复制.pyw"]:
            print(f"[WARNING] 使用notification！")
            if icon_path == "None":
                command = f"pyinstaller --upx-dir \"upx-latest\" --hidden-import plyer.platforms.win.notification --noconsole --onefile --distpath={output_dir} {file_path}"
            else:
                command = f"pyinstaller --upx-dir \"upx-latest\" --hidden-import plyer.platforms.win.notification --noconsole --onefile -i \"{icon_path}\" --distpath={output_dir} {file_path}"
        else:
            if icon_path == "None":
                command = f"pyinstaller --upx-dir \"upx-latest\" --onefile --noconsole --distpath={output_dir} {file_path}"
            else:
                command = f"pyinstaller --upx-dir \"upx-latest\" --onefile --noconsole -i \"{icon_path}\" --distpath={output_dir} {file_path}"
        subprocess.run(command, shell=True, check=True)
        if log_file != "None":
            log_message(f"打包完成：{file_path}", log_file)
        print(f"[PACK INFO] 打包完成：{file_path}")
        fcount += 1
        print(f"[PACK INFO] 还剩 {acount-fcount} 个文件待打包。")
    except subprocess.CalledProcessError as e:
        if log_file != "None":
            log_message(f"打包 {file_path} 时出错:\n{e}", log_file)
        print(f"[ERROR] 打包 {file_path} 时出错:\n{e}")
        fail += 1
        fcount += 1
        print(f"[PACK INFO] 还剩 {acount-fcount} 个文件待打包。")
        sys.exit(1)
        return file_path

if log_path == "None":
    failed_files = [] # 存储打包失败的文件名

    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # 根据文件后缀选择打包方式
            if file.endswith(".py"):
                failed_file = package_py(file_path, file)
                if failed_file:
                    failed_files.append(failed_file)
            elif file.endswith(".pyw"):
                failed_file = package_pyw(file_path, file)
                if failed_file:
                    failed_files.append(failed_file)
else:
    with open(f"{log_path}packaging_log.log", "a", encoding='utf-8') as log_file:
        # 打开日志文件，准备记录日志
        log_message(f"开始打包，需要打包的文件数量：{acount}", log_file)

        failed_files = [] # 存储打包失败的文件名

        # 遍历文件夹中的所有文件
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # 根据文件后缀选择打包方式
                if file.endswith(".py"):
                    failed_file = package_py(file_path, file, log_file)
                    if failed_file:
                      failed_files.append(failed_file)
                    log_message(f"剩余待打包文件数量：{acount-fcount}", log_file)
                elif file.endswith(".pyw"):
                    failed_file = package_pyw(file_path, file, log_file)
                    if failed_file:
                        failed_files.append(failed_file)
                    log_message(f"剩余待打包文件数量：{acount-fcount}", log_file)

# 删除指定格式的文件
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.py') or file.endswith('.pyw'):
            file_path = os.path.join(root, file)
            countd = countd + 1
            os.remove(file_path)
            print(f'[DEL INFO] 已删除源文件: {file_path} (还剩{acount-countd}个源文件)')

print(f"[INFO] 文件删除完成！总共删除了{countd}个原文件")
