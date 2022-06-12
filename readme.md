# Twitch Poll Bot

Using [TwitchIO](https://github.com/TwitchIO/TwitchIO) to listening messages and generate commands on twitchTV stream chats. A great way to realtime interation!

## To Run

    Configure envs on compose.yml

with docker-compose

    docker-compose up

with docker

    docker build . -t twbot 

    docker run twbot --env-file ./.env
or

    docker run twbot --env ACCESS_TOKEN=TWITCH_ACCESS_TOKEN --env COMMANDS_PREFIX=! --env CHANNEL_NAME=...



## Development

### To Test

    pip install -r requirements.txt
    pip install -r test-requirements.txt

    python -m pytest tests