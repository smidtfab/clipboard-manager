from pynput import keyboard

# The key combination to check
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.Key.alt_l, keyboard.KeyCode(char='1')},
    {keyboard.Key.shift, keyboard.Key.alt_l, keyboard.KeyCode(char='2')},
    {keyboard.Key.shift, keyboard.Key.alt_l, keyboard.KeyCode(char='3')}
]

# The currently active modifiers
current = set()

def execute():
    print ("Do Something")

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()