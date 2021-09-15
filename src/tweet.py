from math import trunc
from os import environ
from time import sleep
from datetime import datetime, timedelta
from schedule import every, run_pending
from tweepy import OAuthHandler, API, TweepError
from dotenv import load_dotenv
from draw_image import draw_image

# Loads the .env file for the credentials
load_dotenv()

# Credentials set in the .env file
consumer_key = environ.get('consumer_key')
consumer_secret = environ.get('consumer_secret')
access_token = environ.get('access_token')
access_token_secret = environ.get('access_token_secret')

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = API(auth)
# Time of day to tweet, 24h format
# This value is set in the .env file
tweet_time = environ.get('time_of_day')


# Checks if the credentials entered are correct
def authenticate():
    if not api.verify_credentials():
        print('Authentication: FAILED')
        return False
    else:
        print('Authentication: OK')
        return True


# If the Tweet is longer than 280 characters, strip it and replace with the designated characters
def tweet_strip(tweet_text):
    text = (tweet_text[:276] + '..."') if len(tweet_text) > 280 else tweet_text
    print(text)
    return text


# Call the draw_image function, then tweet the image and the corresponding
# word in the body of the tweet
def tweet():
    # word, word_def = draw_image()
    word, word_def = draw_image()
    # Instantiate dictionary to look up definition of the word
    image = './assets/steve2.jpg'
    status_text = f'The word of the day is {word}: {word_def}'
    status = tweet_strip(status_text)
    # Tweet image with the corresponding status
    api.update_with_media(image, status)
    print('Tweet has been sent! See you in 24h.')


# Calculates the amount of time left (in minutes) before 12am (or the custom time set in the .env file)
def time_left():
    strip_time = tweet_time.replace(':', '')
    time_delta = datetime.combine(
        datetime.now().date() + timedelta(days=1), datetime.strptime(strip_time, "%H%M").time()
    ) - datetime.now()
    s = time_delta.seconds / 60
    return trunc(s)


# Every day at the specified time, tweet
every().day.at(tweet_time).do(tweet)

# Infinite loop, tweets every day at the desired time, rest for 24 hours until the next day.
# If executed twice within the 24 hour interval, it will notify the user how to proceed.
try:
    # Informs the user upon running the script how many minutes are left before the next tweet is sent
    print(f'There is {time_left()} minutes until the next tweet is sent. Sit tight!') if authenticate() else exit()
    # While the authentication function is true, run the tweet function every 1s
    while True:
        run_pending()
        sleep(1)
# Catch TweepError 186 and 187 and proceed accordingly.
# If upon execution the program catches error code 401, proceed accordingly
except TweepError as err:
    if err.api_code == 186:
        print('Error 186: Tweet needs to be a bit shorter.')
    if err.api_code == 187:
        print('Error 187: Duplicate tweet detected. Please wait 24 hours before executing again, or just delete the '
              'newest tweet.')
    if err.api_code == 401:
        print('Error 401: Unauthorized. Please make sure your keys/credentials are correct and try again.')
