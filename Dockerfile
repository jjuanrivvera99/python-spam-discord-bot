FROM python:3.8
# Adding trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# Adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
# Updating apt to see and install Google Chrome
RUN apt-get -y update
# Magic happens
RUN apt-get install -yqq google-chrome-stable

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get install -yqq unzip bash
# Download the Chrome Driver
RUN wget -O /tmp/chromedriver.ZIP https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip
# Unzip the Chrome Driver into /usr/local/bin directory
RUN unzip /tmp/chromedriver.ZIP -d /usr/local/bin/
# Set display port as an environment variable
ENV DISPLAY=:99

COPY requirements.txt /app/

WORKDIR /app

RUN pip install --upgrade pip && pip install -r requirements.txt

VOLUME [ "/app" ]
