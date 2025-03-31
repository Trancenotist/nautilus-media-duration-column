import os
import subprocess
import time
import json
from pathlib import Path
from urllib.parse import unquote
from gi.repository import GObject, Nautilus
from typing import List, Set, Dict

# ===== CONFIGURATION =====
SUPPORTED_EXTENSIONS = {'.mp4', '.mkv', '.avi', '.mov', '.webm', '.mp3', '.flac', '.wav', '.ogg'}
CACHE_FILE = Path.home() / ".cache" / "nautilus-media-durations.json"  # Persistent cache location
CACHE_EXPIRE_DAYS = 7  # Remove entries older than X days
FFPROBE_TIMEOUT = 5
# ========================

class DiskCache:
    def __init__(self):
        self.cache = self._load_cache()
        self._prune_old_entries()

    def _load_cache(self) -> Dict[str, str]:
        try:
            with open(CACHE_FILE, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_cache(self):
        CACHE_FILE.parent.mkdir(exist_ok=True, parents=True)
        with open(CACHE_FILE, 'w') as f:
            json.dump(self.cache, f)

    def _prune_old_entries(self):
        now = time.time()
        self.cache = {
            path: data
            for path, data in self.cache.items()
            if (now - data['timestamp']) < (CACHE_EXPIRE_DAYS * 86400)
        }
        self._save_cache()

    def get(self, path: str) -> str | None:
        data = self.cache.get(path)
        if data and (time.time() - data['timestamp']) < (CACHE_EXPIRE_DAYS * 86400):
            return data['duration']
        return None

    def set(self, path: str, duration: str):
        self.cache[path] = {
            'duration': duration,
            'timestamp': time.time(),
            'mtime': os.path.getmtime(path)  # Track file modification time
        }
        self._save_cache()

class DurationColumnExtension(GObject.GObject, Nautilus.ColumnProvider, Nautilus.InfoProvider):
    def __init__(self):
        super().__init__()
        self.cache = DiskCache()

    # ... [Keep get_columns() and format_duration() unchanged from previous script] ...

    def update_file_info(self, file: Nautilus.FileInfo) -> None:
        if file.get_uri_scheme() != "file":
            return

        path = unquote(file.get_uri()[7:])
        ext = os.path.splitext(path)[1].lower()

        if ext not in SUPPORTED_EXTENSIONS:
            return

        # Check if file has been modified since last cache
        cached = self.cache.get(path)
        if cached and os.path.exists(path):
            current_mtime = os.path.getmtime(path)
            if cached['mtime'] == current_mtime:
                file.add_string_attribute("duration", cached['duration'])
                return

        # ... [Keep ffprobe logic from previous script, then call self.cache.set()] ...
