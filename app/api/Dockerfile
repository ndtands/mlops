FROM python:3.6.15-bullseye

RUN apt update

RUN apt install -y git

RUN mkdir -p /usr/api

COPY . /usr/api

WORKDIR /usr/api

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN wandb login f1a1f2001df713a04e2f5fa9302e426705a9ee4d

EXPOSE 8010

CMD ["uvicorn", "api:api", "--port", "8010", "--host", "0.0.0.0"]
