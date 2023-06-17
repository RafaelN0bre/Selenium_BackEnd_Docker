FROM python:3.8

COPY . .

# RUN apt-get update \
#     && apt-get install -y wget curl unzip

# RUN CHROMEDRIVER_VERSION=$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE) \
#     && wget -q "https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip" \
#     && unzip chromedriver_linux64.zip \
#     && mv chromedriver /usr/local/bin/chromedriver \
#     && chmod +x /usr/local/bin/chromedriver

RUN apt-get update && apt-get -y install libglib2.0-dev libxi6 libnss3-dev
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update && apt-get -y install google-chrome-stable

RUN pip install -r back_and_scrap/requirements.txt &&\
    chmod +x start.sh

EXPOSE 5000

CMD ./start.sh
