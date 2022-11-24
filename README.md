# GithubVisualizer

To run dev server
1. Go into Backend/
2. Run "pip install -r requirements.txt"
3. Run "flask run"
4. Go to 127.0.0.1:5000 in a web browser.

To build docker container:
1. Run "docker build -t sweng3 ."
2. Run "docker create -ti --name SWENG3 -p 80:80 sweng3"
3. Run "docker start SWENG3"
4. Go to 127.0.0.1 in a web browser.
