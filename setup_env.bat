@echo off
echo 正在创建Python虚拟环境...

:: 创建虚拟环境
python -m venv venv

:: 激活虚拟环境
call venv\Scripts\activate.bat

:: 升级pip
python -m pip install --upgrade pip

:: 安装项目依赖
pip install -r requirements.txt

:: 显示安装的包
pip list

echo.
echo 虚拟环境设置完成！
echo 使用 'venv\Scripts\activate.bat' 来激活虚拟环境
echo 使用 'deactivate' 来退出虚拟环境
pause 
