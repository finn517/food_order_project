from speech import speak
from chat import process
from speech_to_text import get_speech
import order as o

# import whatever zubair's thng is
# initialize Jacob

menu = o.initMenu()
order = []

speak("Welcome, what would you like to order?")
while (True):
	sentance = str(get_speech())
	item = process(sentance)
	while (item == "sorry"):
		speak("sorry that item is not on the menu, what would you like to order?")
		sentance = str(get_speech())
		item = process(sentance)
	if (item == "quit"):
		speak(o.printOrder(order))
		speak("Thank you for ordering!, Have a nice day!")
		break
#	while(item == "remove"):
#		speak("What would you like to remove from the order?")
#		sentance = str(get_speech())
#		item = process(sentance)
#		if (item == "quit"):
#			break
#		o.removeItem(order, item)
#		break
	o.addItem(order, menu, item)
	s = "One" + item
	speak(s)
	speak("Is there anything else you would like to order?")


