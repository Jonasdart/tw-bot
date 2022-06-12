from python:3.9-slim

WORKDIR /bot
copy . /bot/

RUN apt-get update -y && apt-get install wheel
RUN pip install -r requirements.txt

CMD main.py