import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import warnings

class EPUBParser:
    def __init__(self, epub_path):
        self.epub_path = epub_path
        
    def extract_text(self):
        """从EPUB文件中提取文本内容"""
        # 忽略特定的警告
        warnings.filterwarnings('ignore', category=UserWarning, 
                              module='ebooklib.epub')
        warnings.filterwarnings('ignore', category=FutureWarning, 
                              module='ebooklib.epub')
        
        try:
            book = epub.read_epub(self.epub_path, options={'ignore_ncx': True})
            text_content = []
            
            for item in book.get_items():
                if item.get_type() == ebooklib.ITEM_DOCUMENT:
                    try:
                        soup = BeautifulSoup(item.get_content(), 'html.parser')
                        # 移除script和style元素
                        for script in soup(["script", "style"]):
                            script.decompose()
                        text = soup.get_text()
                        # 清理文本
                        lines = (line.strip() for line in text.splitlines())
                        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                        text = '\n'.join(chunk for chunk in chunks if chunk)
                        if text.strip():  # 只添加非空文本
                            text_content.append(text)
                    except Exception as e:
                        print(f"处理章节时出错: {str(e)}")
                        continue
                        
            return '\n'.join(text_content)
            
        except Exception as e:
            print(f"解析EPUB文件时出错: {str(e)}")
            return "" 