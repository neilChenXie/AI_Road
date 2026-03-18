---
name: video-to-summary-v2
description: "将视频URL转换为文字总结。支持Bilibili (B站) 和 XiaoHongShu (小红书)。当用户提供视频链接并希望：提取视频内容、生成文字总结、语音转文字、视频转文本时触发。触发短语包括：'视频转文字', '视频总结', '提取视频内容', '转录视频', '视频字幕提取', 'summarize video', 'transcribe video', 'video to text', '小红书视频', 'B站视频'。即使是简单的'帮我看看这个视频'或'这个视频讲了什么'也应该触发此skill。"
---

# Video to Summary V2

将B站和小红书视频转换为文字总结。

## 工作流程

处理视频时，按以下步骤执行：

### 1. 运行处理脚本

使用 Bash 工具执行：

```bash
cd ~/.claude/skills/video-to-summary-v2 && python scripts/video_to_summary.py "视频URL"
```

脚本会自动完成：平台检测 → 视频下载 → 音频提取 → Whisper转录 → 生成总结。

### 2. 读取输出结果

脚本完成后，读取生成的文件并向用户展示总结：
- `output/<视频ID>/summary.md` - Markdown总结
- `output/<视频ID>/transcript.txt` - 完整转录文本

### 3. 展示给用户

将总结内容呈现给用户，可根据需要补充说明。

## 重要说明

- **视频无法通过 WebFetch 获取**：视频是二进制文件，必须通过 yt-dlp 下载
- **不要使用 TaskOutput 或其他工具**：直接用 Bash 运行脚本即可

## 支持平台

| 平台 | 链接格式 |
|------|---------|
| B站 | `bilibili.com/video/BV...` 或 `b23.tv/...` |
| 小红书 | `xiaohongshu.com/...` 或 `xhslink.com/...` |

## 命令参数

```bash
# 使用更大的Whisper模型
python scripts/video_to_summary.py "URL" --model medium

# 保留临时文件
python scripts/video_to_summary.py "URL" --keep-temp

# 检查依赖
python scripts/video_to_summary.py --check-deps
```

## 故障排除

**视频下载失败：**
- 小红书：确保URL包含完整参数
- B站：某些视频可能需要登录

**转录质量差：** 使用 `--model medium` 或 `--model large`
