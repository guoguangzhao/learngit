import numpy as np
import math
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"restaurant_name:{self.restaurant_name};cuisine_type:{self.cuisine_type}")

    def open_restaurant(self):
        print("restaurant is opening")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script
if __name__ == '__main__':
   mylist = [1,2,3]
   mylist = mylist[2:0]
   ll = (1,2,3)
   print(type(ll))
   print(mylist)
   print("hello")
   print(ll)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
