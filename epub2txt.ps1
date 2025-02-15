# 激活虚拟环境
.\venv\Scripts\Activate.ps1

# 创建输出目录（如果不存在）
if (!(Test-Path "txt_book")) {
    New-Item -ItemType Directory -Path "txt_book"
}

# 运行转换程序
python src\epub2txt.py

# 完成后保持窗口打开
Write-Host "`n转换完成！按任意键退出..." -ForegroundColor Green
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

# 退出虚拟环境
deactivate 