from python.generate_facts import generate_fact
from python.tts_voice import generate_voice
from python.build_video import build_video
from python.upload_youtube import upload_video


def main():
    print("🚀 Starting Daily Brainrot pipeline")

    # 1. Generate text
    text = generate_fact()
    print("🧠 Fact generated")

    # 2. Generate voice
    audio_path = generate_voice(text)
    print(f"🔊 Audio created: {audio_path}")

    # 3. Build video
    video_path = build_video(audio_path)
    print(f"🎬 Video created: {video_path}")

    # 4. Upload to YouTube
    upload_video(
        video_path=video_path,
        title="Daily Brainrot 🤯",
        description=text
    )

    print("✅ Upload complete")


if __name__ == "__main__":
    main()
