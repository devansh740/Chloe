# main.py
import asyncio
from wake import detect_wake_word
from STT import listen
from TTS import speak
from Terminate import check_termination
from Think import process_command
from Play import play_song_on_youtube

def main():
    print("🤖 AI Assistant initialized...")
    c=1
    while True:

        if c==1:
                speak("how can I help you?")
                c=0
            # Speech-to-text
        command = listen()

        if not command:
            speak("I didn't catch that. Please repeat.")
            continue

        print(f"🧠 Command received: {command}")
        if "play" in command or "song" in command:
            song_name = command.replace("play", "").replace("song", "").strip()
            speak(f"Playing {song_name} on YouTube 🎶")
            play_song_on_youtube(song_name)
            return None

        # Termination check
        elif check_termination(command):
            speak("Goodbye. Have a great day!")
            break
        else:
        # AI processing using Think (Groq)
            response = process_command(command)
            print(f"🤖 Response: {response}")
            speak(response)

if __name__ == "__main__":
    main()

