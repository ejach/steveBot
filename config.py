from os import environ


class App:
    # Get keys/tokens from environment
    __conf = {
        'consumer_key': environ.get('consumer_key'),
        'consumer_secret': environ.get('consumer_secret'),
        'access_token': environ.get('access_token'),
        'access_token_secret': environ.get('access_token_secret'),
        'time_of_day': environ.get('time_of_day')
    }

    # Return the credential value by the key name
    @staticmethod
    def config(name):
        return App.__conf[name]
