FROM python:3.10.7-slim-buster
WORKDIR /home
ADD Frontend /home/
ADD Backend /home/
WORKDIR /home/Backend
RUN pip install -r requirements.txt
ENTRYPOINT flask run
