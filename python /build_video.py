import subprocess
import random
import os

ASSETS_DIR = "assets/backgrounds"
FONT_PATH = "assets/fonts/Impact.ttf"

def build_video(audio_path, text, output_path):
    background = random.choice([
        f"{ASSETS_DIR}/{f}" for f in os.listdir(ASSETS_DIR)
        if f.endswith((".jpg", ".png"))
    ])

    # FFmpeg command for Shorts-style caption video
    command = [
        "ffmpeg",
        "-y",
        "-loop", "1",
        "-i", background,
        "-i", audio_path,
        "-vf",
        (
            f"scale=1080:1920, "
            f"drawtext=text='{text}':fontfile={FONT_PATH}:fontsize=64:"
            "fontcolor=white:borderw=4:x=(w-text_w)/2:y=h/2"
        ),
        "-shortest",
        output_path
    ]

    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return output_path

if __name__ == "__main__":
    build_video("output.mp3", "Test brainrot fact", "short.mp4")
