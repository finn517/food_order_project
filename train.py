"""file that trains neural network based off of json file
code written by Finn Cook G01134138
"""
import json
import importlib
import torch
import torch.nn as nn
import numpy as np
from torch.utils.data import Dataset, DataLoader
from nltk_utils import tokenize, stem, bag_of_words
from model import NeuralNet

with open("intents.json", "r") as f:
	intents = json.load(f)

all_words = []
tags = []
xy =[]
for intent in intents['intents']:
	tag = intent['tag']
	tags.append(tag)
	for pattern in intent['patterns']:
		w = tokenize(pattern)
		all_words.extend(w)
		xy.append((w,tag))

ignore_words = ['?','!',',','.']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))

x_train = []
y_train = []

for (pattern_sentance, tag) in xy:
	bag = bag_of_words(pattern_sentance, all_words)
	x_train.append(bag)
	label = tags.index(tag)
	y_train.append(label)

x_train = np.array(x_train)
y_train = np.array(y_train)



class ChatDataset():
	def __init__(self):
		self.n_samples = len(x_train)
		self.x_data = x_train
		self.y_data = y_train
	def __getitem__(self, index):
		return self.x_data[index], self.y_data[index]
	def __len__(self):
		return self.n_samples


batch_size = 8
hidden_size = 8
output_size = len(tags)
input_size = len(all_words)
learning_rate = .001
num_epochs = 1000
print(input_size, len(all_words))
print(output_size, tags)

dataset = ChatDataset()
train_loader = DataLoader(dataset = dataset, batch_size = batch_size, shuffle=True, num_workers=0 )

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = NeuralNet(input_size, hidden_size, output_size).to(device)


criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for epoch in range(num_epochs):
	for (words, lables) in train_loader:
		words = words.to(device)
		lables = lables.to(device, dtype=torch.long)
		
		outputs = model(words)
		loss = criterion(outputs, lables)
		
		optimizer.zero_grad()
		loss.backward()
		optimizer.step()
	
	if ((epoch + 1) % 100 == 0):
		print(f'epoch {epoch+1}/{num_epochs}, loss={loss.item():.4f}')
	
print(f'final loss, loss={loss.item():.4f}')

data = {
	"model_state": model.state_dict(),
	"input_size": input_size,
	"output_size": output_size,
	"hidden_size": hidden_size,
	"all_words": all_words,
	"tags": tags
}

FILE = "data.pth"
torch.save(data,f=FILE)

print(f'training complete. file saved to {FILE}')