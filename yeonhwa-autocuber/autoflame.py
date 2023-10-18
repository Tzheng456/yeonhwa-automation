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


def main():
    pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except NameError as e:
        print(f"{e}")