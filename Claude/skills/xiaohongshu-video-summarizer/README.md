# 小红书视频下载和总结 Skill

自动下载小红书视频并生成转录和总结的AI skill。

## 快速开始

### 1. 安装依赖

```bash
bash scripts/install_deps.sh
```

或手动安装：
```bash
pip install yt-dlp openai-whisper
brew install ffmpeg  # macOS
```

### 2. 使用脚本

```bash
python scripts/download_and_summarize.py "小红书视频URL"
```

### 3. 可选参数

```bash
# 使用更高精度的Whisper模型
python scripts/download_and_summarize.py "URL" --model medium

# 保留所有文件（默认删除临时文件）
python scripts/download_and_summarize.py "URL" --keep-files

# 指定输出目录
python scripts/download_and_summarize.py "URL" --output-dir ./results
```

## 工作流程

1. **下载视频** - 使用yt-dlp + 小红书专用headers
2. **提取音频** - 使用FFmpeg从视频中提取音频
3. **转录文字** - 使用OpenAI Whisper进行语音转文字
4. **生成总结** - 对转录内容进行总结
5. **输出结果** - 显示在命令行并保存文件

## Whisper模型对比

| 模型 | 相对速度 | 相对准确度 | 适用场景 |
|------|---------|----------|--------|
| tiny | 最快 ⚡ | 最低 | 快速检查内容概况 |
| base | 快 ⚡ | 中等 ✓ | **推荐**（平衡） |
| small | 中等 | 较好 | 高要求的转录 |
| medium | 慢 | 好 | 专业内容 |
| large | 最慢 🐢 | 最好 | 关键内容必须精准 |

## 注意事项

- 首次运行Whisper会自动下载模型文件（约140MB for base）
- 长视频处理时间较长（取决于视频长度和所选模型）
- 建议在网络稳定的环境下运行
- 小红书等平台可能会升级反爬虫措施，工具可能需要定期更新

## 故障排除

### "yt-dlp command not found"
```bash
pip install yt-dlp
```

### "FFmpeg not found"
```bash
brew install ffmpeg  # macOS
sudo apt install ffmpeg  # Ubuntu/Debian
```

### "Whisper not installed"
```bash
pip install openai-whisper
```

### 下载失败或被封禁
- 检查URL格式是否正确
- 等待一段时间后重新尝试
- 确保网络连接正常

## 文件结构

```
xiaohongshu-video-summarizer/
├── SKILL.md                    # Skill说明文档
├── README.md                   # 本文件
├── scripts/
│   ├── download_and_summarize.py  # 主脚本
│   └── install_deps.sh            # 依赖安装脚本
├── references/                 # 参考文档
└── evals/
    └── evals.json             # 测试用例
```

## 技术栈

- **Python 3.9+** - 脚本语言
- **yt-dlp** - 视频下载工具
- **FFmpeg** - 音视频处理
- **OpenAI Whisper** - 语音转文字

## 许可证

MIT
