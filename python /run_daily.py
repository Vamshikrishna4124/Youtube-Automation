from .generate_facts import generate_fact
from .tts_voice import generate_voice
from .build_video import build_video
from .upload_youtube import upload_video


def main():
    print("🚀 Starting Daily Brainrot Pipeline")

    text = generate_fact()
    print("🧠 Fact generated:", text)

    audio_path = generate_voice(text)
    print("🔊 Voice generated:", audio_path)

    video_path = build_video(audio_path)
    print("🎬 Video built:", video_path)

    upload_video(
        video_path=video_path,
        title="Daily Brainrot 🤯",
        description=text
    )

    print("✅ Upload complete")


if __name__ == "__main__":
    main()
