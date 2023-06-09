from os import path, getenv
from time import sleep
from json import loads
from urllib.request import urlopen

from PIL import Image, ImageFont, ImageDraw

from steveBot.logger.log_conf import Logger


# Path for the assets based on if it is running in a Docker container
assets_path = '.' if path.isfile('/steveBot/__main__.py') else '..'


# Function for getting the word of the day from the RandomWords library and its definition
def get_word():
    req = urlopen('https://api.wordnik.com/v4/words.json/wordOfTheDay?api_key=%s' % getenv('wordnik_api_key'))
    res = loads(req.read().decode(req.info().get_param('charset') or 'utf-8'))
    word = res['word']
    word_def = res['definitions'][0]['text']
    return {'word': word, 'word_def': word_def}


# Gets width of text and adjusts accordingly so it is not cut off
def get_width(width):
    if 45 <= width < 55:
        Logger.log.info('Under 55: Text offset detected, adjusting accordingly.')
        return 295
    elif width < 45:
        Logger.log.info('Under 45: Text offset detected, adjusting accordingly.')
        return 340
    elif 60 < width < 70:
        Logger.log.info('Over 60: Text offset detected, adjusting accordingly.')
        return 205
    elif 70 <= width < 80:
        Logger.log.info('Over 70: Text offset detected, adjusting accordingly.')
        return 175
    elif 80 <= width < 90:
        Logger.log.info('Over 80: Text offset detected, adjusting accordingly.')
        return 110
    elif width >= 90:
        Logger.log.info('Over 90: Text offset detected, adjusting accordingly.')
        return 95
    else:
        return 230


# Function that handles writing the word from the library to the image
# Saved as steve2.jpg, returns the word for use in the tweet status
def draw_image():
    # Calls the get_word function
    gw = get_word()
    word = gw['word']
    # Open an Image
    img = Image.open(assets_path + '/assets/steve.jpg')

    # Call draw Method to add 2D graphics in an image
    img_1 = ImageDraw.Draw(img)
    w, h = img_1.textsize(word)
    Logger.log.info('Width: %s Height: %s' % (str(w), str(h)))

    # Add text to an image
    font_path = assets_path + '/assets/fonts/impact.ttf'
    font = ImageFont.truetype(font_path, 150)
    height = get_width(w)
    # Checks for (almost) centering the image depending on the length of the text
    img_1.text((height, 1020), word, fill='white', font=font,
               stroke_width=5, stroke_fill='black')
    # Save the edited image
    img.save(assets_path + '/assets/steve2.jpg')