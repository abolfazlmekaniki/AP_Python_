FROM python:3.11.3-slim-bullseye

WORKDIR /usr/src/app

ADD requirements.txt .

RUN python3 -m pip install --no-cache-dir -r requirements.txt && rm requirements.txt


COPY . .
