# 使用Python官方镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    LANG=C.UTF-8 \
    TZ=Asia/Shanghai

# 安装系统依赖
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 先复制 requirements.txt 以利用 Docker 缓存
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制源代码和入口脚本
COPY src/ ./src/
COPY docker/entrypoint.sh /entrypoint.sh

# 创建必要的目录
RUN mkdir -p /app/epub /app/audio_book /app/txt_book && \
    chmod +x /entrypoint.sh

# 设置卷挂载点
VOLUME ["/app/epub", "/app/audio_book", "/app/txt_book"]

ENTRYPOINT ["/entrypoint.sh"] 