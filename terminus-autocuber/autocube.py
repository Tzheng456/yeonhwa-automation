import sys
import pygame
import time
import cv2
import numpy as np
import pyautogui
import pydirectinput
import keyboard
import re
import os

from assets.asset import *
from models.item import Item
from templates.cube_templates import loadPotentialTemplates
from util.image_recog import findAllMatchedStatsInImage, findAsset
from util.screenshot import *

delay = 0
log_file_name = 'greed_pendant_bonus_hist'
counter = 0
running = True
pygame.mixer.init()
sound = pygame.mixer.Sound("./resources/diablo-gold.wav")
sound.set_volume(1)
global_anchor = findAsset(GLOBAL_ANCHOR)


def open_cuber():
    global global_anchor, counter
    pyautogui.sleep(1)
    pydirectinput.press("enter")
    pyautogui.typewrite("@check")
    pydirectinput.press("enter")
    pyautogui.typewrite("@cube")
    pydirectinput.press("enter")
    pyautogui.sleep(delay)
    pydirectinput.press("enter")
    pyautogui.sleep(delay)
    pydirectinput.press("enter")
    pyautogui.sleep(delay)
    # at before & after page
    if BEFORE is not None:
        print(f"cube menu opened!")
    else:
        print(f"Could not open cubing menu, quitting")
        file = open(f"./log/{log_file_name}.log", "a+")
        file.write(f"End of log. Cubes consumed: {counter}\n")
        file.write(f"-------------------------------------------------------\n")
        file.close()
        pygame.quit()
        sys.exit(1)


def generate_cube_result():
    create_cube_result()


def update_cache_item(templates, item, cube_result_asset):
    print(f"cache: clearing item, updating item")
    item.clear_stats()
    # read cube results
    cube_results = cv2.imread(cube_result_asset)
    
    # multi templates matching against each stat
    # item updated with stats
    for potential_name in templates.keys():
        matched_stats = findAllMatchedStatsInImage(templates[potential_name], cube_results, potential_name)
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
        pattern = r'_(.*?)\.png'
        prefix = re.search(pattern, CUBE_RESULT_AFTER).group(1)
        file.write(f"{prefix}: {item_stats}\n\n")
        file.write(f"*------------------------------------------------------\n")
    file.close()


def stat_matching(item, target_stats):
    global global_anchor, counter, sound
    for stat in target_stats.keys():
        val = target_stats[stat]
        if getattr(item, f'get_{stat}')() >= val:
            print(
                f"Item has met target of {stat}: {val} after {counter} cubes!")
            sound.play()
            time.sleep(sound.get_length())
            return True
    return False


def match_all_stats(item, target_stats):
    for target_stat in target_stats:
        print(f"Checking against: {target_stat}")
        matched = []
        for stat in target_stat.keys():
            val = target_stat[stat]
            curr_stat = getattr(item, f'get_{stat}')()
            _ = curr_stat >= val
            matched.append(_)
        if all(matched):
            print(
                f"Item has met target of {target_stat} after {counter} cubes!")
            sound.play()
            time.sleep(sound.get_length())
            return True
    return False


def proceed_cubing(continue_asset):
    global global_anchor, counter
    try:
        retry = findAsset(continue_asset, 0.85, log=True)
        pyautogui.click(retry)
        pyautogui.moveTo(global_anchor)
        print(f"Recubing!")
        counter += 1
        return True  # (recube)
    except:
        print(f"Could not find confirm NPC dialogue!")
        print(f"Could not begin cubing, aborting.")
        pygame.quit()
        sys.exit(1)


def end_chat(msg="Aborting!"):
    try:
        pyautogui.sleep(1)
        end = findAsset(END_CHAT, 0.98, log=False)
        pyautogui.click(end)
        print(f"{msg}")
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


def clear_temp():
    temp = [CUBE_RESULT_AFTER, CUBE_RESULT_BEFORE]
    print(f"Clearing temp!")
    for _ in temp:
        if os.path.exists(_):
            os.remove(_)


def recube(templates, item_before, item_after, target_stats, initial=False):
    global global_anchor, counter
    clear_temp()
    sleep(0.25)
    generate_cube_result()
    update_cache_item(templates, item_before, CUBE_RESULT_BEFORE)
    update_cache_item(templates, item_after, CUBE_RESULT_AFTER)
    print(f"Looking for any of: {target_stats}")
    print(f"\nItem current stats: ")
    print(item_before.to_string())
    print(f"\nItem new stats: ")
    print(item_after.to_string())
    print(f"\nCubes used: {counter}")
    matched_after = match_all_stats(item_after, target_stats)
    # matched target_stats, prompt user if want to recube anyways (y/n)
    if initial:
        matched_before = match_all_stats(item_before, target_stats)
        if matched_before:
            prompt = input(
                f"A target stat was found in before stats using {counter} cubes, recube anyways? (y/n): ")
            if prompt.lower() == 'y':
                pyautogui.sleep(1)
                print(f"trying to proceed cubing with asset: {BEFORE}")
                return proceed_cubing(BEFORE)
            else:
                end_chat()
                sys.exit(0)
        else:
            # input("waiting")
            pyautogui.sleep(delay)
            return proceed_cubing(BEFORE)
    elif matched_after:
        prompt = input(
            f"Target stat found in before and after in: {counter} cubes! (1 - take before, 2 - take after, 3 - recube): ")
        if prompt.lower() == '1':
            end_chat(msg="Taking before stats!")
            sys.exit(0)
        elif prompt.lower() == '2':
            after = findAsset(AFTER)
            if after is not None:
                pyautogui.click(after)
                pyautogui.moveTo(global_anchor)
                pyautogui.sleep(delay)
                print(f"Taking after stats!")
                file = open(f"./log/{log_file_name}.log", "a+")
                file.write(f"End of log. Cubes consumed: {counter}\n")
                file.write(
                    f"-------------------------------------------------------\n")
                file.close()
                return False
        elif prompt.lower() == '3':
            pyautogui.sleep(delay)
            return proceed_cubing(BEFORE)
        else:
            end_chat()
            sys.exit(0)
    else:
        # input("waiting")
        pyautogui.sleep(delay)
        return proceed_cubing(BEFORE)


def main():
    global global_anchor, counter
    # init
    def kill():
        global global_anchor, running
        running = False
    clear_temp()
    keyboard.add_hotkey('z', lambda: kill())
    templates = loadPotentialTemplates()
    item_before = Item()
    item_after = Item()
    target_stats = [{"basemeso": 20, "basedrop": 20}, {"basemeso": 21}, {"basedrop": 21}, {"basedex": 33}, {"baseint": 33}, {"basestr": 33}, {"baseluk": 33}]
    cube_limit = 2000
    open_cuber()
    # check if stats on item already meet target_stats
    should_recube = recube(templates, item_before, item_after, target_stats, True)
    try:
        while should_recube and running:
            if counter > cube_limit:
                end_chat()
                sys.exit(0)
            should_recube = recube(templates, item_before, item_after, target_stats)
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
