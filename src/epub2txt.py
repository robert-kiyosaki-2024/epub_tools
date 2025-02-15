import argparse
import os
from epub_parser import EPUBParser
from text_splitter import TextSplitter

def parse_arguments():
    parser = argparse.ArgumentParser(description='将EPUB文件转换为TXT文件')
    parser.add_argument('--input_dir', default='epub', help='EPUB文件所在目录')
    parser.add_argument('--output_dir', default='txt_book', help='TXT文件输出目录')
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
        
        # 创建书籍专属目录
        book_dir = os.path.join(output_dir, book_name)
        os.makedirs(book_dir, exist_ok=True)
        
        # 解析EPUB
        parser = EPUBParser(epub_path)
        content = parser.extract_text()
        
        if not content:
            print(f"警告: {epub_file} 未提取到内容")
            continue
        
        print(f"正在为 {book_name} 生成文本文件...")
        
        # 分割文本
        splitter = TextSplitter()
        text_chunks = splitter.split_text(content)
        
        # 保存文本文件
        for i, chunk in enumerate(text_chunks, 1):
            # 使用序号命名
            output_file = os.path.join(book_dir, f'{i:03d}.txt')
            try:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(chunk)
                print(f"已生成: {output_file}")
            except Exception as e:
                print(f"保存文件时出错 {output_file}: {str(e)}")
                continue
        
        print(f"完成 {book_name} 的文本生成")

if __name__ == '__main__':
    main() 