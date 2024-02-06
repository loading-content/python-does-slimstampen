from tarfile import ExtractError
import pytesseract
import pyautogui
import pyscreenshot as ImageGrab
from time import sleep
import os
import json

# Dictionary containing the translations
dictionary = {

}

file_path = '' #add file path to text file
if os.path.exists(file_path):
    # Open the file and load the dictionary
    with open(file_path, 'r') as f:
        dictionary = json.load(f)
else:
    print(f"The file {file_path} does not exist.")

# Function to extract text from the screen
def extract_text():
    im = ImageGrab.grab(bbox=(100, 500, 1500, 1000))  # Adjust the coordinates as needed
    text = pytesseract.image_to_string(im)
    return text.strip().lower()

# Function to type out the answer
def type_answer(answer):
    pyautogui.typewrite(answer)
    pyautogui.press('enter')

# Main function
def main():
    while True:
        extracted_text = extract_text()
        if 'nieuw!' in extracted_text:
            pyautogui.press('enter')
        if 'bijna goed!' in extracted_text:
            pyautogui.press('enter')
        elif extracted_text in dictionary:
            translation = dictionary[extracted_text]
            type_answer(translation)
        print(extracted_text)
        #sleep(0.1)  # Adjust the sleep time as needed



if __name__ == '__main__':
    sleep(1)  # Add a delay before starting the main function
    main()
