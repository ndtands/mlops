FROM python:3.6.15-bullseye

RUN apt update

RUN apt install -y git

RUN mkdir -p /usr/app

COPY . /usr/app

WORKDIR /usr/app

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8011

CMD ["streamlit", "run", "app.py","--server.port","8011","--browser.serverAddress","0.0.0.0"]