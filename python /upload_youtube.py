import os
import google.auth
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

CLIENT_ID = os.getenv("YOUTUBE_CLIENT_ID")
CLIENT_SECRET = os.getenv("YOUTUBE_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("YOUTUBE_REFRESH_TOKEN")

def get_youtube_service():
    credentials = google.oauth2.credentials.Credentials(
        None,
        refresh_token=REFRESH_TOKEN,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        scopes=["https://www.googleapis.com/auth/youtube.upload"]
    )
    return build("youtube", "v3", credentials=credentials)

def upload_video(file_path, title, description):
    youtube = get_youtube_service()

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["brainrot", "facts", "useless facts", "shorts"]
            },
            "status": {"privacyStatus": "public"}
        },
        media_body=MediaFileUpload(file_path)
    )

    response = request.execute()
    return response

if __name__ == "__main__":
    upload_video("short.mp4", "Test Upload", "Brainrot Short Test")
