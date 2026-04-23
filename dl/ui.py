import re
import sys

BAR_LENGTH = 20
current_title = None


def set_title(line):
    global current_title

    # ✅ correct yt-dlp format
    match = re.search(r"\[download\]\sDestination:\s(.+)", line)

    if match:
        full_path = match.group(1).strip()
        current_title = full_path.split("/")[-1]


def format_bar(percent):
    filled = int(BAR_LENGTH * percent / 100)
    return "█" * filled + "░" * (BAR_LENGTH - filled)


def render_progress(line):
    global current_title

    set_title(line)

    percent_match = re.search(r'(\d+\.?\d*)%', line)
    speed_match = re.search(r'at\s+([0-9\.]+[A-Za-z/]+)', line)
    eta_match = re.search(r'ETA\s+([0-9:?\-]+)', line)

    if not percent_match:
        return

    percent = float(percent_match.group(1))
    speed = speed_match.group(1) if speed_match else "?"
    eta = eta_match.group(1) if eta_match else "?"

    bar = format_bar(percent)
    title = current_title or "Downloading..."

    sys.stdout.write("\r\033[K")
    sys.stdout.write(
        f"🎬 {title} | [{bar}] {percent:.1f}% | {speed} | ETA {eta}"
    )
    sys.stdout.flush()