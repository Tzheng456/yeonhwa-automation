from pyautogui import *
from assets import *

def create_cube_result(cube_type):
    print(f'Locating potential lines and taking screenshot of cube results!')
    try:
        potentials_box = locateOnWindow(cube_type, title='YEONHWA', confidence=0.9)
        region = (potentials_box.left,potentials_box.top+15,potentials_box.width+300,potentials_box.height+80)
        screenshot(CUBE_RESULT, region)
    except AttributeError as e:
        print(f'Failed to locate anchor: {e}')

def create_flame_result():
    print(f"Locating flame lines and taking screenshot of flame results!")
    try:
        flame_box = locateOnWindow(FLAME_ANCHOR, title='YEONHWA', confidence=0.9)
        region = (flame_box.left-50, flame_box.top+120, flame_box.width+50, flame_box.height+100)
        screenshot(FLAME_RESULT, region)
    except:
        print(f"Failed to locate anchor: {e}")