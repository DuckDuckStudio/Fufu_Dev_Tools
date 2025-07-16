[Setup]
AppName=芙芙工具箱开发工具包
AppVersion=develop
VersionInfoVersion=develop
AppPublisher=DuckStudio
VersionInfoCopyright=Copyright (c) 鸭鸭「カモ」
AppPublisherURL=https://duckduckstudio.github.io/yazicbs.github.io/
DefaultDirName={autopf}\Fufu_Dev_Tools
DefaultGroupName=芙芙工具箱开发工具包
OutputDir=Release
OutputBaseFilename=Fufu_Dev_Tools_Setup_develop
SetupIconFile=Fufu_Tools\Installer\Fufu_Tools_Setup_ico.ico
LicenseFile=LICENSE-GBK
Compression=lzma2
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64compatible

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "chinesesimplified"; MessagesFile: "compiler:Languages\ChineseSimplified.isl"
Name: "japanese"; MessagesFile: "compiler:Languages\Japanese.isl"

[Files]
Source: "src-pack\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\芙芙工具箱开发工具包"; Filename: "{app}\Script\ffdev.exe"

[Run]
Filename: "{sys}\cmd.exe"; Parameters: "/C setx PATH ""{app}\Script;%PATH%"" /M"; Flags: runhidden

[UninstallRun]
Filename: "{sys}\cmd.exe"; Parameters: "/C setx PATH ""%PATH:{app}\Script;=%"" /M"; Flags: runhidden; RunOnceId: UninstallSetPath
