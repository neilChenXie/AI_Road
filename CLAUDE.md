# CLAUDE.md - AI开发助手指南

## ⚠️ 重要提醒

- **执行脚本前务必确认当前工作目录**
- **复杂项目优先使用绝对路径**
- **API返回数据需验证时效性**
- **养成先测试后集成的习惯**

---

## 项目开发规范

### 路径使用规范

**问题：**
项目结构复杂（如 `Claude/skills/{skill-name}/`），执行脚本时容易因路径错误导致失败。

**解决方案：**

```bash
# ✅ 推荐：使用绝对路径
python /Users/chen/Project/ai-road/Claude/skills/{skill-name}/scripts/main.py

# ✅ 推荐：先cd到正确目录再执行
cd /Users/chen/Project/ai-road/Claude/skills/{skill-name}
python scripts/main.py

# ✅ 推荐：执行前确认当前位置
pwd  # 确认当前目录
python scripts/main.py
```

**常见错误：**
```bash
# ❌ 错误：在错误目录下执行相对路径
pwd  # /Users/chen/Project/ai-road
python scripts/main.py  # 报错：找不到文件
```

### API调试规范

**问题：**
第三方API可能返回陈旧数据或停止维护，AI容易误判"有返回值就是正确的"。

**解决方案：**

1. **独立测试API**：在ipython或独立脚本中测试接口
2. **验证数据时效性**：检查返回数据的最新日期是否符合预期
3. **对比多个API**：同一功能可能有多个接口，选择数据最新的
4. **形成验证脚本**：将正确的API调用保存为独立脚本便于复用

**示例：**
```python
# test_api.py - API验证脚本
import akshare as ak

# 测试接口1
df1 = ak.stock_yjbb_em()
print(f"接口1最新日期: {df1['最新公告日期'].max()}")

# 测试接口2
df2 = ak.stock_notice_report(symbol='全部', date='20260402')
print(f"接口2公告数量: {len(df2)}")

# 对比选择正确的接口
```

### Python调试规范

**问题：**
不同项目可能依赖不同版本的Python包，直接在系统环境调试容易导致依赖冲突。

**解决方案：**

1. **使用Python虚拟环境**：为每个项目创建独立的虚拟环境
2. **在虚拟环境中调试**：确保依赖隔离，避免影响系统环境
3. **记录依赖清单**：使用 `requirements.txt` 记录项目依赖

**示例：**
```bash
# 1. 创建虚拟环境（在项目目录下）
cd /Users/chen/Project/ai-road/Claude/skills/{skill-name}
python -m venv venv

# 2. 激活虚拟环境
source venv/bin/activate  # macOS/Linux
# 或
venv\Scripts\activate  # Windows

# 3. 安装依赖
pip install -r requirements.txt

# 4. 在虚拟环境中调试Python脚本
python scripts/main.py

# 5. 退出虚拟环境
deactivate
```

**调试技巧：**
```bash
# 使用ipython进行交互式调试
ipython

# 在ipython中导入项目模块测试
import sys
sys.path.insert(0, '/Users/chen/Project/ai-road/Claude/skills/{skill-name}')
from scripts.fetch_today_reports import fetch_reports_by_date

# 测试函数
df = fetch_reports_by_date('20260402')
print(df.head())
```

### 开发流程建议

1. **先验证，后集成**：确保API正确再写入主程序
2. **小步快跑**：每个功能独立测试通过后再合并
3. **记录问题**：在 `dev-logs/{skill-name}/` 下记录遇到的问题和解决方案
4. **使用虚拟环境**：避免依赖冲突，确保环境一致性

### 项目结构说明

```
ai-road/
├── CLAUDE.md              # 本文件 - 开发规范
├── Claude/
│   └── skills/            # Skill项目目录
│       ├── {skill-name-1}/
│       ├── {skill-name-2}/
│       └── ...
└── dev-logs/              # 开发日志
    ├── {skill-name-1}/
    └── {skill-name-2}/
```

