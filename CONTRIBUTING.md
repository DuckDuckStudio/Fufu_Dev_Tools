# 芙芙工具箱贡献文档

在贡献前请先阅读[LICENSE许可文件](https://github.com/DuckDuckStudio/Fufu_Tools/blob/main/LICENSE)。  

## 提交建议 / 直接修改
您可以通过在仓库的[Issues](https://github.com/DuckDuckStudio/yazicbs.github.io/issues)界面提交您的建议，您也可以Fork本仓库后直接修改并提交 PR。  
请确保您的修改没有与其他PR重复或者无效后再提交PR。  

## 关于打包
### [Fufu_Dev_Tools](https://github.com/DuckDuckStudio/Fufu_Dev_Tools) 仓库
1. 手动克隆仓库到本地  
   ```powershell
   git clone https://github.com/DuckDuckStudio/Fufu_Dev_Tools.git
   ```
2. 下载芙芙工具箱的[发行版](https://github.com/DuckDuckStudio/Fufu_Tools/releases)或克隆最新[仓库](https://github.com/DuckDuckStudio/Fufu_Tools)  
   ```powershell
   winget install DuckStudio.FufuTools #发行版
   git clone https://github.com/DuckDuckStudio/Fufu_Tools.git #仓库
   ```
3. 构建虚拟环境
   ```powershell
   python -m venv .venv
   & ".venv\Scripts\Activate.ps1"
   ```
4. 运行芙芙工具箱的自动打包工具(`Tools\【实验性工具】\自动化\自动打包所有py文件\使用Pyinstaller.py`)  
5. 输入相关参数
<!--等待补充-->

## 关于翻译
你可以对本项目进行翻译，请将翻译后的文件放在`翻译版`>`{tag}`下。  
如果你没找到`翻译版`文件夹就在根目录自己建一个。  

<div style="text-align: right;">
    <p>鸭鸭「カモ」</p>
    <p>2024年7月31日</p>
    <p>编辑内容：更新打包过程</p>
</div>
