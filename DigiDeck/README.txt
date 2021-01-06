This set of scripts uses python to generate the necessary HTML and JS to create a local server that serves a soundboard page over your area network. Its use is intended for people who stream games, but was written in a way where all you have to do is drag and drop soundclip mp3's into the folder and everything else is done for you. The soundboard can be accessed and interacted with via wifi with a phone or tablet on the users network and will play the sound locally on the computer so it can be heard in stream.

Running Instructions:

-If you do not have Python 3.7 installed, install Python 3.7 or greater
	-https://www.python.org/downloads/
	-Ensure you install Python 3.7 AND it is added to PATH enviornment variables

-Open DigiDeck.bat by double clicking
-Open the address provided in the CMD prompt window on your tablet or phone WHILE CONNECTED TO WIFI
-Enjoy!




-TO ADD BUTTONS AND SOUND CLIPS-
-Drag and drop any .mp3 into the Sounds folder
	-The filename CANNOT be only an integer (111.mp3)
	-The file MUST be a .mp3
	-The filename will be the name displayed on the button
	-Re-running DigiDeck.bat is required after every sound that is added, buttons will be generated automatically after reload.
