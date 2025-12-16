import os
import json
import tempfile
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def get_youtube_service():
    # Load secrets from GitHub Actions env
    client_secret = json.loads(os.environ["YOUTUBE_CLIENT_SECRET_JSON"])
    token_data = json.loads(os.environ["YOUTUBE_TOKEN_JSON"])

    credentials = Credentials(
        token=token_data["access_token"],
        refresh_token=token_data["refresh_token"],
        token_uri=token_data["token_uri"],
        client_id=token_data["client_id"],
        client_secret=token_data["client_secret"],
        scopes=SCOPES,
    )

    return build("youtube", "v3", credentials=credentials)


def upload_video():
    youtube = get_youtube_service()

    video_path = "short.mp4"

    if not os.path.exists(video_path):
        raise FileNotFoundError("short.mp4 not found")

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": "Daily Brainrot Short 🤯",
                "description": "Automated YouTube Short upload",
                "categoryId": "22"
            },
            "status": {
                "privacyStatus": "public"
            },
        },
        media_body=MediaFileUpload(video_path, resumable=True),
    )

    response = request.execute()
    print("✅ Uploaded video ID:", response["id"])


if __name__ == "__main__":
    upload_video()
