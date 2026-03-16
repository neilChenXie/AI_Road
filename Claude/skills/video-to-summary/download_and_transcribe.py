#!/usr/bin/env python3
"""
下载B站音频并进行语音转文字
"""

import os
import sys
import json
import requests
import logging
from pathlib import Path

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def download_audio(audio_url: str, output_path: Path) -> bool:
    """下载音频文件"""
    try:
        logger.info(f"开始下载音频...")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Referer': 'https://www.bilibili.com'
        }
        
        response = requests.get(audio_url, headers=headers, stream=True, timeout=30)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        
        with open(output_path, 'wb') as f:
            downloaded = 0
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        percent = (downloaded / total_size) * 100
                        if downloaded % (1024 * 1024) < 8192:  # 每MB打印一次
                            logger.info(f"下载进度: {percent:.1f}%")
        
        logger.info(f"音频下载完成: {output_path}, 大小: {output_path.stat().st_size} bytes")
        return True
        
    except Exception as e:
        logger.error(f"下载音频失败: {e}")
        return False

def transcribe_audio(audio_path: Path, output_dir: Path) -> Path:
    """使用whisper转录音频"""
    try:
        import whisper
        
        logger.info(f"加载Whisper模型...")
        model = whisper.load_model("base")
        
        logger.info(f"开始转录音频: {audio_path}")
        result = model.transcribe(str(audio_path), language='zh', task='transcribe')
        
        # 保存结果
        transcript_path = output_dir / "transcript.txt"
        with open(transcript_path, 'w', encoding='utf-8') as f:
            f.write(result["text"])
        
        # 保存详细结果
        json_path = output_dir / "transcript.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        logger.info(f"转录完成: {transcript_path}")
        logger.info(f"转录文本长度: {len(result['text'])} 字符")
        
        return transcript_path
        
    except ImportError:
        logger.error("请先安装whisper: pip install openai-whisper")
        return None
    except Exception as e:
        logger.error(f"转录失败: {e}")
        return None

def main():
    """主函数"""
    # 读取API信息
    api_info_path = Path("output/20260314_000803/bilibili_api_info.json")
    
    if not api_info_path.exists():
        logger.error("API信息文件不存在")
        return
    
    with open(api_info_path, 'r', encoding='utf-8') as f:
        api_info = json.load(f)
    
    # 获取视频信息
    title = api_info.get("title", "未知")
    bvid = api_info.get("bvid", "未知")
    
    logger.info(f"视频标题: {title}")
    logger.info(f"BVID: {bvid}")
    
    # 选择最佳音频下载地址
    download_urls = api_info.get("download_info", {}).get("download_urls", [])
    audio_urls = [url for url in download_urls if url.get("format") == "dash_audio"]
    
    if not audio_urls:
        logger.error("未找到音频下载地址")
        return
    
    # 选择最高质量的音频
    best_audio = max(audio_urls, key=lambda x: x.get("bandwidth", 0))
    audio_url = best_audio["url"]
    
    logger.info(f"选择音频质量: {best_audio.get('bandwidth')} bps")
    
    # 创建输出目录
    output_dir = Path("output/20260314_000803/transcription")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 下载音频
    audio_path = output_dir / "audio.m4s"
    if not download_audio(audio_url, audio_path):
        logger.error("音频下载失败")
        return
    
    # 转录音频
    logger.info("开始语音转文字...")
    transcript_path = transcribe_audio(audio_path, output_dir)
    
    if transcript_path and transcript_path.exists():
        # 读取转录结果
        with open(transcript_path, 'r', encoding='utf-8') as f:
            transcript_text = f.read()
        
        logger.info("=" * 60)
        logger.info("音频转录完成！")
        logger.info(f"转录文件: {transcript_path}")
        logger.info(f"文本长度: {len(transcript_text)} 字符")
        logger.info("=" * 60)
        
        # 显示部分文本
        preview = transcript_text[:500] + "..." if len(transcript_text) > 500 else transcript_text
        logger.info(f"转录文本预览:\n{preview}")
        
    else:
        logger.error("语音转文字失败")

if __name__ == "__main__":
    main()
