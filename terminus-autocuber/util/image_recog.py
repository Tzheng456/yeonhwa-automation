import cv2
import numpy as np
import pyautogui
import pydirectinput

TIMEOUT = 5

def findAllMatchedStatsInImage(asset, image, potential_name):
    res = cv2.matchTemplate(image, asset, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    threshold = 0.99
    loc = np.where(res >= threshold)
    matched_stats = []

    for pt in zip(*loc[::-1]):
        print(f"{potential_name} present with {(max_val * 100):.2f}% confidence!")
        matched_stats.append(potential_name)
    return matched_stats

def findFlameLineInImage(asset, image):

    # Load the original image and the subregion image
    original_image = image
    subregion_image = asset

    # Match the subregion in the original image
    result = cv2.matchTemplate(original_image, subregion_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    threshold = 0.99  # Set your desired threshold value (adjust as needed)
    loc = np.where(result >= threshold)

    for pt in zip(*loc[::-1]):
        x, y = pt
        h, w, _ = subregion_image.shape

        # Crop the original image with an extended width
        extended_width = 200
        cropped_image = original_image[y:y+h, x:x+w+extended_width]

        # Save the result
        cv2.imwrite('./assets/temp/curr_flame_line.png', cropped_image)
        if cropped_image is None: return None
        return cropped_image


def findAsset(asset, confidence=0.98, grayscale=True, region=None, log=True):
    counter = 0
    if region is not None:
        box = pyautogui.locateOnWindow(
            asset, title='Terminus', confidence=confidence, grayscale=grayscale, region=region)
    else:
        box = pyautogui.locateOnWindow(
            asset, title='Terminus', confidence=confidence, grayscale=grayscale)
    while box is None:
        counter += 1
        if region is not None:
            box = pyautogui.locateOnWindow(
                asset, title='Terminus', confidence=confidence, grayscale=grayscale, region=region)
            if counter >= TIMEOUT:
                print(f"Timed out without finding asset in region:", asset)
                return None
        else:
            box = pyautogui.locateOnWindow(
                asset, title='Terminus', confidence=confidence, grayscale=grayscale)
            if counter >= TIMEOUT:
                print(f"Timed out without finding asset:", asset)
                return None
    if box is None:
        return None
    if log:
        print("Found asset: ", asset, box)
    return pyautogui.center(box)