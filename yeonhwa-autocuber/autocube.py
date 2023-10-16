import sys
import pygame
import time
import cv2
import numpy as np
import pyautogui
import pydirectinput
import keyboard

import screenshot
from assets import *
from item import Item

delay = 0.3
TIMEOUT = 180
NUM_LINES = 3
log_file_name = 'greed_pendant_bonus_hist'
counter = 0
running = True
pygame.mixer.init()
sound = pygame.mixer.Sound("./resources/diablo-gold.wav")
sound.set_volume(0.5)


def loadPotentialTemplates():
    print(f"Loading stat lines...")
    # STR
    base_str_6 = bonus_str_6 = cv2.imread(SIX_STR_LINE)
    bonus_str_8 = cv2.imread(EIGHT_STR_LINE)
    base_str_9 = cv2.imread(NINE_STR_LINE)
    base_str_12 = cv2.imread(TWELVE_STR_LINE)
    bonus_strperlevel_1 = cv2.imread(ONE_STR_PER_LEVEL_LINE)
    bonus_strperlevel_2 = cv2.imread(TWO_STR_PER_LEVEL_LINE)

    # DEX
    base_dex_6 = bonus_dex_6 = cv2.imread(SIX_DEX_LINE)
    bonus_dex_8 = cv2.imread(EIGHT_DEX_LINE)
    base_dex_9 = cv2.imread(NINE_DEX_LINE)
    base_dex_12 = cv2.imread(TWELVE_DEX_LINE)
    bonus_dexperlevel_1 = cv2.imread(ONE_DEX_PER_LEVEL_LINE)
    bonus_dexperlevel_2 = cv2.imread(TWO_DEX_PER_LEVEL_LINE)

    # INT
    base_int_6 = bonus_int_6 = cv2.imread(SIX_INT_LINE)
    bonus_int_8 = cv2.imread(EIGHT_INT_LINE)
    base_int_9 = cv2.imread(NINE_INT_LINE)
    base_int_12 = cv2.imread(TWELVE_INT_LINE)
    bonus_intperlevel_1 = cv2.imread(ONE_INT_PER_LEVEL_LINE)
    bonus_intperlevel_2 = cv2.imread(TWO_INT_PER_LEVEL_LINE)

    # LUK
    base_luk_6 = bonus_luk_6 = cv2.imread(SIX_LUK_LINE)
    bonus_luk_8 = cv2.imread(EIGHT_LUK_LINE)
    base_luk_9 = cv2.imread(NINE_LUK_LINE)
    base_luk_12 = cv2.imread(TWELVE_LUK_LINE)
    bonus_lukperlevel_1 = cv2.imread(ONE_LUK_PER_LEVEL_LINE)
    bonus_lukperlevel_2 = cv2.imread(TWO_LUK_PER_LEVEL_LINE)

    # ALL
    bonus_allstat_5 = cv2.imread(FIVE_ALLSTAT_LINE)
    base_allstat_6 = bonus_allstat_6 = cv2.imread(SIX_ALLSTAT_LINE)
    base_allstat_9 = bonus_allstat_9 = cv2.imread(NINE_ALLSTAT_LINE)

    # HP
    bonus_hp_8 = cv2.imread(EIGHT_HP_LINE)
    base_hp_9 = cv2.imread(NINE_HP_LINE)
    bonus_hp_11 = cv2.imread(ELEVEN_HP_LINE)
    base_hp_12 = cv2.imread(TWELVE_HP_LINE)

    # CRIT DMG
    base_critdmg_8 = cv2.imread(CRIT_DMG_LINE)

    print(f"Loading weapon lines...")
    base_att_9 = bonus_att_9 = cv2.imread(NINE_ATT_LINE)
    base_att_12 = bonus_att_12 = cv2.imread(TWELVE_ATT_LINE)
    base_matt_9 = bonus_matt_9 = cv2.imread(NINE_MATT_LINE)
    base_matt_12 = bonus_matt_12 = cv2.imread(TWELVE_MATT_LINE)
    base_dmg_9 = bonus_dmg_9 = cv2.imread(NINE_DMG_LINE)
    base_dmg_12 = bonus_dmg_12 = cv2.imread(TWELVE_DMG_LINE)
    base_boss_30 = cv2.imread(BOSS_DMG_LINE)
    base_ied_30 = cv2.imread(IED_LINE)

    print(f"Loading meso & drop lines...")
    base_meso_20 = cv2.imread(MESO_LINE)
    base_drop_20 = cv2.imread(DROP_LINE)

    print(f"done loading base & bonus templates!")
    base_templates = {
        'base_str_6': base_str_6,
        'base_str_9': base_str_9,
        'base_str_12': base_str_12,
        'base_dex_6': base_dex_6,
        'base_dex_9': base_dex_9,
        'base_dex_12': base_dex_12,
        'base_int_6': base_int_6,
        'base_int_9': base_int_9,
        'base_int_12': base_int_12,
        'base_luk_6': base_luk_6,
        'base_luk_9': base_luk_9,
        'base_luk_12': base_luk_12,
        'base_allstat_6': base_allstat_6,
        'base_allstat_9': base_allstat_9,
        'base_hp_9': base_hp_9,
        'base_hp_12': base_hp_12,
        'base_critdmg_8': base_critdmg_8,
        'base_att_9': base_att_9,
        'base_att_12': base_att_12,
        'base_matt_9': base_matt_9,
        'base_matt_12': base_matt_12,
        'base_dmg_9': base_dmg_9,
        'base_dmg_12': base_dmg_12,
        'base_boss_30': base_boss_30,
        'base_ied_30': base_ied_30,
        'base_meso_20': base_meso_20,
        'base_drop_20': base_drop_20
    }
    bonus_templates = {
        'bonus_str_6': bonus_str_6,
        'bonus_str_8': bonus_str_8,
        'bonus_strperlevel_1': bonus_strperlevel_1,
        'bonus_strperlevel_2': bonus_strperlevel_2,
        'bonus_dex_6': bonus_dex_6,
        'bonus_dex_8': bonus_dex_8,
        'bonus_dexperlevel_1': bonus_dexperlevel_1,
        'bonus_dexperlevel_2': bonus_dexperlevel_2,
        'bonus_int_6': bonus_int_6,
        'bonus_int_8': bonus_int_8,
        'bonus_intperlevel_1': bonus_intperlevel_1,
        'bonus_intperlevel_2': bonus_intperlevel_2,
        'bonus_luk_6': bonus_luk_6,
        'bonus_luk_8': bonus_luk_8,
        'bonus_lukperlevel_1': bonus_lukperlevel_1,
        'bonus_lukperlevel_2': bonus_lukperlevel_2,
        'bonus_allstat_5': bonus_allstat_5,
        'bonus_allstat_6': bonus_allstat_6,
        'bonus_allstat_9': bonus_allstat_9,
        'bonus_hp_8': bonus_hp_8,
        'bonus_hp_11': bonus_hp_11,
        'bonus_att_9': bonus_att_9,
        'bonus_att_12': bonus_att_12,
        'bonus_matt_9': bonus_matt_9,
        'bonus_matt_12': bonus_matt_12,
        'bonus_dmg_9': bonus_dmg_9,
        'bonus_dmg_12': bonus_dmg_12,
    }
    return [base_templates, bonus_templates]


