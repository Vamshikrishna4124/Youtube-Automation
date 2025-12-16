from generate_facts import generate_fact
from tts_voice import generate_voice
from build_video import build_video
from upload_youtube import upload_video

def main():
    print("🚀 Starting daily Brainrot pipeline")

    text = generate_fact()
    audio_path = generate_voice(text)
    video_path = build_video(audio_path)
    
    upload_video(
        video_path,
        title="Daily Brainrot 🤯",
        description=text
    )

    print("✅ Upload complete")

if __name__ == "__main__":
    main()
