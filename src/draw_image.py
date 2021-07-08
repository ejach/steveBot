# Importing the PIL library
import json
import time

from PIL import Image, ImageFont
from PIL import ImageDraw
from random_word import RandomWords

# Global variable for the RandomWords function
wotd = RandomWords()


# Function for getting the word of the day from the RandomWords API
def get_word():
    dict_word = RandomWords()
    word_grab = json.loads(dict_word.word_of_the_day())
    for _ in word_grab:
        dict_word = word_grab['word']
        return dict_word


# Function for getting the word's definition from the RandomWords API
def get_def():
    dict_grab = RandomWords()
    word_grab = json.loads(dict_grab.word_of_the_day())
    for _ in word_grab:
        dict_def = word_grab['definations'][0]['text']
        return dict_def


# Function that handles writing the word from the API to the image
# Saved as steve2.jpg, returns the word for use in the tweet status
def draw_image():
    # Calls the get_word function
    word = get_word()
    while True:
        try:
            # Open an Image
            img = Image.open('../assets/steve.jpg')

            # Call draw Method to add 2D graphics in an image
            img_1 = ImageDraw.Draw(img)
            w, h = img_1.textsize(word)
            print('Width: ' + str(w) + ' height: ' + str(h))

            # Add text to an image
            font_path = '../assets/fonts/impact.ttf'
            font = ImageFont.truetype(font_path, 150)
            # Checks for (almost) centering the image depending on the length of the text
            # TODO: Needs improvement
            if 45 < w < 55:
                img_1.text((295, 1020), word, fill='white', font=font,
                           stroke_width=5, stroke_fill='black')
                print("Under 55: Text offset detected, adjusting accordingly.")
            elif w < 45:
                img_1.text((340, 1020), word, fill='white', font=font,
                           stroke_width=5, stroke_fill='black')
                print("Under 45: Text offset detected, adjusting accordingly.")
            else:
                img_1.text((230, 1020), word, fill='white', font=font,
                           stroke_width=5, stroke_fill='black')
            # Save the edited image
            img.save("../assets/steve2.jpg")
            # If typeError is thrown, get another random word
            # This is a workaround for the API itself, there is no fix as of late
        except Exception as e:
            print(e)
            print('Restarting!')
            time.sleep(1)
            word = get_word()
            continue
        else:
            break
    return word
