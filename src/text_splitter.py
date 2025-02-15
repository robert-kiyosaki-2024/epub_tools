class TextSplitter:
    def __init__(self, chunk_size=5000):
        self.chunk_size = chunk_size
        
    def split_text(self, text):
        """将文本分割成较小的块"""
        chunks = []
        current_chunk = []
        current_size = 0
        
        # 按段落分割
        paragraphs = text.split('\n')
        
        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            if not paragraph:
                continue
                
            # 如果当前段落加上已有内容超过限制，保存当前块并开始新块
            if current_size + len(paragraph) > self.chunk_size:
                if current_chunk:
                    chunks.append('\n'.join(current_chunk))
                current_chunk = [paragraph]
                current_size = len(paragraph)
            else:
                current_chunk.append(paragraph)
                current_size += len(paragraph)
        
        # 添加最后一个块
        if current_chunk:
            chunks.append('\n'.join(current_chunk))
            
        return chunks 