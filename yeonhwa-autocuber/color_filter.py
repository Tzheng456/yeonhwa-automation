import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Load the image
image = cv2.imread('./assets/temp/flameresult.png')

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
cv2.imwrite('filtered_text.png', filtered_text)

# Convert the filtered text to grayscale
gray_filtered_text = cv2.cvtColor(filtered_text, cv2.COLOR_BGR2GRAY)

# Use Tesseract to perform OCR and extract text
extracted_text = pytesseract.image_to_string(gray_filtered_text)

symbols_to_remove = ['+', '(', ')', '%']
for symbol in symbols_to_remove:
    extracted_text = extracted_text.replace(symbol, '')

print(extracted_text)
# Display the resulting image
# cv2.imshow('Filtered Text', filtered_text)
# cv2.waitKey(0)
# cv2.destroyAllWindows()