# steveBot

[![Twitter Badge](https://img.shields.io/badge/-@SteveBWOTD-00acee?style=flat-square&logo=Twitter&logoColor=white)](https://twitter.com/intent/follow?screen_name=SteveBWOTD "Follow on Twitter")
[![Docker](https://img.shields.io/docker/v/ejach/stevebot?logo=docker&label=version&style=flat-square)](https://hub.docker.com/r/ejach/stevebot)
[![Docker](https://img.shields.io/docker/cloud/build/ejach/stevebot?logo=docker&style=flat-square)](https://hub.docker.com/r/ejach/stevebot/builds)
[![PyPI](https://img.shields.io/pypi/v/tweepy?logo=python&label=tweepy&style=flat-square&color=FFD43B)](https://pypi.org/project/tweepy/)
[![PyPI](https://img.shields.io/pypi/v/Random-Word?logo=python&label=Random-Word&style=flat-square&color=FFD43B)](https://pypi.org/project/Random-Word/)
[![PyPI](https://img.shields.io/pypi/v/Pillow?logo=python&label=Pillow&style=flat-square&color=FFD43B)](https://pypi.org/project/Pillow/)


A simple Twitter bot that tweets every 24 hours the amount of time Bobby Shmurda has been released from prison and has **not** released a song.

## How to install

### With Docker

`sudo docker run -it -e consumer_key=<YOUR_KEY> -e consumer_secret=<YOUR_KEY> -e access_token=<YOUR_KEY> -e access_token_secret=<YOUR_KEY> ejach/stevebot:latest`

### Manually

- Clone the repository
- Install the requirements using `pip3 install -r requirements.txt`
- Edit the `.env` file with your twitter tokens and API keys ([reference](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api))
- Start the program by running `python3 main.py`
- Go crazy

## ⚠ NOTICE ⚠
This is intended as a joke, please do not take it seriously.
