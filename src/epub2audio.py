import argparse
import os
from epub_parser import EPUBParser
from text_splitter import TextSplitter
from audio_generator import AudioGenerator

def parse_arguments():
    parser = argparse.ArgumentParser(description='将EPUB文件转换为有声书')
    parser.add_argument('--input_dir', default='epub', help='EPUB文件所在目录')
    parser.add_argument('--output_dir', default='audio_book', help='音频文件输出目录')
    parser.add_argument('--voice', default='zh-CN-YunxiNeural', 
                        help='Edge TTS声音选择')
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    # 使用正确的路径格式
    input_dir = os.path.abspath(args.input_dir)
    output_dir = os.path.abspath(args.output_dir)
    
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 获取所有epub文件
    epub_files = [f for f in os.listdir(input_dir) 
                  if f.lower().endswith('.epub')]
    
    for epub_file in epub_files:
        print(f"\n开始处理: {epub_file}")
        epub_path = os.path.join(input_dir, epub_file)
        book_name = os.path.splitext(epub_file)[0]
        
        # 解析EPUB
        parser = EPUBParser(epub_path)
        content = parser.extract_text()
        
        if not content:
            print(f"警告: {epub_file} 未提取到内容")
            continue
        
        print(f"正在为 {book_name} 生成音频文件...")
        
        # 分割文本
        splitter = TextSplitter()
        text_chunks = splitter.split_text(content)
        
        # 生成音频
        generator = AudioGenerator(args.voice)
        generator.generate_audio(text_chunks, output_dir, book_name)
        
        print(f"完成 {book_name} 的音频生成")

if __name__ == '__main__':
    main() 