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