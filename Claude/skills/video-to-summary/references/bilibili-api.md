# Bilibili API Documentation

## Overview

The Bilibili API module provides official API integration for video information retrieval and download URL generation, bypassing 412 anti-crawling errors.

## API Endpoints

### Video Info API

```
GET https://api.bilibili.com/x/web-interface/view
```

**Parameters:**
- `bvid` - Video BV ID (e.g., BV12CA1zhEmK)

**Response:**
```json
{
  "code": 0,
  "data": {
    "bvid": "BV12CA1zhEmK",
    "title": "Video Title",
    "duration": 131,
    "owner": {
      "name": "UP主名称"
    }
  }
}
```

### Play URL API

```
GET https://api.bilibili.com/x/player/wbi/playurl
```

**Parameters:**
- `bvid` - Video BV ID
- `cid` - Video CID (from video info)
- `qn` - Quality (16=360P, 32=480P, 64=720P, 80=1080P)

**Response:**
```json
{
  "code": 0,
  "data": {
    "dash": {
      "video": [...],
      "audio": [...]
    }
  }
}
```

## BVID Extraction

Supports multiple URL formats:

- `https://www.bilibili.com/video/BV12CA1zhEmK`
- `https://b23.tv/hHipbJS` (short link)
- `BV12CA1zhEmK` (direct BVID)

## Rate Limiting

- No authentication required for public videos
- Recommended delay: 1 second between requests
- High-frequency requests may trigger rate limiting

## Error Handling

**Common Errors:**

- `412` - Anti-crawling triggered (use API method)
- `404` - Video not found
- `403` - Access denied (private video)

## Implementation

See `scripts/utils/bilibili_api.py` for implementation details.

### Example Usage

```python
from utils.bilibili_api import BilibiliAPI

api = BilibiliAPI()

# Extract BVID
bvid = api.extract_bvid("https://b23.tv/hHipbJS")

# Get video info
video_info = api.get_video_info(bvid)

# Get download URLs
download_info = api.get_play_url(bvid, cid, quality=80)
```

## Subtitle Support

Check for available subtitles:

```python
subtitles = api.get_subtitles(bvid, cid)
if subtitles:
    # Use existing subtitles instead of transcription
    pass
```

## Cookies (Optional)

For premium content or login-required videos:

```python
api = BilibiliAPI(cookies_path="cookies.txt")
```

Cookies file format (Netscape):
```
.bilibili.com	TRUE	/	FALSE	0	SESSDATA	xxx
.bilibili.com	TRUE	/	FALSE	0	bili_jct	xxx
```
