from tarfile import ExtractError
import pytesseract
import pyautogui
import pyscreenshot as ImageGrab
from time import sleep

# Dictionary containing the translations
dictionary = {
    "commuters": "forenzen",
    "employees": "werknemers",
    "employers": "werkgevers",
    "immigrants": "immigranten",
    "inhabitants": "inwoners",
    "motorists": "automobilisten",
    "pedestrians": "voetgangers",
    "politicians": "politici",
    "refugees": "vluchtelingen",
    "residents": "bewoners",
    "the crew": "de bemanning",
    "the staff": "het personeel",
    "bring about": "teweegbrengen",
    "go through": "doormaken",
    "pick up": "oppakken",
    "put up with": "ermee leven",
    "set out for": "vertrekken",
    "touch down": "landen",
    "turn out": "uitdraaien",
    "wear out": "afmatten",
    "borders": "grenzen",
    "remain": "overblijven",
    "immunity": "immuniteit",
    "destination": "bestemming",
    "annual": "jaarlijks",
    "clans": "clans",
    "extinct": "uitgestorven",
    "diet": "voedingspatroon",
    "Cue": "Antwoord",
    "dive": "duiken",
    "climb": "klimmen",
    "crawl": "kruipen",
    "hop": "hinkelen",
    "leap": "springen",
    "rush": "haasten",
    "stagger": "strompelen",
    "swing": "zwaaien",
    "tiptoe": "op je tenen lopen",
    "wander": "zwerven",
    "ashamed": "beschaamd",
    "puzzled": "verbaasd",
    "stuck": "vastgelopen",
    "awkward": "ongemakkelijk",
    "guilty": "schuldig",
    "desperate": "wanhopig",
    "right?": "toch?",
    "right away": "onmiddellijk",
    "right in the middle": "precies in het midden",
    "rightly or wrongly": "terecht of onterecht",
    "sword": "zwaard",
    "shield": "schild",
    "leather jacket": "leren jas",
    "wig": "pruik",
    "snorkel": "snorkel",
    "poncho": "poncho",
    "helmet": "helm",
    "bathrobe": "badjas",
    "mask": "masker",
    "apron": "schort",
    "football top": "voetbalshirt",
    "bring up": "grootbrengen",
    "childhood": "jeugd",
    "do your best": "je best doen",
    "do well": "goed doen",
    "get ahead in life": "vooruitgaan in het leven",
    "grow up": "opgroeien",
    "soft": "mild",
    "strict": "streng",
    "trendy": "trendy",
    "didn't have a clue": "had geen idee",
    "whichever way": "hoe dan ook",
    "to reckon": "veronderstellen",
    "straightforward": "rechtdoorzee",
    "mess it up": "het verknoeien",
    "ridiculous": "belachelijk",
        "Cue": "Antwoord",
    "bright": "pienter",
    "arrogant": "arrogant",
    "bad-tempered": "humeurig",
    "cautious": "voorzichtig",
    "confident": "zelfverzekerd",
    "decisive": "daadkrachtig",
    "dull": "saai",
    "imaginative": "vindingrijk",
    "impatient": "ongeduldig",
    "organised": "georganiseerd",
    "practical": "praktisch",
    "responsible": "verantwoordelijk",
    "for good": "voor altijd",
    "So far, so good": "Tot nu toe gaat het goed",
    "not very good at": "niet erg goed in",
    "It's no good": "Het heeft geen nut",
    "It's a good thing that...": "Het is maar goed dat...",
    "in secret": "in het geheim",
    "by accident": "per ongeluk",
    "in a hurry": "overhaast",
    "in a panic": "in paniek",
    "in a row": "achter elkaar",
    "in private": "prive",
    "in public": "in het openbaar",
    "on purpose": "bewust"
}

# Function to extract text from the screen
def extract_text():
    im = ImageGrab.grab(bbox=(200, 500, 1300, 1000))  # Adjust the coordinates as needed
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
        elif extracted_text in dictionary:
            translation = dictionary[extracted_text]
            type_answer(translation)
        print(extracted_text)
        sleep(1)  # Adjust the sleep time as needed



if __name__ == '__main__':
    sleep(1)  # Add a delay before starting the main function
    main()
