---
layout: default
title: Nautilus Duration Column
---

# 🎥 Nautilus Duration Column

![Demo](https://raw.githubusercontent.com/Trancenotist/nautilus-media-duration-column/main/screenshots/2.png)
![Demo](https://raw.githubusercontent.com/Trancenotist/nautilus-media-duration-column/main/screenshots/3.png)


## One-Click Install
```bash
sudo apt update && sudo apt install ffmpeg python3-nautilus -y
mkdir -p ~/.local/share/nautilus-python/extensions
wget https://raw.githubusercontent.com/Trancenotist/nautilus-media-duration-column/main/duration-column.py -O ~/.local/share/nautilus-python/extensions/duration-column.py
chmod +x ~/.local/share/nautilus-python/extensions/duration-column.py
nautilus -q
```

[Full Documentation](https://github.com/Trancenotist/nautilus-media-duration-column)


## FAQ

### Why is the column not showing up?
- Restart Nautilus: `nautilus -q`
- Ensure the script is in `~/.local/share/nautilus-python/extensions/`
