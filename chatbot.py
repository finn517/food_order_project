from speech import speak
from chat import process
from speech_to_text import get_speech
import order
#import whatever zubair's thng is
#initialize Jacob
speak("Welcome, what would you like to order")
while(True):
	sentance = str(get_speech())
	if (sentance == "no"):
		break;
	item = process(sentance)
	s = "One" + item + "ordered"
	speak(s)
	speak ("Is there anything else you would like to order?")


