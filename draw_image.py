# Importing the PIL library
import time

from PIL import Image, ImageFont
from PIL import ImageDraw
from random_word import RandomWords

rw = RandomWords()
word = rw.get_random_word(hasDictionaryDef="true", includePartOfSpeech="adjective,verb", minCorpusCount=1,
                          maxCorpusCount=10,
                          minDictionaryCount=1, maxDictionaryCount=10, minLength=5, maxLength=10)


def draw_image():
    global word
    while True:
        try:
            # Open an Image
            img = Image.open('steve.jpg')

            # Call draw Method to add 2D graphics in an image
            img_1 = ImageDraw.Draw(img)
            w, h = img_1.textsize(word)
            print('Width: ' + str(w) + ' height: ' + str(h))

            # Add Text to an image
            font_path = 'fonts/impact.ttf'
            font = ImageFont.truetype(font_path, 150)
            # Display top text
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
            img.save("steve2.jpg")
            # If typeError is thrown, get another random word
        except Exception as e:
            print(e)
            print('Restarting!')
            time.sleep(1)
            word = rw.get_random_word(hasDictionaryDef="true", includePartOfSpeech="adjective,verb", minCorpusCount=1,
                                      maxCorpusCount=10,
                                      minDictionaryCount=1, maxDictionaryCount=10, minLength=5, maxLength=10)
            continue
        else:
            break
