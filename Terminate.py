# terminate.py

def check_termination(command, terminate_words=None):
    if terminate_words is None:
        terminate_words = ["bye", "stop", "terminate", "exit", "goodbye", "shut down"]

    if not command:
        return False

    command = command.lower()
    for word in terminate_words:
        if word in command:
            print(f"🛑 Termination word '{word}' detected.")
            return True

    return False
