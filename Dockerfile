FROM python:3.10.7-slim-buster
WORKDIR /home
ADD . /home
WORKDIR /home
RUN pip install -r requirements.txt
ENTRYPOINT streamlit run app.py
