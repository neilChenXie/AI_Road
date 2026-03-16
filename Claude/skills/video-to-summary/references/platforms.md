# Platform Support Matrix

## Supported Platforms

### Bilibili (B站)

**Status:** ✅ Fully Supported

**Features:**
- Official API integration
- 412 error bypass
- Short link support (b23.tv)
- Video info retrieval
- Direct download URLs
- Subtitle support

**Requirements:**
- No authentication for public videos
- Optional cookies for premium content

**Recommended Method:**
```bash
python scripts/video_to_summary.py --url "BILIBILI_URL" --use-api
```

---

### YouTube

**Status:** ✅ Supported via yt-dlp

**Features:**
- Video download
- Audio extraction
- Subtitle extraction
- Multiple quality options

**Requirements:**
- yt-dlp installed
- Cookies for age-restricted content

**Usage:**
```bash
python scripts/video_to_summary.py --url "YOUTUBE_URL"
```

**With Cookies:**
```bash
python scripts/video_to_summary.py --url "YOUTUBE_URL" --cookies cookies.txt
```

---

### TikTok

**Status:** ✅ Supported via yt-dlp

**Features:**
- Video download
- Audio extraction

**Requirements:**
- yt-dlp installed

**Usage:**
```bash
python scripts/video_to_summary.py --url "TIKTOK_URL"
```

---

### Twitter/X

**Status:** ✅ Supported via yt-dlp

**Features:**
- Video download from tweets
- Audio extraction

**Requirements:**
- yt-dlp installed

**Usage:**
```bash
python scripts/video_to_summary.py --url "TWITTER_URL"
```

---

### Other Platforms

**Status:** ✅ Supported via yt-dlp

**Supported:**
- Vimeo
- Facebook
- Instagram
- Reddit
- And 1000+ other sites

**Check Support:**
```bash
yt-dlp --list-extractors | grep PLATFORM_NAME
```

## Platform Detection

Automatic platform detection:

```python
from utils.platform_detector import detect_platform

platform = detect_platform("https://b23.tv/xxx")
# Returns: "bilibili"
```

## API Support Matrix

| Platform | API Support | Auth Required | Rate Limit | Notes |
|----------|-------------|---------------|------------|-------|
| Bilibili | ✅ Yes | ❌ No | Yes | Official API, bypasses 412 |
| YouTube | ❌ No | Optional | Yes | Use cookies for restricted |
| TikTok | ❌ No | ❌ No | Yes | Via yt-dlp |
| Twitter | ❌ No | Optional | Yes | Via yt-dlp |

## Quality Options

### Bilibili

| Quality | Code | Resolution |
|---------|------|------------|
| 1080P+ | 112 | 1080P High Bitrate |
| 1080P | 80 | 1080P |
| 720P | 64 | 720P |
| 480P | 32 | 480P |
| 360P | 16 | 360P |

### YouTube

| Quality | Format |
|---------|--------|
| 4K | 2160p |
| 1080P | 1080p |
| 720P | 720p |
| 480P | 480p |

## Troubleshooting by Platform

### Bilibili

**412 Error:**
- Use `--use-api` flag
- API method bypasses anti-crawling

**Private Video:**
- Not supported
- Requires video owner to make public

**Region Locked:**
- May require VPN
- Or use cookies from that region

### YouTube

**Age-Restricted:**
- Use cookies: `--cookies cookies.txt`
- Export cookies from browser

**Region Locked:**
- Use VPN
- Or proxy configuration

### TikTok

**Private Account:**
- Not supported
- Videos must be public

**Watermark:**
- yt-dlp removes watermark by default
- Use `--no-remove-watermark` to keep

## Cookie Configuration

### Export Cookies

Use browser extension:
- Chrome: "Get cookies.txt LOCALLY"
- Firefox: "cookies.txt"

### Cookie File Format

Netscape format:
```
.domain.com	TRUE	/	FALSE	0	cookie_name	cookie_value
```

### Usage

```bash
python scripts/video_to_summary.py --url "URL" --cookies cookies.txt
```

## Proxy Configuration

For region-locked content:

```bash
export HTTP_PROXY="http://proxy:port"
export HTTPS_PROXY="http://proxy:port"

python scripts/video_to_summary.py --url "URL"
```
