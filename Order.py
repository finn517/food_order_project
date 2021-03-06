"""
Order.py is a file that will contain the customer/user's order. This will contain a list of items that the user will
order which will be called the menu. There will also be a list that the user can add or remove from as well as find
the total cost of the items that they already have. This list will be called the order.

Code written by - Jacob Corbin G01075549
"""

# Importing the Items class
import Items as it

# Method to initialize an array of items which will be the menu
def initMenu():
    item1 = it.Item(1, "burger order", 3.99)
    item2 = it.Item(2, "chicken order", 2.99)
    item3 = it.Item(3, "fries order", 1.99)
    menu = [item1, item2, item3]
    return menu

# This method will print the menu
def printMenu(menu):
    s = ""
    for item in menu:
        s = s + "Item number " + str(item.getId()) + " is " + item.getName() + " and costs $" + str(item.getCost())
    return s
# This method will add an item object to an order list
def addItem(order, menu, name):
    item = getFromMenu(menu, name)
    order.append(item)

# This method will remove an item object from an order list based on the items id
def removeItem(order, name):
    for item in order:
        if item.getName() == name:
            order.remove(item)
            break

# This method will calculate the total cost of the order at that that time
def calcTotal(order):
    total = 0
    for item in order:
        total = total + float(item.getCost())
    final_total = round(total, 2)
    return final_total

# This method will grab an item from the menu based off of the name
def getFromMenu(menu, name):
    for item in menu:
        if item.getName() == name:
            return item

# This method will get an item
def getItem(order, id):
    for item in order:
        if item.getId == id:
            return item

# This method will print out the order along with the total cost
def printOrder(order):
    s = ""
    s = s+"Here is your current order: "
    for item in order:
        s = s + str(item.getId()) + " " + item.getName() + " $" + str(item.getCost())
    s = s + "The total cost of the order is $" + str(calcTotal(order))
    return s
