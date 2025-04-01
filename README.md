# Ubuntu Nautilus Media Duration Column 🎥

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub Release](https://img.shields.io/github/v/release/Trancenotist/nautilus-media-duration-column)](https://github.com/Trancenotist/nautilus-media-duration-column/releases)

Adds a **duration column** to Nautilus File Manager for videos/audio files, just like Windows!

![Demo Screenshot](https://github.com/Trancenotist/nautilus-media-duration-column/blob/main/screenshots/2.png)![Demo Screenshot](https://github.com/Trancenotist/nautilus-media-duration-column/blob/main/screenshots/3.png)<!-- Add a screenshot later -->

## Features ✨
- 🕒 Persistent caching (no rescanning!)
- ⚙️ Customize supported formats (MP4, MKV, etc.)
- 🛠️ Easy install with copy-paste commands

## Works On: Ubuntu 20.04+, Debian 11+, and other GNOME-based distros.

## Installation 🚀
```bash
sudo apt update && sudo apt install ffmpeg python3-nautilus -y
mkdir -p ~/.local/share/nautilus-python/extensions
wget https://raw.githubusercontent.com/Trancenotist/nautilus-media-duration-column/main/duration-column.py -O ~/.local/share/nautilus-python/extensions/duration-column.py
chmod +x ~/.local/share/nautilus-python/extensions/duration-column.py
nautilus -q
```

## Customization 🔧
Edit the `SUPPORTED_EXTENSIONS` list in the script to add more file types:
```python
SUPPORTED_EXTENSIONS = {'.mp4', '.mkv', '.your-format-here'}
```

## Troubleshooting 🔍
| Issue | Fix |
|-------|-----|
| Column not showing | Restart Nautilus: `nautilus -q` |
| "Timeout" errors | Increase `FFPROBE_TIMEOUT` in the script |

**Need help?** [Open an issue](https://github.com/Trancenotist/nautilus-media-duration-column/issues)!
