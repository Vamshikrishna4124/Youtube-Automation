from generate_facts import generate_facts
from tts_voice import text_to_speech
from build_video import build_video
from upload_youtube import upload_video
import random
import time

def run():
    facts = generate_facts()
    selected = random.sample(facts, 5)

    for i, fact in enumerate(selected):
        print(f"[+] Creating short {i+1}/5 → {fact}")

        audio = text_to_speech(fact, f"audio_{i}.mp3")
        video = build_video(audio, fact, f"short_{i}.mp4")

        upload_video(video, fact, "Daily Brainrot Fact")

        print("[✔] Uploaded successfully")
        time.sleep(5)  # space uploads

if __name__ == "__main__":
    run()
