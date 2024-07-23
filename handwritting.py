import pywhatkit as pw
import time

while True:
    try:
        # Prompt the user to enter the text
        txt = input("Enter the text: ")

        # Convert the text to handwriting and save it as an image
        pw.text_to_handwriting(txt, "pywhatkit.png", rgb=(0, 0, 255))

        # Print a confirmation message
        print("Saved as pywhatkit.png")
        break
    except pw.core.exceptions.UnableToAccessApi:
        print("Unable to access Pywhatkit API. Trying again in 5 seconds...")
        time.sleep(5)