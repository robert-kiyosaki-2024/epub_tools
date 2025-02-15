import asyncio
import edge_tts
import os

class AudioGenerator:
    def __init__(self, voice):
        self.voice = voice
        
    def generate_audio(self, text_chunks, output_dir, book_name):
        """为每个文本块生成音频文件"""
        # 创建书籍专属目录
        book_dir = os.path.join(output_dir, book_name)
        os.makedirs(book_dir, exist_ok=True)
        
        for i, chunk in enumerate(text_chunks, 1):
            # 使用序号命名
            output_file = os.path.join(book_dir, f'{i:03d}.mp3')
            
            # 使用异步方式调用edge-tts
            asyncio.run(self._generate_single_audio(chunk, output_file))
            print(f'已生成音频文件: {output_file}')
    
    async def _generate_single_audio(self, text, output_file):
        """生成单个音频文件"""
        communicate = edge_tts.Communicate(text, self.voice)
        await communicate.save(output_file) 