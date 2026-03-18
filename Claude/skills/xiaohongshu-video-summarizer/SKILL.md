---
name: xiaohongshu-video-summarizer
description: 下载小红书视频并自动提取转录内容和生成总结。使用此技能当用户提供小红书视频URL并要求下载、转录或总结视频内容。支持通过yt-dlp下载视频、FFmpeg提取音频、Whisper进行语音转文字、以及总结视频观点等。如果用户提到小红书、短视频下载、视频转录、语音识别或视频内容分析，都应该使用此技能。
compatibility: 需要yt-dlp、FFmpeg、OpenAI Whisper这三个工具；Python 3.9+
---

# 小红书视频下载和总结Skill

## 概述

此skill自动化小红书视频的下载、转录和总结流程。它可以帮助用户快速获取视频内容的文字版本和要点总结。

## 使用步骤

### 准备环境

首先确保已安装所需的工具和包。运行脚本中的安装步骤：

```bash
# 1. 安装yt-dlp
pip install yt-dlp

# 2. 安装Whisper
pip install openai-whisper

# 3. 检查ffmpeg是否已安装
ffmpeg -version
# 如果未安装，在macOS上可以用：
brew install ffmpeg
```

### 核心工作流程

当用户提供小红书视频URL时，按照以下步骤处理：

#### 步骤1：下载视频

使用yt-dlp下载视频，命令格式如下：

```bash
yt-dlp --referer "https://www.xiaohongshu.com" \
  --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
  "视频URL"
```

**关键参数说明：**
- `--referer "https://www.xiaohongshu.com"` - 设置HTTP referer防止被阻止
- `--user-agent` - 设置用户代理，模拟浏览器请求
- URL必须是完整的小红书视频链接

**预期输出：** 一个mp4或其他视频格式的文件

#### 步骤2：提取音频

使用FFmpeg从视频中提取音频：

```bash
ffmpeg -i input_video.mp4 -q:a 0 -map a output_audio.mp3
```

**参数说明：**
- `-i input_video.mp4` - 输入视频文件
- `-q:a 0 -map a` - 最高质量地提取音频流
- `output_audio.mp3` - 输出音频文件

**预期输出：** 一个mp3或wav格式的音频文件

#### 步骤3：语音转文字

使用OpenAI的Whisper模型进行转录：

```bash
whisper audio_file.mp3 --model base --language zh
```

**参数说明：**
- `--model base` - 使用base模型（平衡速度和准确度）
- `--language zh` - 指定中文语言
- Whisper将自动输出几个格式的转录文本（txt、json、srt等）

#### 步骤4：总结内容

基于转录的文本内容生成总结。总结应该：
- 提取主要观点和核心信息
- 保留重要数据和引用
- 组织成清晰的段落或要点形式
- 长度为原文的20-30%

## 输出格式

处理完成后，向用户显示：

```
===== 小红书视频内容总结 =====
URL: [原始视频URL]
下载时间: [时间戳]

【完整转录】
[转录的完整文本]

【核心要点总结】
[用户偏好的总结格式 - 此处为纯文本显示]

【处理完成】
已删除临时文件：视频文件、音频文件
保留的文件：转录文本
```

## 错误处理

流程中可能出现的错误及处理方式：

| 错误类型 | 可能原因 | 解决方法 |
|---------|--------|--------|
| 下载失败 | URL无效、网络问题、被封禁 | 检查URL格式，稍后重试，检查网络连接 |
| 音频提取失败 | FFmpeg未安装或视频格式不支持 | 确认FFmpeg已正确安装：`ffmpeg -version` |
| Whisper转录失败 | Whisper未安装或权限问题 | 运行 `pip install openai-whisper` 更新 |
| 语言检测错误 | 音频内容混合多种语言 | 手动指定 `--language zh` |

当遇到任何错误，应该：
1. 报告具体的错误信息
2. 说明停在哪个处理步骤
3. 建议用户的解决方案
4. 停止处理不继续后续步骤

## 脚本使用

在 `scripts/` 目录中提供了 `download_and_summarize.py` 脚本，可以一键完成整个流程：

```bash
python scripts/download_and_summarize.py "小红书视频URL"
```

脚本会自动处理所有步骤，并在完成后删除临时文件。

## 配置项

脚本支持以下可选参数：

- `--model` - Whisper模型大小，可选：tiny, base, small, medium, large（默认：base）
- `--language` - 语言代码（默认：zh）
- `--keep-files` - 完成后保留所有文件（默认：删除）
- `--output-dir` - 指定输出目录（默认：当前目录）

## 常见问题

**Q: 能处理其他短视频平台吗？**
A: 此skill特定于小红书。其他平台（如TikTok、YouTube等）可能需要不同的配置或headers。

**Q: 转录准确度如何？**
A: Whisper base模型的中文准确度约为80-90%，取决于视频音质。如需更高准确度，可使用medium或large模型，但会更耗时。

**Q: 支持处理多语言内容吗？**
A: 可以。Whisper支持99+种语言。如果内容是英文或其他语言，修改 `--language` 参数即可。

**Q: 下载的视频是否会被保存？**
A: 默认不保存。处理完成后自动删除以节省空间。使用 `--keep-files` 参数可保留所有文件。

## 依赖和版本

- Python 3.9+
- yt-dlp >= 2024.01.01
- FFmpeg >= 4.0
- openai-whisper >= 20231117
- OpenAI API访问（可选，用于高级总结功能）
