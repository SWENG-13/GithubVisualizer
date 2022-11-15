FROM python:3.10.7-slim-buster
WORKDIR /home
ADD Frontend /home/Frontend/
ADD Backend /home/Backend/
WORKDIR /home/Backend
RUN pip install -r requirements.txt
ENTRYPOINT flask run --host=0.0.0.0
