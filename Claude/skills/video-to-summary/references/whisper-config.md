# Whisper Configuration Guide

## Model Selection

Choose the appropriate model based on your needs:

| Model | VRAM | Speed | Accuracy | Use Case |
|-------|------|-------|----------|----------|
| tiny | ~1GB | Fastest | Good | Quick drafts, real-time |
| base | ~1GB | Fast | Better | General purpose (recommended) |
| small | ~2GB | Medium | Good | Higher accuracy needed |
| medium | ~5GB | Slow | Better | Professional transcription |
| large | ~10GB | Slowest | Best | Maximum accuracy |

## Language Support

### Chinese (zh)

Optimized for Chinese transcription:

```bash
python scripts/video_to_summary.py --url "URL" --lang zh
```

### Auto-detection

Let Whisper detect language automatically:

```bash
python scripts/video_to_summary.py --url "URL" --lang auto
```

## Performance Optimization

### GPU Acceleration

Whisper automatically uses GPU if available:

```python
import torch
print(torch.cuda.is_available())  # Check GPU availability
```

### CPU Optimization

For CPU-only systems:

```bash
# Use smaller model
python scripts/video_to_summary.py --url "URL" --model tiny

# Reduce audio quality (faster processing)
python scripts/audio_extractor.py --quality low
```

### Memory Management

For large videos:

```bash
# Split audio into chunks
ffmpeg -i audio.wav -f segment -segment_time 600 -c copy chunk_%03d.wav

# Process chunks separately
for chunk in chunk_*.wav; do
    whisper $chunk --language zh
done
```

## Output Formats

### Text

```bash
whisper audio.wav --output_format txt
```

### JSON (with timestamps)

```bash
whisper audio.wav --output_format json
```

### SRT (subtitles)

```bash
whisper audio.wav --output_format srt
```

## Advanced Options

### Temperature

Control randomness in transcription:

```python
result = model.transcribe(audio, temperature=0.2)
```

- Lower (0.0-0.3): More deterministic
- Higher (0.5-1.0): More creative

### Initial Prompt

Provide context for better transcription:

```python
prompt = "这是一段关于股市分析的视频"
result = model.transcribe(audio, initial_prompt=prompt)
```

### Word-level Timestamps

```python
result = model.transcribe(audio, word_timestamps=True)
```

## Installation

### Standard Installation

```bash
pip install openai-whisper
```

### With GPU Support

```bash
pip install openai-whisper[gpu]
```

### Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate  # Windows

pip install openai-whisper
```

## Troubleshooting

### FP16 Warning

```
UserWarning: FP16 is not supported on CPU; using FP32 instead
```

This is normal for CPU systems. Ignore this warning.

### CUDA Out of Memory

Use smaller model or reduce batch size:

```bash
# Use smaller model
whisper audio.wav --model base

# Or use CPU
CUDA_VISIBLE_DEVICES="" whisper audio.wav
```

### Slow Transcription

- Use GPU if available
- Use smaller model (tiny/base)
- Reduce audio quality before transcription
- Split long audio into chunks

## Model Downloads

Models are automatically downloaded on first use:

- Linux/macOS: `~/.cache/whisper/`
- Windows: `C:\Users\<user>\.cache\whisper\`

Manual download:

```bash
# Download specific model
wget https://openaipublic.azureedge.net/main/whisper/models/ed3a0b6b1c0edf879ad9b11b1af5a0e6ab5db9205f891f668f8b0e6c6326e34e/base.pt
```
