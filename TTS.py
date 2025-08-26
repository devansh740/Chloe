import requests
import pygame
import tempfile
import os
import base64

# 🔑 Your API key
API_KEY = "API_KEY"

# 🌐 Google TTS API endpoint
TTS_ENDPOINT = f"https://texttospeech.googleapis.com/v1/text:synthesize?key={API_KEY}"

# 🎵 Initialize pygame mixer
pygame.mixer.init()

def speak(text, language_code="en-US", voice_name="en-US-Studio-O", speaking_rate=1.0):
    try:
        headers = {
            "Content-Type": "application/json"
        }

        payload = {
            "input": {"text": text},
            "voice": {
                "languageCode": language_code,
                "name": voice_name
            },
            "audioConfig": {
                "audioEncoding": "MP3",
                "speakingRate": speaking_rate
            }
        }

        # 🔁 Send request to Google TTS API
        response = requests.post(TTS_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()

        audio_content = response.json()["audioContent"]
        audio_binary = base64.b64decode(audio_content)

        # 💾 Save audio to temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as out:
            temp_path = out.name
            out.write(audio_binary)

        # ▶️ Play audio using pygame
        pygame.mixer.music.load(temp_path)
        pygame.mixer.music.play()

        # ⏳ Wait until playback is finished
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        # ✅ Now it's safe to delete
        pygame.mixer.music.unload()  # <-- Explicitly unload the file first
        os.remove(temp_path)

    except Exception as e:
        print(f"❌ Error during TTS: {e}")
