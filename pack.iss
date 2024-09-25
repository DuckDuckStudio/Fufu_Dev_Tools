[Setup]
AppName=芙芙工具箱开发工具包
AppVersion=2024.09.08.2000
VersionInfoVersion=2024.09.08.2000
AppPublisher=DuckStudio
VersionInfoCopyright=Copyright (c) 鸭鸭「カモ」
AppPublisherURL=https://duckduckstudio.github.io/yazicbs.github.io/
DefaultDirName={autopf}\Fufu_Dev_Tools
DefaultGroupName=芙芙工具箱开发工具包
UninstallDisplayIcon={app}\Script\ffdev.exe
OutputDir=构建文件
OutputBaseFilename=Fufu_Dev_Tools_Setup_2024.09.08.2000
SetupIconFile=Fufu_Tools\ico.ico
LicenseFile=LICENSE-GBK
Compression=lzma2
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "chinesesimplified"; MessagesFile: "compiler:Languages\ChineseSimplified.isl"
Name: "japanese"; MessagesFile: "compiler:Languages\Japanese.isl"

[Files]
Source: "开发工具-打包-done\*"; DestDir: "{app}"
Source: "开发工具-打包-done\git\*"; DestDir: "{app}\git"
Source: "开发工具-打包-done\Script\*"; DestDir: "{app}\Script"
Source: "开发工具-打包-done\代码校对\*"; DestDir: "{app}\代码校对"
Source: "开发工具-打包-done\生成工具\*"; DestDir: "{app}\生成工具"
Source: "开发工具-打包-done\统计\*"; DestDir: "{app}\统计"

[Icons]
Name: "{group}\芙芙工具箱开发工具包"; Filename: "{app}\Script\ffdev.exe"

[Run]
Filename: "{sys}\cmd.exe"; Parameters: "/C setx PATH ""{app}\Script;%PATH%"" /M"; Flags: runhidden

[UninstallRun]
Filename: "{sys}\cmd.exe"; Parameters: "/C setx PATH ""%PATH:{app}\Script;=%"" /M"; Flags: runhidden; RunOnceId: UninstallSetPath
