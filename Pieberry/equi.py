import pyautogui
import pydirectinput
import threading
import keyboard
import sys

from assets import *

running = True

def search(asset, conf=0.9):
    return pyautogui.locateOnWindow(asset, "YEONHWA", confidence=conf)

def search_image():
    while running:
        try:
            # Locate the image in the specified region of the screen
            x = search(EQUILIBRIUM)
            if x is not None:
                print(f"ENTERED EQUILIBRIUM, COUNTDOWN THEN CAST DOOR")
                pyautogui.sleep(20.48)
                pydirectinput.press("n")
                pyautogui.sleep(1)
                l = search(LIGHT)
                d = search(DARK)
                if l is not None or d is not None:
                    pass
                else:
                    g = search(GLITCHED)
                    if g is not None:
                        print(f"Success! Glitched, quitting")
                        sys.exit(0)
        except Exception as e:
            print("Error:", e)

def main():
    def kill():
        global running
        running = False
    keyboard.add_hotkey('z', lambda: kill())
    # Create a thread for the image search
    image_search_thread = threading.Thread(target=search_image)
    
    # Start the thread
    image_search_thread.start()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass