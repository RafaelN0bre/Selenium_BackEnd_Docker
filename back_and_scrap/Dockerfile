FROM python:3.8

COPY . .

RUN apt-get install -yqq unzip

RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip

RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

ENV DISPLAY=:99

RUN pip install -r back_and_scrap/requirements.txt &&\
    chmod +x start.sh

EXPOSE 5000

CMD ./start.sh
