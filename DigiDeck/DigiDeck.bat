@echo off
pip install hug &
pip install numpy &
pip install playsound &
python htmlGenerator.py &
python serverGenerator.py &
python ipFinder.py
PAUSE
hug -f server.py
PAUSE