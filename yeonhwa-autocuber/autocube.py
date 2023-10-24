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
from templates.cube_templates import loadPotentialTemplates
from util.image_recog import findAllMatchedStatsInImage, findAsset
from util.screenshot import *

delay = 0.2
log_file_name = 'greed_pendant_bonus_hist'
counter = 0
running = True
pygame.mixer.init()
sound = pygame.mixer.Sound("./resources/diablo-gold.wav")
sound.set_volume(0.5)


def context_menu_cube():
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
        cuber = findAsset(CUBER, 0.9)
        if cuber is not None:
            print(f"opening cuber npc!")
            pyautogui.click(cuber)
            pyautogui.sleep(delay)
            pyautogui.moveTo(cuber.x+250, cuber.y+250)
            pyautogui.sleep(delay)
            print(f"Hitting Enter")
            # Select first item as cube target
            pydirectinput.press("enter")
            pyautogui.sleep(delay)
            # Click to finish generating dialogue
            pyautogui.click(cuber.x-50, cuber.y)
            pyautogui.sleep(delay)
            # On cube selection page -> scroll down to cube select menu
            down = findAsset(DOWN, 0.9)
            if down is not None:
                print(f"Scrolling down")
                pyautogui.click(down, clicks=50)
                pyautogui.sleep(delay)
    else:
        print(f"Could not open cubing menu, quitting")
        file = open(f"./log/{log_file_name}.log", "a+")
        file.write(f"End of log. Cubes consumed: {counter}\n")
        file.write(f"-------------------------------------------------------\n")
        file.close()
        pygame.quit()
        sys.exit(1)


def select_cube(cube):
    asset = cube["type"]
    cube_asset = findAsset(asset, 0.85)
    if cube is not None:
        print(f"Selecting cube")
        pyautogui.click(cube_asset)
        pyautogui.sleep(delay)
        print(f"reposition mouse!")
        pyautogui.click(cube_asset.x - 120, cube_asset.y)
        pyautogui.sleep(delay)
    else:
        print(f"cube not found!")


def generate_cube_result(cube, initial):
    if initial:
        create_cube_result(cube["init_anchor"])
    else:
        create_cube_result(cube["anchor"])


def update_cache_item(all_templates, item, cube):
    print(f"cache: clearing item, updating item")
    item.clear_stats()
    # read cube results
    cube_result = cv2.imread(CUBE_RESULT)
    # template choice (based on cube type) base or bonus templates
    cube_type = cube["type"]
    if "redcube" in cube_type or "blackcube" in cube_type:
        # base templates
        templates = all_templates[0]
    else:
        # bonus templates
        templates = all_templates[1]
    # multi templates matching against each stat
    # item updated with stats
    for potential_name in templates.keys():
        matched_stats = findAllMatchedStatsInImage(
            templates[potential_name], cube_result, potential_name)
        if len(matched_stats) > 0:
            for matched_stat in matched_stats:
                line_type, stat, val = potential_name.split("_")
                prefix = line_type+stat
                item_get = getattr(item, f'get_{prefix}')
                item_set = getattr(item, f'set_{prefix}')
                item_add = getattr(item, f'add_{prefix}')
                item_add(val)
    item_stats = item.to_string()
    file = open(f"./log/{log_file_name}.log", "a+")
    if len(item_stats) > 0:
        file.write(f"{item_stats}\n\n")
        file.write(f"*------------------------------------------------------\n")
    file.close()


def stat_matching(item, target_stats):
    global counter, sound
    for stat in target_stats.keys():
        val = target_stats[stat]
        if getattr(item, f'get_{stat}')() >= val:
            print(
                f"Item has met target of {stat}: {val} after {counter} tries!")
            sound.play()
            time.sleep(sound.get_length())
            return True
    return False


def proceed_cubing(continue_asset):
    global counter
    try:
        retry = findAsset(continue_asset, 0.85, log=True)
        pyautogui.click(retry)
        pyautogui.moveTo(retry.x+50, retry.y+50)
        pyautogui.sleep(delay)
        print(f"recubing!")
        counter += 1
        return True  # (recube)
    except:
        print(f"Could not find confirm NPC dialogue!")
        print(f"Could not begin cubing, aborting.")
        pygame.quit()
        sys.exit(1)


