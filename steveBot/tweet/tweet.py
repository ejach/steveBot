from datetime import datetime, timedelta
from math import trunc
from os import environ
from time import sleep

from schedule import every, run_pending
from tweepy import OAuthHandler, API, TweepyException

from steveBot.draw_image.draw_image import draw_image, assets_path

# Credentials set in the config
auth = OAuthHandler(environ.get('consumer_key'), environ.get('consumer_secret'))
auth.set_access_token(environ.get('access_token'), environ.get('access_token_secret'))

# Create API object
api = API(auth)
# Time of day to tweet, 24h format, set in the config
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
    text = (tweet_text[:277] + '...') if len(tweet_text) > 280 else tweet_text
    return text


# Call the draw_image function, then tweet the image and the corresponding
# word in the body of the tweet
def tweet():
    word, word_def = draw_image()
    # Instantiate dictionary to look up definition of the word
    image = assets_path + '/assets/steve2.jpg'
    status_text = f'The word of the day is {word}: {word_def}'
    status = tweet_strip(status_text)
    # Tweet image with the corresponding status
    api.update_status_with_media(status=status, filename=image)
    print('Tweet has been sent! See you in 24h.')


# Calculates the amount of time left (in minutes) before 12am (or the custom time set in the example.env file)
def time_left():
    strip_time = tweet_time.replace(':', '')
    time_delta = datetime.combine(
        datetime.now().date() + timedelta(days=1), datetime.strptime(strip_time, '%H%M').time()
    ) - datetime.now()
    s = time_delta.seconds / 60
    return trunc(s)


try:
    # Every day at the specified time, tweet
    every().day.at(tweet_time).do(tweet)
# Catch the TypeError
except TypeError as err:
    exit(str(err) + '\n' + 'Please make sure your environment variables are set properly and try again.')

# Infinite loop, tweets every day at the desired time, rest for 24 hours until the next day.
# If executed twice within the 24 hour interval, it will notify the user how to proceed.
try:
    # Informs the user upon running the script how many minutes are left before the next tweet is sent
    print(f'There is {time_left()} minutes until the next tweet is sent. Sit tight!') if authenticate() else exit()
    # While the authentication function is true, run the tweet function every 1s
    while True:
        run_pending()
        sleep(1)
# Catch the TweepErrors and proceed accordingly
except TweepyException as err:
    if err.api_code == 186:
        exit(str(err) + '\n' + 'Error 186: Tweet needs to be a bit shorter.')
    if err.api_code == 187:
        exit(str(err) + '\n' + 'Error 187: Duplicate tweet detected. Please wait 24 hours before executing again, '
                               'or just delete the newest tweet.')
    if err.api_code == 215:
        exit(str(err) + '\n' + 'Error 215: Bad Authentication data. Please make sure your keys/credentials are '
                               'correct and try again.')
    if err.api_code == 401:
        exit(str(err) + '\n' + 'Error 401: Unauthorized. Please make sure your keys/credentials are correct and try '
                               'again.')
