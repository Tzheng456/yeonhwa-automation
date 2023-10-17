import cv2
import numpy as np
import pyautogui
import pydirectinput

TIMEOUT = 5

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
    counter = 0
    if region is not None:
        box = pyautogui.locateOnWindow(
            asset, title='YEONHWA', confidence=confidence, grayscale=grayscale, region=region)
    else:
        box = pyautogui.locateOnWindow(
            asset, title='YEONHWA', confidence=confidence, grayscale=grayscale)
    while box is None:
        counter += 1
        if region is not None:
            box = pyautogui.locateOnWindow(
                asset, title='YEONHWA', confidence=confidence, grayscale=grayscale, region=region)
            if counter >= TIMEOUT:
                print(f"Timed out without finding asset in region:", asset)
                return None
        else:
            box = pyautogui.locateOnWindow(
                asset, title='YEONHWA', confidence=confidence, grayscale=grayscale)
            if counter >= TIMEOUT:
                print(f"Timed out without finding asset:", asset)
                return None
    if box is None:
        return None
    if log:
        print("Found asset: ", asset, box)
    return pyautogui.center(box)