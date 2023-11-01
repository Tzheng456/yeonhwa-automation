from pyautogui import *
from assets.asset import *
class NoAssetException(Exception):
    pass

def create_cube_result():
    print(f'Locating potential lines and taking screenshot of cube results!')
    try:
        sleep(0.075)
        before_box = locateOnWindow(BEFORE, title='Terminus', confidence=0.8)
        before_region = (before_box.left-50,before_box.top+15,before_box.width+350,before_box.height+80)
        screenshot(CUBE_RESULT_BEFORE, before_region)

        after_box = locateOnWindow(AFTER, title='Terminus', confidence=0.8)
        after_region = (after_box.left-50,after_box.top+15,after_box.width+350,after_box.height+80)
        screenshot(CUBE_RESULT_AFTER, after_region)
    except AttributeError as e:
        msg =f'Failed to locate anchor: {e}'
        raise NoAssetException(msg)