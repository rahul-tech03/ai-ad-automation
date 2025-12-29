import requests
import os

HEYGEN_URL = "https://api.heygen.com/v1/video.generate"
HEYGEN_API_KEY = os.getenv("HEYGEN_API_KEY")
def create_video(script_text):
    headers = {
        "Authorization": f"Bearer {HEYGEN_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "video_inputs": [
            {
                "character": "Amy",
                "voice": "en-US-Wavenet-D",
                "script": script_text,
                "background": "office"
            }
        ],
        "ratio": "9:16"
    }

    response = requests.post(HEYGEN_URL, json=payload, headers=headers)
    return response.json()
