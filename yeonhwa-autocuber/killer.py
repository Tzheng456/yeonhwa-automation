import keyboard

running = True

def kill():
    global running
    running = False
    
keyboard.add_hotkey('z', lambda: kill())