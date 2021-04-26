"""
test_Order.py is a file that is used to test out the essential methods of Order.py. This utilizes the unittest module
to create automated test cases to test the functionality of Order.py.

Code written by - Jacob Corbin G01075549
"""

import unittest
import Order

class TestMenu(unittest.TestCase):

    def testMenu1(self):
        menu = Order.initMenu()
        self.assertEqual(menu[0].getName(), "burger order")

    def testMenu2(self):
        menu = Order.initMenu()
        self.assertEqual(menu[1].getName(), "chicken order")

    def testMenu3(self):
        menu = Order.initMenu()
        self.assertEqual(menu[2].getName(), "fries order")

class TestOrderAdd(unittest.TestCase):

    def testAdd1(self):
        menu = Order.initMenu()
        order = []
        Order.addItem(order, menu, "burger order")
        self.assertEqual(order[0].getName(), "burger order")
        self.assertEqual(order[0].getCost(), 3.99)

    def testAdd2(self):
        menu = Order.initMenu()
        order = []
        Order.addItem(order, menu, "burger order")
        Order.addItem(order, menu, "chicken order")
        self.assertEqual(order[1].getName(), "chicken order")
        self.assertEqual(order[1].getCost(), 2.99)

    def testAdd3(self):
        menu = Order.initMenu()
        order = []
        Order.addItem(order, menu, "burger order")
        Order.addItem(order, menu, "chicken order")
        Order.addItem(order, menu, "burger order")
        self.assertEqual(order[2].getName(), "burger order")
        self.assertEqual(order[2].getCost(), 3.99)

class TestGets(unittest.TestCase):

    def testMenuGet1(self):
        menu = Order.initMenu()
        item = Order.getFromMenu(menu, "fries order")
        self.assertEqual(item.getName(), "fries order")
        self.assertEqual(item.getCost(), 1.99)

    def testMenuGet2(self):
        menu = Order.initMenu()
        item = Order.getFromMenu(menu, "burger order")
        self.assertEqual(item.getName(), "burger order")
        self.assertEqual(item.getCost(), 3.99)

class TestTotalCost(unittest.TestCase):

    def testTotalCost1(self):
        menu = Order.initMenu()
        order = []
        Order.addItem(order, menu, "burger order")
        total = Order.calcTotal(order)
        self.assertEqual(total, 3.99)

    def testTotalCost2(self):
        menu = Order.initMenu()
        order = []
        Order.addItem(order, menu, "burger order")
        Order.addItem(order, menu, "burger order")
        Order.addItem(order, menu, "burger order")
        total = Order.calcTotal(order)
        self.assertEqual(total, 11.97)

    def testTotalCost3(self):
        menu = Order.initMenu()
        order = []
        Order.addItem(order, menu, "burger order")
        Order.addItem(order, menu, "chicken order")
        Order.addItem(order, menu, "fries order")
        total = Order.calcTotal(order)
        self.assertEqual(total, 8.97)

if __name__ == "__main__":
    unittest.main()