def findAssetInImage(asset, image, potential_name):
    res = cv2.matchTemplate(image, asset, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    threshold = 0.99
    loc = np.where(res >= threshold)
    matched_stats = []

    for pt in zip(*loc[::-1]):
        print(f"{potential_name} present with {(max_val * 100):.2f}% confidence!")
        matched_stats.append(potential_name)
    return matched_stats


def findAsset(asset, confidence=0.98, grayscale=True, region=None, log=True):
    if region is not None:
        box = pyautogui.locateOnWindow(
            asset, title='YEONHWA', confidence=confidence, grayscale=grayscale, region=region)
    else:
        box = pyautogui.locateOnWindow(
            asset, title='YEONHWA', confidence=confidence, grayscale=grayscale)
    if box == None:
        return None
    if log:
        print("Found asset: ", asset, box)
    return pyautogui.center(box)


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


def talk_to_npc():
    global counter
    pos = findAsset(CUBE_NPC, 0.9)
    if pos is not None:
        print(f"Clicking NPC")
        # NPC interaction
        pyautogui.click(pos)
        pyautogui.sleep(delay)
        # Move cursor off NPC area
        pyautogui.moveTo(pos.x+250, pos.y+250)
        pyautogui.sleep(delay)
        print(f"Hitting Enter")
        # Select first item as cube target
        pydirectinput.press("enter")
        pyautogui.sleep(delay)
        # Click to finish generating dialogue
        pyautogui.click(pos.x-500, pos.y)
        pyautogui.sleep(delay)
        # On cube selection page -> scroll down to cube select menu
        down = findAsset(DOWN, 0.9)
        if down is not None:
            print(f"Scrolling down")
            pyautogui.click(down, clicks=50)
            pyautogui.sleep(delay)
    else:
        print(f"NPC was not found, quitting")
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
        screenshot.create_cube_result(cube["init_anchor"])
    else:
        screenshot.create_cube_result(cube["anchor"])


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
        matched_stats = findAssetInImage(
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
        # file = open(f"./log/{log_file_name}.log", "a+")
        # file.write(f"End of log. Cubes consumed: {counter}\n")
        # file.write(f"-------------------------------------------------------\n")
        # file.close()
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
            print(f"trying to proceed cubing with asset: {continue_asset}")
            return proceed_cubing(continue_asset)
        else:
            try:
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
    cube = RED_CUBE_CONFIG
    # cube = BONUS_CUBE_CONFIG
    target_stats = {"baseint": 31, "basestr": 31, "basedex": 31, "baseluk": 25, "basemeso": 41, "basedrop": 41}
    # target_stats = {"bonusatt": 21}
    cube_limit = 2000
    # initial run
    # talk_to_npc()  # includes selecting item to cube step
    context_menu_cube()
    # initial cube selection step -> produces item's initial stat as cuberesult.png
    select_cube(cube)
    recube(all_templates, item, cube, target_stats, True)
    try:
        should_recube = True
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
