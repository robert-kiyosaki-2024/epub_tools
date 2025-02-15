# EPUB有声书生成器

## 项目简介
这是一个自动处理EPUB电子书的Python工具集，包含以下功能：
1. 将EPUB转换为有声书（MP3格式）
2. 将EPUB转换为文本文件（TXT格式）

## 功能特点
- 批量处理目录下的所有EPUB文件
- 自动提取EPUB文件中的文本内容
- 支持将大文本自动分割成小块处理
- 支持两种转换模式：
  - EPUB → MP3（使用Edge-TTS）
  - EPUB → TXT
- 自动为每本书创建独立的输出目录

## 使用方法

### 目录结构
```
epub-audiobook-generator/
  ├── epub/                  # 存放EPUB源文件
  ├── audio_book/           # 音频输出目录
  │   └── 书名/
  │       ├── 001.mp3
  │       ├── 002.mp3
  │       └── ...
  ├── txt_book/            # 文本输出目录
  │   └── 书名/
  │       ├── 001.txt
  │       ├── 002.txt
  │       └── ...
  └── src/                 # 源代码目录
```

### 转换为有声书
```bash
.\epub2audio.ps1
```

### 转换为文本文件
```bash
.\epub2txt.ps1
```

### 使用Docker
```bash
docker run -v $(pwd)/epub:/app/epub -v $(pwd)/audio_book:/app/audio_book -v $(pwd)/txt_book:/app/txt_book epub-converter text # 转换为文本
docker run -v $(pwd)/epub:/app/epub -v $(pwd)/audio_book:/app/audio_book -v $(pwd)/txt_book:/app/txt_book epub-converter audio # 转换为音频
``` 

### 使用Docker Compose
```bash
docker-compose run --rm epub-converter text   # 转换为文本
docker-compose run --rm epub-converter audio  # 转换为音频
``` 

## 输出说明
- 有声书输出位置：.\audio_book\书名\001.mp3
- 文本文件输出位置：.\txt_book\书名\001.txt

## 支持的声音列表
- zh-CN-XiaoxiaoNeural (女声)
- zh-CN-YunxiNeural (默认，男声)
- zh-CN-YunyangNeural (男声)
- zh-CN-XiaochenNeural (女声)
- zh-CN-XiaohanNeural (女声)
- zh-CN-XiaomoNeural (女声)
- zh-CN-XiaoruiNeural (女声)

## 项目结构
```
epub-audiobook-generator/
  ├── src/
  │   ├── epub2audio.py      # 音频转换主程序
  │   ├── epub2txt.py        # 文本转换主程序
  │   ├── epub_parser.py     # EPUB解析器
  │   ├── text_splitter.py   # 文本分割器
  │   └── audio_generator.py # 音频生成器
  ├── requirements.txt       # 项目依赖
  ├── epub2audio.ps1        # 音频转换启动脚本
  ├── epub2txt.ps1          # 文本转换启动脚本
  └── README.md             # 项目说明文档
```

## 注意事项
1. 确保您有足够的磁盘空间存储生成的音频文件
2. 处理大型EPUB文件可能需要较长时间
3. 需要稳定的网络连接以使用Edge-TTS服务
4. 请将EPUB文件放在 epub 目录下
5. 输出文件会自动按书名分类存放

## 许可证
该项目采用 MIT 许可证。

## 贡献指南
欢迎提交 Issue 和 Pull Request 来帮助改进项目。

## 联系方式
如有问题或建议，请通过 GitHub Issues 与我们联系。
