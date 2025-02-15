#!/bin/bash

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 升级pip
pip install --upgrade pip

# 安装项目依赖
pip install -r requirements.txt

# 显示安装的包
pip list

echo "虚拟环境设置完成！"
echo "使用 'source venv/bin/activate' 来激活虚拟环境"
echo "使用 'deactivate' 来退出虚拟环境" 