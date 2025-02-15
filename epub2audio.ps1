# 激活虚拟环境
.\venv\Scripts\Activate.ps1

# 创建输出目录（如果不存在）
if (!(Test-Path ".\audio_book")) {
    New-Item -ItemType Directory -Path ".\audio_book"
}

# 运行转换程序
python .\src\epub2audio.py --input_dir ".\epub" --output_dir ".\audio_book" --voice zh-CN-YunxiNeural

# 完成后保持窗口打开
Write-Host "`n转换完成！按任意键退出..." -ForegroundColor Green
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

# 退出虚拟环境
deactivate 