def recube(all_templates, item, cube, target_stats, initial):
    global counter
    print(f"recubing! initial: {initial}")
    generate_cube_result(cube, initial)
    update_cache_item(all_templates, item, cube)
    print(f"Looking for any of: {target_stats}")
    print(f"\nItem current stats: ")
    print(item.to_string())
    print(f"Cubes used: {counter}")
    matched = stat_matching(item, target_stats)
    if initial:
        continue_asset = CONFIRM
    else:
        continue_asset = NEXT
    # matched target_stats, prompt user if want to recube anyways (y/n)
    if matched:
        prompt = input(
            f"A target stat was already met after {counter} tries, recube anyways? (y/n): ")
        if prompt.lower() == 'y':
            pyautogui.sleep(1)
            print(f"trying to proceed cubing with asset: {continue_asset}")
            return proceed_cubing(continue_asset)
        else:
            try:
                pyautogui.sleep(1)
                end = findAsset(END_CHAT, log=False)
                pyautogui.click(end)
                print("aborting!")
                file = open(f"./log/{log_file_name}.log", "a+")
                file.write(f"End of log. Cubes consumed: {counter}\n")
                file.write(
                    f"-------------------------------------------------------\n")
                file.close()
                return False  # stop recubing
            except:
                print(f"Could not abort NPC dialogue!")
                file = open(f"./log/{log_file_name}.log", "a+")
                file.write(f"End of log. Cubes consumed: {counter}\n")
                file.write(
                    f"-------------------------------------------------------\n")
                file.close()
                pygame.quit()
                sys.exit(1)
    else:
        # pyautogui.sleep(delay)
        return proceed_cubing(continue_asset)


def main():
    # init
    def kill():
        global running
        running = False
    keyboard.add_hotkey('z', lambda: kill())
    all_templates = loadPotentialTemplates()
    item = Item()
    global counter

    # config
    RED_CUBE_CONFIG = {"type": RED_CUBE, "anchor": RED_CUBE_ANCHOR,
                       "init_anchor": RED_CUBE_ANCHOR_INITIAL}
    BONUS_CUBE_CONFIG = {"type": BONUS_CUBE, "anchor": BONUS_CUBE_ANCHOR,
                         "init_anchor": BONUS_CUBE_ANCHOR_INITIAL}
    # cube = RED_CUBE_CONFIG
    cube = BONUS_CUBE_CONFIG
    # target_stats = {"baseint": 25, "basestr": 31, "basedex": 31, "baseluk": 31, "basemeso": 40, "basedrop": 40}
    # target_stats = {"baseluk": 25, "basemeso": 40, "basedrop": 40}
    # target_stats = {"basemeso": 40}
    # target_stats = {"baseluk": 5}
    target_stats = {"bonusmatt": 25}
    # target_stats = {"bonusint": 11, "bonusintperlevel": 4}
    cube_limit = 2000
    # initial run
    # talk_to_npc()  # includes selecting item to cube step
    context_menu_cube()
    # initial cube selection step -> produces item's initial stat as cuberesult.png
    select_cube(cube)
    should_recube = recube(all_templates, item, cube, target_stats, True)
    try:
        while should_recube and running:
            if counter > cube_limit:
                print(f"Counter reached cube limit: {cube_limit}")
                end = findAsset(END_CHAT, log=False)
                pyautogui.click(end)
                print("aborting!")
                file = open(f"./log/{log_file_name}.log", "a+")
                file.write(f"End of log. Cubes consumed: {counter}\n")
                file.write(
                    f"-------------------------------------------------------\n")
                file.close()
                sys.exit(0)
            should_recube = recube(all_templates, item,
                                   cube, target_stats, False)
            file = open(f"./log/{log_file_name}.log", "a+")
            file.write(
                f"*------------------------------------------------------\n")
            file.close()
    except KeyboardInterrupt:
        file = open(f"./log/{log_file_name}.log", "a+")
        file.write(f"End of log. Cubes consumed: {counter}\n")
        file.write(f"-------------------------------------------------------\n")
        file.close()
        pass
    pygame.quit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    except NameError as e:
        print(f"{e}")
