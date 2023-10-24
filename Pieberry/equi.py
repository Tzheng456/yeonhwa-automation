import pyautogui
import pydirectinput
import threading
import keyboard
import sys
import random

from assets import *

running = True
sleep_time = 20.52

def search(asset, conf=0.9):
    return pyautogui.locateOnWindow(asset, "YEONHWA", confidence=conf)

def search_image():
    print(f"auto equilibrium glitcher started")
    while running:
        global sleep_time
        try:
            # Locate the image in the specified region of the screen
            x = search(EQUILIBRIUM)
            if x is not None:
                print(f"ENTERED EQUILIBRIUM, COUNTDOWN: {sleep_time} THEN CAST DOOR")
                pyautogui.sleep(sleep_time)
                print(f"CASTING DOOR NOW!")
                pydirectinput.press("n")
                print(f"CHECKING IF GLITCHED...")
                pyautogui.sleep(1)
                l = search(LIGHT)
                d = search(DARK)
                if l is not None or d is not None:
                    print(f"GLITCHING FAILED - WAITING FOR REATTEMPT...")
                    offsets = [0.01, -0.01, 0.02, -0.02]
                    offset = random.choice(offsets)
                    sleep_time += offset
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