FROM python:3.8-alpine

# set the working directory in the container
WORKDIR /steveBot

# allow logs to be printed to console output
ENV PYTHONUNBUFFERED=1

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies / make sure time zone is correct
RUN apk add -u zlib-dev jpeg-dev gcc musl-dev && \
    ln -sf /usr/share/zoneinfo/America/New_York /etc/timezone && \
    ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime && \
    pip install -r requirements.txt

# copy the content of the local directory to the working directory
COPY . /steveBot
COPY steveBot/__main__.py /steveBot

# command to run on container start
CMD [ "python", "-m", "steveBot" ]
