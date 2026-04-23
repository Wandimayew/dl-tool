import subprocess
from dl.config import load_config, save_config
from dl.history import log_download
from dl.ui import render_progress

def download(url, folder, quality="bv*+ba/b"):
    cmd = [
        "yt-dlp",
        "-f", quality,
        "--newline",
        "--progress",
        "--cookies-from-browser", "firefox",
        "--sleep-interval", "2",
        "--retries", "5",
        "-o", f"{folder}/%(title)s.%(ext)s",
        url
    ]

    print("\n📥 Download started...\n")

    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )

    for line in process.stdout:
        line = line.strip()

        # ONLY stable progress lines
        if "[download]" in line:
            render_progress(line)

    process.wait()

    print("\n\n✅ Download finished")
    log_download(url, folder)


def handle_command(args):
    config = load_config()
    folder = config["download_folder"]

    # HELP
    if args[0] in ["--help", "-h"]:
        print("""
DL TOOL

Usage:
  dl <url>
  dl --audio <url>
  dl --quality 720p <url>
  dl --folder <path> <url>
  dl --set-folder <path>
  dl history
""")
        return

    # HISTORY
    if args[0] == "history":
        from dl.history import show_history
        show_history()
        return

    # SET FOLDER
    if args[0] == "--set-folder":
        config["download_folder"] = args[1]
        save_config(config)
        print(f"✅ Folder set: {args[1]}")
        return

    # AUDIO
    if args[0] == "--audio":
        url = args[1]
        cmd = [
            "yt-dlp",
            "-x",
            "--audio-format", "mp3",
            "--newline",
            "-o", f"{folder}/%(title)s.%(ext)s",
            url
        ]

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for line in process.stdout:
            line = line.strip()

            # only process real progress lines
            if "%" in line and ("at" in line or "ETA" in line):
                render_progress(line)

        process.wait()
        log_download(url, folder)
        print("\n✅ Audio download finished")
        return

    # CUSTOM FOLDER
    if args[0] == "--folder":
        custom_folder = args[1]
        url = args[2]
        download(url, custom_folder)
        return

    # QUALITY
    if args[0] == "--quality":
        quality = f"best[height<={args[1].replace('p','')}]"
        url = args[2]
        download(url, folder, quality)
        return

    # DEFAULT
    url = args[0]
    download(url, folder)