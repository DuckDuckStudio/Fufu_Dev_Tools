[Setup]
AppName=芙芙工具箱开发工具包
AppVersion=2024.06.30.1356
VersionInfoVersion=2024.06.30.1356
AppPublisher=DuckStudio
VersionInfoCopyright=Copyright (c) 鸭鸭「カモ」
AppPublisherURL=https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/wiki/Dev/
DefaultDirName={autopf}\Fufu_Dev_Tools
DefaultGroupName=芙芙工具箱开发工具包
UninstallDisplayIcon={app}\Script\ffdev.exe
OutputDir=D:\Duckhome\projects\MSVS\Source\Repos\Fufu_Dev_Tools\开发工具-winget\version\安装包\
OutputBaseFilename=Fufu_Dev_Tools_Setup_2024.06.30.1356
SetupIconFile=D:\Duckhome\projects\MSVS\Source\Repos\Fufu_Tools\ico.ico
LicenseFile=D:\Duckhome\projects\MSVS\Source\Repos\Fufu_Dev_Tools\开发工具-winget\LICENSE
Compression=lzma2
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "chinesesimplified"; MessagesFile: "compiler:Languages\ChineseSimplified.isl"
Name: "japanese"; MessagesFile: "compiler:Languages\Japanese.isl"

[Files]
Source: "D:\Duckhome\projects\MSVS\Source\Repos\Fufu_Dev_Tools\开发工具-winget\version\2024.06.30.1356\*"; DestDir: "{app}"
Source: "D:\Duckhome\projects\MSVS\Source\Repos\Fufu_Dev_Tools\开发工具-winget\version\2024.06.30.1356\git\*"; DestDir: "{app}\git"
Source: "D:\Duckhome\projects\MSVS\Source\Repos\Fufu_Dev_Tools\开发工具-winget\version\2024.06.30.1356\Script\*"; DestDir: "{app}\Script"
Source: "D:\Duckhome\projects\MSVS\Source\Repos\Fufu_Dev_Tools\开发工具-winget\version\2024.06.30.1356\代码校对\*"; DestDir: "{app}\代码校对"
Source: "D:\Duckhome\projects\MSVS\Source\Repos\Fufu_Dev_Tools\开发工具-winget\version\2024.06.30.1356\生成工具\*"; DestDir: "{app}\生成工具"
Source: "D:\Duckhome\projects\MSVS\Source\Repos\Fufu_Dev_Tools\开发工具-winget\version\2024.06.30.1356\统计\*"; DestDir: "{app}\统计"

[Icons]
Name: "{group}\芙芙工具箱开发工具包"; Filename: "{app}\Script\ffdev.exe"

[Run]
Filename: "{sys}\cmd.exe"; Parameters: "/C setx PATH ""{app}\Script;%PATH%"" /M"; Flags: runhidden

[UninstallRun]
Filename: "{sys}\cmd.exe"; Parameters: "/C setx PATH ""%PATH:{app}\Script;=%"" /M"; Flags: runhidden; RunOnceId: UninstallSetPath
