#Play.py

import pywhatkit as kit
import sys
from TTS import speak

def play_song_on_youtube(song_name: str):
    try:
        if not song_name:
            print("⚠️ No song name provided.")
            return

        print(f"🔎 Searching and playing: {song_name}")
        kit.playonyt(song_name)  # This opens YouTube and plays the top result

    except Exception as e:
        speak(f"❌ Failed to play song: {e}")
