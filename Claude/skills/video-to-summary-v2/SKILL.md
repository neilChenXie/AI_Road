---
name: video-to-summary-v2
description: "IMMEDIATELY HANDLE ANY VIDEO URL by extracting and transcribing. Use this whenever users share a video URL and ask to summarize, transcribe, or extract content from B站 (Bilibili), 小红书 (XiaoHongShu), or ask 'what's in this video?'. Support both Chinese and English. Follow the workflow，必须使用Python脚本. Trigger on phrases: '视频总结', 'summarize video', 'transcribe video', or any video link + 'what do you see?', '帮我看看', 'extract content'."
---

# Video to Summary V2

EXECUTE THIS WORKFLOW when user provides a video URL:

## ⚠️ 重要：必须使用本 Skill 的 Python 脚本

**禁止**直接调用 fetch、yt-dlp、whisper 等命令行工具。
必须通过运行 `python scripts/video_to_summary.py "the_user_provided_url"` 来完成任务。

## Quick Reference

| Task | Guide |
|------|-------|
| 总结视频 | `python scripts/video_to_summary.py "the_user_provided_url"` |

## Workflow

Your job is to execute these exact steps in sequence:

### 1. Run the Script
Execute with the user's URL:
```bash
python scripts/video_to_summary.py "the_user_provided_url"
```

### 2. Read the Generated Files
Wait for the script to complete. Read that file to show the user:
```
📄 总结文件: output/[VIDEO_ID]/[视频标题].md
```
If user needs more detail, also check `transcript/transcript.txt` in the same directory.

### 3. Present to User
Display the summary markdown file content directly, formatted as Markdown. If the user asks for transcript or detailed breakdown, use files in the same directory.

## Supported Platforms

| Platform | URL Pattern | Notes |
|----------|-----------|-------|
| **B站 (Bilibili)** | `bilibili.com/video/BV...` or `b23.tv/...` | Handles short links |
| **小红书 (XiaoHongShu)** | `xiaohongshu.com/...` or `xhslink.com/...` | Preserves full URL params |

## Advanced Options (Use Only If Needed)

If the first run fails or user needs special handling, use these flags:

```bash
# Higher accuracy (slower, ~2x time):
python scripts/video_to_summary.py "URL" --model base

# Keep temporary files for debugging:
python scripts/video_to_summary.py "URL" --keep-temp

# Custom output location:
python scripts/video_to_summary.py "URL" --output-dir /path/to/output

# Just check if dependencies are installed:
python scripts/video_to_summary.py --check-deps
```

## Output File Structure

After running, files are generated in `output/[VIDEO_ID]/` (relative to this skill directory):

- **[视频标题].md** ← **Show this to the user** (formatted Markdown with title, overview, key points, detailed breakdown)
- **[视频标题]_summary.json** — Structured data version if user needs parsing
- **transcript.txt** — Full plain-text transcription (inside transcript/ folder)
- **transcript.json** — Detailed transcript with timestamps (inside transcript/ folder)

Note: Output files are saved to `/Users/chen/.claude/skills/video-to-summary-v2/output/[VIDEO_ID]/`

## Common Issues & Fixes

**The script won't run / Python not found**
→ First, run: `python scripts/video_to_summary.py --check-deps`. Then use: `python scripts/video_to_summary.py "the_user_provided_url"` from the skill directory to install missing dependencies.

**Video download fails**
- For   小红书: Ensure URL has full parameters (especially xsec_token) — use share link, not browser bar
- For B站: Some videos may require login or cookies; the script tries automatically

**Transcription is garbled or too short**
→ The downloaded video may be corrupted. Retry with: `python scripts/video_to_summary.py "URL" --keep-temp` and check the downloaded file.

**"Model not found" error**
→ First Whisper model download takes time (~500MB). Let it complete. Or specify smaller: `--model tiny` or `--model small`.

## Configuration

The skill reads `config.yaml` for:
- `whisper.model` — Which Whisper size to use (base/small/medium/large)
- `output.cleanup_temp` — Whether to delete video after processing
- `download.timeout` — How long to wait for video download
