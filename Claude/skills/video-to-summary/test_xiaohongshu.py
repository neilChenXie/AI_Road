#!/usr/bin/env python3
"""
测试小红书视频下载配置
"""

import sys
import subprocess
from pathlib import Path

# 添加模块路径
sys.path.insert(0, str(Path(__file__).parent / "scripts"))

from utils.platform_detector import detect_platform, get_platform_info, PLATFORM_NAMES

# 测试URL
test_url = "https://www.xiaohongshu.com/discovery/item/69732e85000000002103ec2d"

print("=" * 60)
print("测试小红书平台检测")
print("=" * 60)

# 检测平台
platform_id = detect_platform(test_url)
platform_name = PLATFORM_NAMES.get(platform_id, platform_id)
print(f"平台ID: {platform_id}")
print(f"平台名称: {platform_name}")

# 获取平台信息
info = get_platform_info(test_url)
print(f"\n平台详细信息:")
print(f"  ID: {info.get('id')}")
print(f"  名称: {info.get('name')}")
print(f"  配置: {info.get('config')}")

# 构建下载命令
print(f"\n构建yt-dlp命令:")
cmd = [
    "yt-dlp",
    "--referer", "https://www.xiaohongshu.com",
    "--user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "--list-formats",
    test_url
]
print(" ".join(cmd[:6]) + " ... " + test_url)

# 尝试执行
print(f"\n尝试获取视频格式列表...")
try:
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=30
    )
    
    if result.returncode == 0:
        print("✅ 成功获取格式列表")
        print(result.stdout)
    else:
        print("❌ 获取格式列表失败")
        print("错误:", result.stderr[:500])
except Exception as e:
    print(f"❌ 执行失败: {e}")

print("\n" + "=" * 60)
