import os
import sys
import subprocess
from colorama import init, Fore
init(autoreset=True)

version = "develop"

def main():
    try:
        if len(sys.argv) < 2:
            print("Usage: ffdev <工具> <命令> [<参数>...]")
            return 2

        program = sys.argv[1]
        args = sys.argv[2:]

        parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))

        scripts = {
            "参数查重": "代码校对/参数查重.exe",
            "非UTF-8编码": "代码校对/非UTF-8编码.exe",
            "尾随空格": "代码校对/尾随空格.exe",
            "末尾空行": "代码校对/末尾空行.exe",
            "需求生成": "生成工具/需求生成.exe",
            "代码行数": "统计/代码总行数.exe",
            "账号切换": "git/账号切换.exe",
            "连续push": "git/连续push尝试.exe",
            "连续pull": "git/连续pull尝试.exe",
            "git连续尝试": "git/git连续尝试.exe",
            "目录复制": "目录复制.exe"
        }

        if program in ["ver", "版本", "version", "Version", "--version", "--ver", "-v"]:
            print(f"{Fore.GREEN}✓{Fore.RESET} 版本: {version}")
            print(f"{Fore.GREEN}✓{Fore.RESET} 安装在: {parent_dir}")
            return 0

        if program not in scripts:
            print(f"{Fore.YELLOW}⚠{Fore.RESET} 无效的程序调用")
            print(f"{Fore.BLUE}[!]{Fore.RESET} 可用程序: [目录复制] [参数查重] [非UTF-8编码] [尾随空格] [需求生成] [代码行数] [账号切换] [连续push] [连续pull] [git连续尝试]")
            return 2

        program_path = os.path.normpath(os.path.join(parent_dir, scripts[program]))

        if not os.path.isfile(program_path):
            print(f"{Fore.RED}✕{Fore.RESET} 缺少工具 {Fore.BLUE}{program_path}{Fore.RESET} !\n{Fore.YELLOW}⚠{Fore.RESET} 尝试重新安装程序以解决该问题")
            return 1

        result = subprocess.run([program_path] + args)
        return result.returncode
    except KeyboardInterrupt:
        return 2

if __name__ == "__main__":
    sys.exit(main())
