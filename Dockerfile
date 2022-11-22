FROM python:3.10.7-slim-buster
WORKDIR /home
ADD Frontend /home/Frontend/
ADD Backend /home/Backend/
WORKDIR /home/Backend
RUN pip install -r requirements.txt
ENTRYPOINT streamlit run app.py
