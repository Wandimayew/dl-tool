📥 DL Tool

A fast, lightweight terminal-based video downloader powered by yt-dlp with an IDM-style progress UI, smart filename detection, and flexible download controls.

✨ Features
🎬 Download videos from YouTube, TikTok, and more
📊 Real-time IDM-style progress bar
⚡ Live speed and ETA display
📁 Custom download folder support
🧠 Automatic filename detection
🎧 Audio extraction (MP3 mode)
🎯 Quality selection (360p, 720p, 1080p)
🕘 Download history tracking
⚙️ Simple and fast CLI interface
🐧 Linux optimized (tested on Parrot OS)

📦 Installation
1. Requirements

Make sure you have:

Python 3.8+
pip
ffmpeg (recommended)
Install ffmpeg (Linux)
sudo apt update
sudo apt install ffmpeg
2. Clone repository
git clone https://github.com/Wandimayew/dl-tool.git
cd dl-tool
3. Install dependencies
pip install -r requirements.txt
4. Install CLI tool globally
pip install -e .
5. Verify installation
dl --help

🚀 Usage

📥 Download video
dl <url>

Example:

dl https://www.tiktok.com/@user/video/123456

🎧 Download audio only (MP3)
dl --audio <url>

🎯 Choose video quality
dl --quality 720p <url>

📁 Download to specific folder
dl --folder <path> <url>

Example:

dl --folder ~/Videos https://youtube.com/watch?v=xxxxx
🧭 Set default download folder
dl --set-folder ~/Downloads

🕘 View download history
dl history

❓ Help
dl --help

📊 UI Preview

During download:

🎬 Funny Cat Video.mp4 | [███████████░░░░░░░░] 63.2% | 2.1MiB/s | ETA 00:01:20

⚙️ Configuration

Default settings stored in:

config.json

Example:

{
  "download_folder": "~/Downloads"
}

🧠 How it works

This tool is a lightweight wrapper around yt-dlp.

It:

Extracts video metadata
Selects best available format
Downloads and merges streams
Streams progress to a custom terminal UI

📁 Project Structure
dl-tool/
├── dl/
│   ├── cli.py
│   ├── core.py
│   ├── ui.py
│   ├── config.py
│   ├── history.py
│
├── setup.py
├── requirements.txt
├── config.json
├── README.md

🐞 Known Issues
Very short videos may skip progress animation
Some platforms may require cookies (YouTube/TikTok)
ETA may be unstable on slow networks

🚀 Roadmap
 Download queue system
 Parallel downloads
 GUI version (desktop app)
 Plugin system
 Mobile API support
 Colored terminal UI

🤝 Contributing

Pull requests are welcome.

If you want to contribute:

Improve UI rendering
Add site extractors
Optimize download performance
Fix bugs and edge cases

📜 License

MIT License — free to use, modify, and distribute.

🙌 Credits

Built with:

Python
yt-dlp engine
custom terminal UI system
