# food_order_project
This project is a chotbot that interacts with the user and takes their order based on a menu
The code is broken up into four sections
Artificial Neural Network - author Finn Cook:
chat.py
model.py
train.py
nltk_utils.py
data.pth
intents.json
refrences:
https://pytorch.org/docs/stable/index.html
https://stackoverflow.com/questions/65979825/valueerror-only-one-element-tensors-can-be-converted-to-python-scalars-while-co
Speech recognition - author Zubair Azam:
speech_to_text.py
refrences:
https://youtu.be/f_Pq7GDdxos
Data Structure - author Jacob Corbin:
Items.py
Order.py
Additional files:
chatbot.py (main file for running code) - authors Finn Cook and Jacob Corbin
speech.py (implements google speech to text) - author Finn Cook


For running the code first download these libraries from pip:
json, PyTorch, importlib, numpy, nltk, gtts, playsound, speechrecognition

As well as PyAudio from conda 

To run the code place all of the files in one directory and enter that directory in command line
then run python chatbot.py and you will be prompted by our chatbot to make your order!
