import os

HISTORY_FILE = "dl_history.log"

def log_download(url, folder):
    with open(HISTORY_FILE, "a") as f:
        f.write(f"{url} -> {folder}\n")

def show_history():
    if not os.path.exists(HISTORY_FILE):
        print("No history yet.")
        return
    print(open(HISTORY_FILE).read())