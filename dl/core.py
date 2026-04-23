import os
from dl.config import load_config
from dl.history import log_download

def run(cmd):
    print(f"🚀 {cmd}")
    os.system(cmd)

def download(url, folder, quality="best"):
    cmd = f'yt-dlp -f "{quality}" -o "{folder}/%(title)s.%(ext)s" "{url}"'
    run(cmd)
    log_download(url, folder)

def handle_command(args):
    config = load_config()

    if args[0] == "--help":
        print("DL TOOL HELP...")
        return

    folder = config["download_folder"]

    if args[0] == "--set-folder":
        config["download_folder"] = args[1]
        from dl.config import save_config
        save_config(config)
        print("Folder updated")
        return

    if args[0] == "--audio":
        url = args[1]
        cmd = f'yt-dlp -x --audio-format mp3 -o "{folder}/%(title)s.%(ext)s" "{url}"'
        run(cmd)
        log_download(url, folder)
        return

    if args[0] == "--folder":
        custom_folder = args[1]
        url = args[2]
        download(url, custom_folder)
        return

    # default
    url = args[0]
    download(url, folder)