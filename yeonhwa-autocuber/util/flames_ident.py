import cv2
import pytesseract
import re
import pyautogui

from util.image_recog import findFlameLineInImage
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def get_line_update_cache_flame(flame_line, stat_name, flame):
    # Load the image
    image = flame_line

    # Convert to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define a range for the greenish hue
    lower_green = (35, 50, 50)  # Lower range for greenish hue
    upper_green = (85, 255, 255)  # Upper range for greenish hue

    # Create a mask
    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)

    # Filter the text
    filtered_text = cv2.bitwise_and(image, image, mask=green_mask)

    # Save the resulting image
    cv2.imwrite('./assets/temp/filtered_text.png', filtered_text)

    # Convert the filtered text to grayscale
    gray_filtered_text = cv2.cvtColor(filtered_text, cv2.COLOR_BGR2GRAY)

    # Use Tesseract to perform OCR and extract text
    custom_config = r'--oem 3 --psm 7'
    stat_val = pytesseract.image_to_string(gray_filtered_text, config=custom_config)
    print(f"stat_val before filter:{stat_val}")
    stat_val = ''.join(re.findall(r'\d', stat_val))
    print(f"Found: {stat_name}:{stat_val} in flame results!")
    add_flame = getattr(flame, f"add_{stat_name}")
    add_flame(stat_val)


def get_lines(templates, flame, flame_result, is_wep):
    print(f"cache: clearing flame, updating flame")
    flame.clear_stats()
    print(f"Getting flame lines!")
    for stat_name in templates.keys():
        flame_line = findFlameLineInImage(templates[stat_name], flame_result)
        if flame_line is not None:
            get_line_update_cache_flame(flame_line, stat_name, flame)
            input("KEY TO CONTINUE")