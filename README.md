# steveBot

[![Twitter Badge](https://img.shields.io/badge/-@SteveBWOTD-00acee?style=flat-square&logo=Twitter&logoColor=white)](https://twitter.com/intent/follow?screen_name=SteveBWOTD "Follow on Twitter")
[![PyPI](https://img.shields.io/pypi/v/tweepy?logo=python&label=tweepy&style=flat-square&color=FFD43B)](https://pypi.org/project/tweepy/)
[![PyPI](https://img.shields.io/pypi/v/Random-Word?logo=python&label=Random-Word&style=flat-square&color=FFD43B)](https://pypi.org/project/Random-Word/)
[![PyPI](https://img.shields.io/pypi/v/Pillow?logo=python&label=Pillow&style=flat-square&color=FFD43B)](https://pypi.org/project/Pillow/)

A Twitter bot that tweets a Steve Buscemi word of the day.

## How to install

### With Docker

`sudo docker run -it -e consumer_key=<YOUR_KEY> -e consumer_secret=<YOUR_KEY> -e access_token=<YOUR_KEY> -e access_token_secret=<YOUR_KEY> -e time_of_day=00:00 ghcr.io/ejach/stevebot:latest`

#### Docker Compose
```yaml
version: '3.2'
services:
   stevebot:
      container_name: stevebot
      image: ghcr.io/ejach/stevebot:latest
      environment:
        - PYTHONUNBUFFERED=1
        - time_of_day=00:00
        - consumer_key=<consumer_key>
        - consumer_secret=<consumer_secret>
        - access_token=<access_token>
        - access_token_secret=<access_token_secret>
      restart: unless-stopped
```

### Manually

- Clone the repository
- Install the requirements using `pip3 install -r requirements.txt`
- Edit the `.env` file with your twitter tokens and API keys ([reference](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api))
- Start the program by running `python3 main.py`
- Go crazy

## ⚠ NOTICE ⚠
This is intended as a joke, please do not take it seriously.
