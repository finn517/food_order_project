import json
import importlib
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
nltk_utils = input('nltk_utils.py')
importlib.import_module(nltk_utils)
from nltk_utils import tokenize, stem, bag_of_words

with open("intents.json", "r") as f:
	intents = json.load(f)

all_words = []
tags = []
xy =[]
for intent in intents['intents']:
	tag = intent['tag']
	tags.append(tag)
	for pattern in intents['patterns']:
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
	def _init_(self):
		self.n_samples = len(x_train)
		self.x_data = x_train
		self.y_data = y_train
	def _getitem_(self, index):
		return self.x_data[index], self.y_data[index]
	def _len_(self):
		return self.n_samples


batch_size = 8
hidden_size = 8
output_size = len(tags)
input_size = len(x_train[0])
print(input_size, len(all_words))
print(output_size, tags)

dataset = ChatDataset()
train_loader = DataLoader(dataset = dataset, batch_size = batch_size, shuffle=True, num_workers=2 )

model = NeuralNet(input_size, hidden_size, output_size)