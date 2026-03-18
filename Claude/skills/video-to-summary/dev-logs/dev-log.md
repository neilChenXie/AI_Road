# Video-to-Summary Skill 开发经验汇总

> 基于 v2.1 ~ v2.3.3 开发过程的总结

---

## 一、技术实现经验

### 1.1 平台适配策略

**小红书下载优化（核心突破）**

小红书视频下载需要专用命令格式，不能使用标准的 yt-dlp 参数：

```bash
# 正确方式
yt-dlp --referer "https://www.xiaohongshu.com" \
       --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
       "完整URL（包含xsec_token）"

# 错误方式（会失败）
yt-dlp --cookies browser --dump-json "URL"
yt-dlp --no-playlist -f best "URL"
```

**关键要点：**
- 必须使用完整的分享链接（包含所有查询参数，尤其是 `xsec_token`）
- 不需要浏览器 cookies
- 不要添加额外的 yt-dlp 参数

### 1.2 命令行接口设计

**简化参数设计**

```bash
# 旧设计（易出错）
python3 scripts/video_to_summary.py --url "URL" --output-dir ./output

# 新设计（简洁可靠）
python scripts/video_to_summary.py "URL" --output-dir ./output
```

**改进点：**
- URL 作为位置参数，而非 `--url` 标志
- 统一使用 `python` 和 `pip`，避免 `python3`/`pip3` 的系统差异
- YAML front matter 中 description 字段需用引号包裹

### 1.3 Bug 修复记录

| 问题 | 根因 | 解决方案 |
|------|------|----------|
| Whisper `--language ''` 报错 | 空字符串参数不合法 | 当 language 为空或 'auto' 时不传递该参数 |
| macOS 文件名过长错误 | 255 字节限制 | 使用固定的 `transcript` 作为文件名 |
| 小红书下载失败 | `--dump-json` 和 cookies 方式不稳定 | 使用专用的 referer/user-agent 命令格式 |

---

## 二、Skill 开发核心经验

### 2.1 最重要发现：AI 会绕过低效的 Skill

> **核心原则**：如果 SKILL 的安排不高效，AI 会自动绕过。

这是开发过程中最重要的发现。即使 SKILL.md 写得再详细，如果 AI 认为直接用命令行更简单，它就会跳过你的 Python 脚本。

**表现：**
- Skill 成功加载（显示 "Successfully loaded skill"）
- 但 AI 不执行脚本中的命令
- AI 自行调用 yt-dlp、whisper 等工具

### 2.2 SKILL.md 设计原则

**失败的设计：**
- 文档太长（127 行），模型没有仔细阅读关键指令
- 使用描述性语言："视频文件需要下载后才能处理"
- 缺少强制执行标记

**成功的设计：**
```markdown
## ⚠️ 重要：必须使用本 Skill 的 Python 脚本

**禁止**直接调用 yt-dlp、whisper 等命令行工具。
必须通过运行 `python skill_script.py` 来完成任务。
```

**关键要素：**
1. **开头就是明确的强制指令** - "IMMEDIATELY HANDLE..."
2. **使用强硬语气** - 加粗、警告符号、"禁止"、"必须"
3. **简洁的工作流程** - 1. Run, 2. Read, 3. Present
4. **降低"绕过"的动机** - 脚本应提供真正的价值（错误重试、格式化输出、多步骤编排）

### 2.3 调试 Skill 的方法

**调试路径问题：**
- 开发目录：`/Users/chen/Project/AI_Road/Claude/skills/video-to-summary/`
- 安装目录：`~/.claude/skills/video-to-summary/`
- 两者路径不一致可能导致问题

**调试工具：**
- `/skill-creator` - 官方的 skill 创建和优化工具
- `evals/evals.json` - 测试 skill 的触发和执行

**关键调试问题：**
1. 问 AI："你整个过程是使用的 skill 中的 Python 脚本吗？"
2. 检查 AI 是否真的执行了脚本，还是绕过了

---

## 三、版本迭代历程

| 版本 | 日期 | 主要改进 |
|------|------|----------|
| v2.1 | 2026-03-15 | 小红书下载优化、Bug 修复 |
| v2.2 | 2026-03-16 | CLI 命令简化、YAML 规范化 |
| v2.3.1 | - | 调试 skill-creator、发现执行问题 |
| v2.3.2 | - | 根因分析、多版 SKILL.md 尝试 |
| v2.3.3 | - | 确认核心原因：AI 绕过低效 Skill |

---

## 四、最佳实践总结

### 4.1 Skill 文件结构

```
skill-name/
├── SKILL.md          ← 必须，核心文件
└── （可选资源）
   ├── scripts/       ← 可执行脚本
   ├── references/    ← 参考文档
   └── assets/        ← 输出用文件
```

### 4.2 SKILL.md 编写指南

1. **开头就是可执行代码**，而非详细说明
2. **使用强制短语**：IMMEDIATELY、MUST、REQUIRED
3. **文档简洁**，结构清晰
4. **禁止事项明确列出**："不要使用 WebFetch"、"不要使用 TaskOutput"

### 4.3 脚本设计指南

不要让脚本只是简单封装命令行调用。脚本应提供：
- 自动错误重试
- 格式化输出结果
- 多步骤流程编排
- 平台特定的处理逻辑

这样 AI 才有动力使用脚本，而不是绕过它。

---

## 五、待改进项

- [ ] 支持更多视频平台
- [ ] 优化长视频处理性能
- [ ] 添加批量处理功能
- [ ] 支持自定义输出模板
- [ ] 提高脚本执行率（彻底解决 AI 绕过问题）

---

## 六、参考资源

- Claude Code 官方 skill-creator
- yt-dlp 文档
- Whisper 文档
