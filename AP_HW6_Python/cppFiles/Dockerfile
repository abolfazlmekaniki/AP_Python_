
FROM python:3.9

RUN apt-get update && apt-get install -y \
    libfreetype6-dev \
    libpng-dev \
    pkg-config \
    python3-dev \
    && pip install --no-cache-dir matplotlib==3.4.2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./your_script.py" ]