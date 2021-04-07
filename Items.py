"""
Items.py will be a file that will initialize an item class that will contain attributes similar to a food item from
a restaurant or a fast food restaurant. This will be the object used for the order that the customer/user will be
modifying. There are also some methods to grab the attributes from the item object.

Code written by - Jacob Corbin G01075549
"""


class Item:

    def __init__(self, id, name, cost):
        self.id = id
        self.name = name
        self.cost = cost

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getCost(self):
        return self.cost
