import sys
import pygame
import time
import cv2
import numpy as np
import pyautogui
import pydirectinput
import keyboard

from assets.asset import *
from models.item import Item
# from templates.flame_templates import loadFlameTemplates
from util.image_recog import findAssetInImage, findAsset
from util.screenshot import *

delay = 0.5
log_file_name = 'greed_pendant_bonus_hist'
counter = 0
running = True
pygame.mixer.init()
sound = pygame.mixer.Sound("./resources/diablo-gold.wav")
sound.set_volume(0.5)


def context_menu_flame():
    global counter
    findAsset(GLOBAL_ANCHOR)
    pyautogui.sleep(1)
    pydirectinput.press("f9")
    qolmenu = findAsset(QOLMENU, 0.9)
    if qolmenu is not None:
        print(f"context menu opened!")
        pyautogui.click(qolmenu)
        pyautogui.sleep(delay)
        pyautogui.moveTo(qolmenu.x+250, qolmenu.y+250)
        pyautogui.sleep(delay)
        flame_npc = findAsset(FLAME_NPC, 0.9)
        if flame_npc is not None:
            print(f"opening flame npc!")
            pyautogui.click(flame_npc)
            pyautogui.sleep(delay)
            pyautogui.moveTo(flame_npc.x+250, flame_npc.y+250)
            pyautogui.sleep(delay)
            flame_type = findAsset(ETERNAL_FLAME, 0.9)
            if flame_type is not None:
                pyautogui.click(flame_type)
                pyautogui.sleep(delay)
                pyautogui.moveTo(flame_type.x+250, flame_type.y+250)
                pyautogui.sleep(delay)
                print(f"Hitting Enter")
                # Select first item as cube target
                pydirectinput.press("enter")
                pyautogui.sleep(delay)
                # Click to finish generating dialogue
                pyautogui.click(flame_npc.x-70, flame_npc.y)
                pyautogui.sleep(delay)
    else:
        print(f"Could not open cubing menu, quitting")
        file = open(f"./log/{log_file_name}.log", "a+")
        file.write(f"End of log. Cubes consumed: {counter}\n")
        file.write(f"-------------------------------------------------------\n")
        file.close()
        pygame.quit()
        sys.exit(1)


def main():
    context_menu_flame()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except NameError as e:
        print(f"{e}")