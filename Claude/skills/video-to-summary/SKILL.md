---
name: video-to-summary
description: Convert video URLs to text summaries with speech-to-text transcription. Supports Bilibili (B站), YouTube, TikTok, Twitter, and other platforms. Use when users provide video URLs and want to: (1) Extract and transcribe audio content, (2) Generate text summaries from videos, (3) Download and process video content for analysis. Triggers on phrases like "视频转文字", "视频总结", "transcribe video", "summarize video", "提取视频内容".
---

# Video to Summary

Convert video URLs into structured text summaries with automatic speech recognition.

## Quick Start

Process a video URL:

```bash
python scripts/video_to_summary.py --url "https://b23.tv/xxx" --output-dir ./output
```

For Bilibili videos with API support (recommended):

```bash
python scripts/video_to_summary.py --url "https://b23.tv/xxx" --use-api --output-dir ./output
```

## Supported Platforms

- **Bilibili (B站)** - Full API support with 412 error bypass
- **YouTube** - Via yt-dlp (requires cookies for restricted content)
- **TikTok** - Via yt-dlp
- **Twitter/X** - Via yt-dlp
- **Other platforms** - Any platform supported by yt-dlp

## Core Workflow

1. **URL Analysis** - Detect platform and check API support
2. **Video Download** - Download video/audio with platform-specific handling
3. **Audio Extraction** - Extract audio track for transcription
4. **Speech-to-Text** - Transcribe audio using OpenAI Whisper
5. **Summarization** - Generate structured summary from transcript

## Key Features

### Bilibili API Integration

Bilibili videos use official API to bypass 412 anti-crawling errors:

- Automatic BVID extraction from short links (b23.tv)
- Video info retrieval without web scraping
- Direct download URL generation
- Subtitle support

See [references/bilibili-api.md](references/bilibili-api.md) for API details.

### Speech Recognition

Uses OpenAI Whisper for accurate transcription:

- Multiple model sizes (tiny, base, small, medium, large)
- Automatic language detection
- Chinese (zh) language optimization
- Timestamp support

See [references/whisper-config.md](references/whisper-config.md) for configuration.

## Installation

### Prerequisites

```bash
# System dependencies
apt-get install ffmpeg

# Python dependencies
pip install -r scripts/requirements.txt
```

### Whisper Setup

```bash
# Install Whisper (recommended in virtual environment)
python -m venv venv
source venv/bin/activate
pip install openai-whisper
```

## Usage Examples

### Basic Usage

```bash
# Process Bilibili video
python scripts/video_to_summary.py --url "https://b23.tv/hHipbJS" --use-api

# Process YouTube video
python scripts/video_to_summary.py --url "https://youtube.com/watch?v=xxx"

# Specify output directory
python scripts/video_to_summary.py --url "VIDEO_URL" --output-dir ./my-output
```

### Advanced Options

```bash
# Audio-only mode (faster, smaller files)
python scripts/video_to_summary.py --url "VIDEO_URL" --audio-only

# Specify language for transcription
python scripts/video_to_summary.py --url "VIDEO_URL" --lang zh

# Use specific Whisper model
python scripts/video_to_summary.py --url "VIDEO_URL" --model base
```

### Batch Processing

```bash
# Process multiple videos
bash scripts/batch_process.sh urls.txt
```

## Output Structure

```
output/
└── YYYYMMDD_HHMMSS/
    ├── bilibili_api_info.json      # Video metadata
    ├── transcription/
    │   ├── audio.wav               # Extracted audio
    │   ├── whisper_transcript.txt  # Transcription text
    │   ├── whisper_transcript.json # Detailed transcription data
    │   └── summary.md              # Generated summary
    └── final_report.json           # Processing report
```

## Configuration

### Environment Variables

- `WHISPER_MODEL` - Default Whisper model (default: base)
- `OUTPUT_DIR` - Default output directory (default: ./output)
- `BILIBILI_COOKIES` - Path to Bilibili cookies file (optional)

### Platform-Specific Notes

**Bilibili:**
- API method recommended for reliability
- No cookies required for public videos
- Rate limiting may apply for high-frequency requests

**YouTube:**
- Requires cookies for age-restricted content
- Use `--cookies` flag with cookies file path

## Troubleshooting

### Common Issues

**412 Error (Bilibili):**
- Use `--use-api` flag
- API method bypasses anti-crawling

**Whisper Not Found:**
- Install: `pip install openai-whisper`
- Use virtual environment recommended

**FFmpeg Missing:**
- Install: `apt-get install ffmpeg` (Ubuntu/Debian)
- Install: `brew install ffmpeg` (macOS)

**Slow Transcription:**
- Use smaller model: `--model tiny` or `--model base`
- Ensure audio-only mode: `--audio-only`

## Script Reference

- `scripts/video_to_summary.py` - Main processing script
- `scripts/batch_process.sh` - Batch processing wrapper
- `scripts/utils/` - Utility modules
  - `bilibili_api.py` - Bilibili API client
  - `video_downloader.py` - Multi-platform downloader
  - `audio_extractor.py` - Audio extraction utilities
  - `speech_to_text.py` - Whisper integration
  - `text_summarizer.py` - Summary generation

## References

- [Bilibili API Documentation](references/bilibili-api.md)
- [Whisper Configuration](references/whisper-config.md)
- [Platform Support Matrix](references/platforms.md)
