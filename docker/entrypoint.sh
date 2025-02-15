#!/bin/bash

# 检查命令行参数
if [ "$1" = "text" ]; then
    echo "开始转换EPUB为文本..."
    python src/epub2txt.py
elif [ "$1" = "audio" ]; then
    echo "开始转换EPUB为音频..."
    python src/epub2audio.py
else
    echo "请指定转换类型: text 或 audio"
    echo "例如: docker run ... text"
    echo "或: docker run ... audio"
    exit 1
fi 