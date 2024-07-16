# 1 describe the problem
# list of dishes and prices
# select some number of the available dishes
# show itemised receipt with grand total
# use twilit to confirm order is on its way at a set time

# 2 
# class menu
# def __init__
# parameters are self, menu
# output is none
# process initialises:
# self.menu, a dictionary where keys are dish names, and the items are the price
# self.order, an empty list

# def view_dishes
# parameters are self
# output is a dictionary where keys are dish names, and the items are the price
# no process

# def add_dish
# parameters are self and dish_name
# output is none
# process finds checks if dish_name is in self.menu, and if so adds it to self.order

# def calculate_receipt
# parameters are self
# output is a list of dishes in self.order, and the calculated price of all the dishes

# def other

# 3 test examples
# see test_takeaway.py

# 4 implementation
import twilit

class Takeaway:
    def __init__(self,menu):
        self.menu = menu
        self.order = []

    def view_dishes(self):
        return self.menu
    
    def add_dish(self, dish_name):
        if dish_name in self.menu.keys():
            self.order.append(dish_name)

    def calculate_receipt(self):
        total = 0
        for item in self.order:
            total += self.menu[item]
        return [total, self.order]