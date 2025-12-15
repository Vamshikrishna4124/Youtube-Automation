import os
import requests

ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")

# Bella voice ID (public voice)
BELLA_VOICE_ID = "EXAVITQu4vr4xnSDxMaL"

def text_to_speech(text, output_path="output.mp3"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{BELLA_VOICE_ID}"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ELEVEN_API_KEY
    }

    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.15,
            "similarity_boost": 0.85,
            "style": 0.85,
            "use_speaker_boost": True
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    with open(output_path, "wb") as f:
        f.write(response.content)

    return output_path

if __name__ == "__main__":
    text_to_speech("This is a test of Bella chaotic Gen-Z voice.")
