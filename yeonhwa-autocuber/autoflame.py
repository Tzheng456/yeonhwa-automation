import sys
import pygame
import time
import cv2
import numpy as np
import pyautogui
import pydirectinput
import keyboard

from assets.asset import *
from models.flame import Flame
from templates.flame_templates import loadFlameTemplates
from util.flames_ident import get_lines
from util.image_recog import findAsset
from util.screenshot import *

delay = 1.5
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


def stat_matching(flame, target_stats):
    global counter, sound
    for stat in target_stats.keys():
        val = target_stats[stat]
        if getattr(flame, f"get_{stat}")() >= val:
            print(
                f"Flame has met target of {stat}: {val} after {counter} tries!")
            sound.play()
            time.sleep(sound.get_length())
            return True
    return False


def flame_score(flame, flame_config):
    prim_sec_dict = {
        "flame_str": "flame_dex",
        "flame_dex": "flame_str",
        "flame_int": "flame_luk",
        "flame_luk": "flame_int",
    }
    primary, attack_type = flame_config
    secondary = prim_sec_dict[primary]
    score = 0
    stats = flame.get_stats()

    for stat in stats:
        get = getattr(flame, f"get_{stat}")
        stat_val = get()
        if stat == primary:
            score += stat_val * 1
        if stat == secondary:
            score += stat_val * 0.125
        if stat == attack_type:
            score += stat_val * 4
        if stat == "flame_allstat":
            score += stat_val * 10

    return score

def main():
    def kill():
        global running
        running = False
    keyboard.add_hotkey('z', lambda: kill())
    flame_result = cv2.imread(FLAME_RESULT)
    all_templates = loadFlameTemplates()
    is_wep = False
    min_flame_score = 120
    flame_config = ["flame_luk", "flame_att"]
    flame = Flame()
    get_lines(all_templates, flame, flame_result, is_wep)
    print(f"CURRENT STATS:\n{flame.to_string()}")

def main1():
    def kill():
        global running
        running = False
    keyboard.add_hotkey('z', lambda: kill())
    all_templates = loadFlameTemplates()
    is_wep = False
    min_flame_score = 120
    flame_config = ["flame_luk", "flame_att"]
    flame = Flame()
    context_menu_flame()

    while running:
        create_flame_result()
        pyautogui.sleep(delay)
        flame_result = cv2.imread(FLAME_RESULT)
        get_lines(all_templates, flame, flame_result, is_wep)
        print(f"CURRENT STATS:\n{flame.to_string()}")
        current_score = current_score(flame,flame_config)
        print(f"CURRENT SCORE: {current_score}")
        if current_score >= min_flame_score:
            prompt = input(f"SCORE THRESHOLD: {min_flame_score} ACHIEVED, reflame anyways? (y/n)")
            if prompt.lower() == 'y':
                pyautogui.sleep(1)
                reflame = findAsset(REFLAME, 0.9)
                if reflame is not None:
                    pyautogui.click(reflame)
                    pyautogui.moveTo(reflame.x + 200, reflame.y + 200)
                    pyautogui.sleep(delay)
            else:
                try:
                    pyautogui.sleep(1)
                    end = findAsset(STOP_FLAME, log=False)
                    pyautogui.click(end)
                    print("aborting!")
                    file = open(f"./log/{log_file_name}.log", "a+")
                    file.write(f"End of log. Cubes consumed: {counter}\n")
                    file.write(
                        f"-------------------------------------------------------\n")
                    file.close()
                except:
                    print(f"Could not abort NPC dialogue!")
                    file = open(f"./log/{log_file_name}.log", "a+")
                    file.write(f"End of log. Cubes consumed: {counter}\n")
                    file.write(
                        f"-------------------------------------------------------\n")
                    file.close()
                    pygame.quit()
                    sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except NameError as e:
        print(f"{e}")
