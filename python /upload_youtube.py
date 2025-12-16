import os
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def get_youtube_service():
    token_info = json.loads(os.environ["YOUTUBE_TOKEN_JSON"])
    client_info = json.loads(os.environ["YOUTUBE_CLIENT_SECRET_JSON"])

    credentials = Credentials(
        token=token_info.get("token"),
        refresh_token=token_info.get("refresh_token"),
        token_uri=client_info["installed"]["token_uri"],
        client_id=client_info["installed"]["client_id"],
        client_secret=client_info["installed"]["client_secret"],
        scopes=SCOPES,
    )

    return build("youtube", "v3", credentials=credentials)

def upload_video(video_path, title, description):
    youtube = get_youtube_service()

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "categoryId": "22",
            },
            "status": {
                "privacyStatus": "public",
            },
        },
        media_body=MediaFileUpload(video_path, resumable=True),
    )

    response = request.execute()
    print("Uploaded video ID:", response["id"])

