using System;
using System.Collections.Generic;
using System.IO;

namespace FFDev
{
    class Program
    {
        static readonly string version = "2024.08.05.0100";

        static readonly Dictionary<string, string> scripts = new()
        {
            { "总调用", "代码校对/参数查重.exe" },
            { "目录复制", "目录复制.exe" },
            { "参数查重", "代码校对/参数查重.exe" },
            { "非UTF-8编码", "代码校对/非UTF-8编码.exe" },
            { "尾随空格", "代码校对/尾随空格.exe" },
            { "需求生成", "生成工具/需求生成.exe" },
            { "代码行数", "统计/代码总行数.exe" },
            { "账号切换", "git/账号切换.exe" },
            { "连续push", "git/连续push尝试.exe" },
            { "连续pull", "git/连续pull尝试.exe" },
            { "git连续尝试", "git/git连续尝试.exe" }
        };

        static void Main(string[] args)
        {
            if (args.Length < 2)
            {
                Environment.ExitCode = 2;
                Console.WriteLine("Usage: ffdev <工具> <命令> [<参数>...]");
                return;
            }

            string program = args[0];
            string command = args.Length > 1 ? args[1] : "";
            string[] inputArgs = new string[args.Length - 2];
            Array.Copy(args, 2, inputArgs, 0, inputArgs.Length);

            if (IsVersionCommand(program))
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine($"✓ Version {version}");
                Console.ResetColor();
                return;
            }

            if (!scripts.TryGetValue(program, out string? value))
            {
                Environment.ExitCode = 1;
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("✕ 无效的程序调用");
                Console.ResetColor();
                Console.WriteLine("[!] 可用程序: [总调用] [目录复制] [参数查重] [非UTF-8编码] [尾随空格] [需求生成] [代码行数] [账号切换] [连续push] [连续pull] [git连续尝试]");
                return;
            }


            string parentDir = Path.GetDirectoryName(Path.GetDirectoryName(Path.GetFullPath(Environment.GetCommandLineArgs()[0])));
            Console.WriteLine(parentDir);
            string programPath = Path.Combine(parentDir, value);
            Console.WriteLine(programPath);
            Console.ReadKey();

            if (!File.Exists(programPath))
            {
                Environment.ExitCode = 1;
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine($"✕ 缺少工具 {programPath} !");
                Console.ForegroundColor = ConsoleColor.Yellow;
                Console.WriteLine("⚠ 尝试重新安装程序以解决该问题");
                Console.ResetColor();
                return;
            }

            string commandArgs = $"{command} {string.Join(" ", inputArgs)}";
            ExecuteCommand(programPath, commandArgs);
        }

        static bool IsVersionCommand(string program)
        {
            return program.Equals("ver", StringComparison.OrdinalIgnoreCase) ||
                   program.Equals("版本", StringComparison.OrdinalIgnoreCase) ||
                   program.Equals("version", StringComparison.OrdinalIgnoreCase) ||
                   program.Equals("--version", StringComparison.OrdinalIgnoreCase) ||
                   program.Equals("--ver", StringComparison.OrdinalIgnoreCase) ||
                   program.Equals("-v", StringComparison.OrdinalIgnoreCase);
        }

        static void ExecuteCommand(string programPath, string arguments)
        {
            try
            {
                var process = new System.Diagnostics.Process
                {
                    StartInfo = new System.Diagnostics.ProcessStartInfo
                    {
                        FileName = programPath,
                        Arguments = arguments,
                        UseShellExecute = false,
                        RedirectStandardOutput = false,
                        CreateNoWindow = true
                    }
                };
                process.Start();
                process.WaitForExit();
            }
            catch (Exception ex)
            {
                Environment.ExitCode = 1;
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine($"执行命令时出错: {ex.Message}");
                Console.ResetColor();
            }
        }
    }
}
