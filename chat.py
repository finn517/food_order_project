import random
import json
import torch 
from model import NeuralNet
from nltk_utils import tokenize, stem, bag_of_words

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

with open('intents.json', 'r') as f:
	intents = json.load(f)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]
hidden_size = data["hidden_size"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()


bot_name = "Zoey"
print("Welcome, please make your order")
while True:
	sentance = input("Enter order: ")
	if sentance == "bye":
		break;
	sentance = tokenize(sentance)
	x = bag_of_words(sentance, all_words)
	print(x)
	x = x.reshape(1, x.shape[0])
	print(x)
	x = torch.from_numpy(x)
	print(x)
	output = model(x)
	print(x)
	_, predicted = torch.max(output, dim=1)
	print(predicted)
	tag = tags[predicted.item()]
	print(tag)
#	for intent in intents["intents"]:
#		if tag == intent["tag"]:
#			choice = random.choice(intent["responses"])
#			print(f"{bot_name}: {choice}")