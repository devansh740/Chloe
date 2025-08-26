# wake.py
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import tempfile
import os
from faster_whisper import WhisperModel

# Load the tiny model on GPU
model = WhisperModel("tiny", device="cuda", compute_type="float16")

def record_audio(duration=3, fs=16000):
    print("🎤 Say something to activate...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    write(temp_wav.name, fs, recording)
    return temp_wav.name

def detect_wake_word(wake_words=None):
    if wake_words is None:
        wake_words = ["hi", "hello", "chloe"]

    audio_path = record_audio()

    try:
        print("🔍 Transcribing...")
        segments, _ = model.transcribe(audio_path)
        text = " ".join([seg.text for seg in segments]).lower()
        print(f"📝 You said: {text}")

        for word in wake_words:
            if word in text:
                print(f"🧠 Wake word '{word}' detected!")
                os.remove(audio_path)
                return True

        print("❌ No wake word found.")
        os.remove(audio_path)
        return False

    except Exception as e:
        print(f"🚫 Error during transcription: {e}")
        os.remove(audio_path)
        return False

# Run once for testing
if __name__ == "__main__":
    detect_wake_word()
