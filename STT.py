# stt.py

import speech_recognition as sr

def listen(duration=8):
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎧 Listening...")
            audio = recognizer.listen(source, timeout=duration, phrase_time_limit=duration)

        print("🔍 Recognizing with Google...")
        text = recognizer.recognize_google(audio, language="en-IN")
        print(f"📝 You said: {text}")
        return text

    except sr.WaitTimeoutError:
        print("⌛ Timeout: No speech detected.")
    except sr.UnknownValueError:
        print("❓ Could not understand the audio.")
    except sr.RequestError as e:
        print(f"⚠️ Could not request results; {e}")
    except Exception as e:
        print(f"❗ Unexpected error: {e}")
    return None
