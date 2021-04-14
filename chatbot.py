from speech import speak
from chat import process
from speech_to_text import get_speech
import Order as o

# import whatever zubair's thng is
# initialize Jacob

menu = o.initMenu()
order = []

speak("Welcome, what would you like to order")
while (True):
    sentance = str(get_speech())
    if (sentance == "no" or sentance == "No" or sentance == "quit"):
        speak(o.printOrder(order))
        break
    item = process(sentance)
    o.addItem(order, menu, item)
    s = "One" + item
    speak(s)
    speak("Is there anything else you would like to order?")
