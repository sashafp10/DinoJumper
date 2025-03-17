# keyboard_listener.py
from pynput import keyboard

class KeyboardListener:

    def __init__(self):
        self._exit_requested = False

    def on_key_press(self, key):
        try:
            # Check if 'ESC' key is pressed
            if key == keyboard.Key.esc:
                self._exit_requested = True
                return False  # Stop listener
        except Exception as ex:
            print(f"Error: {ex}")

    def start_listening(self):
        # Listen to key presses in a separate thread
        with keyboard.Listener(on_press=self.on_key_press) as listener:
            listener.join()