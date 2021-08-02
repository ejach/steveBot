import math
from time import sleep
from json import loads
from PIL import Image, ImageFont
from PIL import ImageDraw
from random_word import RandomWords


# Function for getting the word of the day from the RandomWords library
def get_word():
    dict_word = RandomWords()
    word_grab = loads(dict_word.word_of_the_day())
    for _ in word_grab:
        dict_word = word_grab['word']
        return dict_word


# Function for getting the word's definition from the RandomWords library
def get_def():
    dict_grab = RandomWords()
    word_grab = loads(dict_grab.word_of_the_day())
    for _ in word_grab:
        # This spelling mistake is hardcoded directly in the library itself,
        # guess who isn't sleeping tonight?
        dict_def = word_grab['definations'][0]['text']
        return dict_def


# Gets width of text and adjusts accordingly so it is not cut off
def get_width(width):
    if 45 <= width < 55:
        print("Under 55: Text offset detected, adjusting accordingly.")
        return 295
    elif width < 45:
        print("Under 45: Text offset detected, adjusting accordingly.")
        return 340
    elif 60 < width < 70:
        print("Over 60: Text offset detected, adjusting accordingly.")
        return 205
    elif 70 <= width < 80:
        print("Over 70: Text offset detected, adjusting accordingly.")
        return 175
    elif 80 <= width < 90:
        print("Over 80: Text offset detected, adjusting accordingly.")
        return 110
    elif width >= 90:
        print("Over 90: Text offset detected, adjusting accordingly.")
        return 95
    else:
        return 230


# Function that handles writing the word from the library to the image
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
            height = get_width(w)
            # Checks for (almost) centering the image depending on the length of the text
            # TODO: Needs improvement
            img_1.text((height, 1020), word, fill='white', font=font,
                       stroke_width=5, stroke_fill='black')
            # Save the edited image
            img.save("../assets/steve2.jpg")
        # If typeError is thrown, get another random word
        # This is a workaround for the library itself, there is no fix as of late
        except TypeError as e:
            print(e)
            print('Restarting!')
            sleep(1)
            word = get_word()
            continue
        else:
            break
    return word
