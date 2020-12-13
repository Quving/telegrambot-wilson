FROM ubuntu:20.04

LABEL maintainer="vinh-ngu@hotmail.com"

ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install python3 python3-pip wget firefox -y

WORKDIR /app

# Install Firefox
RUN wget "https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux64.tar.gz" -O geckodriver.tar.gz
RUN tar xvfz geckodriver.tar.gz
# RUN wget "https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=de" -O firefox.tar.bz2
# RUN tar xvf firefox.tar.bz2
# RUN ln -s /app/firefox/firefox /usr/bin/firefox


# Install Dependencies for T-Bot
ADD . .
RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]
