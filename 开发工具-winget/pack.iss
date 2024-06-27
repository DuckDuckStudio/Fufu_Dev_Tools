[Setup]
AppName=芙芙工具箱开发工具包
AppVersion=202406242036
VersionInfoVersion=202406242036
AppPublisher=DuckStudio
VersionInfoCopyright=Copyright (c) 鸭鸭「カモ」
AppPublisherURL=https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/wiki/Dev/
DefaultDirName={autopf}\Fufu_Dev_Tools
DefaultGroupName=芙芙工具箱开发工具包
UninstallDisplayIcon={app}\Script\ffdev.exe
OutputDir=D:\Duckhome\projects\MSVS\Source\Repos\Fufu_Dev_Tools\开发工具-winget\version\
OutputBaseFilename=Fufu_Dev_Tools_Setup_202406242036
SetupIconFile=D:\Duckhome\projects\MSVS\Source\Repos\Fufu_Tools\ico.ico
LicenseFile=D:\Duckhome\projects\MSVS\Source\Repos\Fufu_Dev_Tools\开发工具-winget\LICENSE
Compression=lzma2
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "chinesesimplified"; MessagesFile: "compiler:Languages\ChineseSimplified.isl"
Name: "japanese"; MessagesFile: "compiler:Languages\Japanese.isl"

[Files]
Source: "D:\Duckhome\projects\MSVS\Source\Repos\Fufu_Dev_Tools\开发工具-winget\version\202406242036\*"; DestDir: "{app}"

[Icons]
Name: "{group}\芙芙工具箱开发工具包"; Filename: "{app}\Script\ffdev.exe"

[Run]
Filename: "{sys}\cmd.exe"; Parameters: "/C setx PATH ""{app}\Script;%PATH%"" /M"; Flags: runhidden

[UninstallRun]
Filename: "{sys}\cmd.exe"; Parameters: "/C setx PATH ""%PATH:{app}\Script;=%"" /M"; Flags: runhidden
