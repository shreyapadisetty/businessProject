# this module is used to avoid repetition
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

# product categories
basicMenu = ["pizza", "side", "dessert", "drink"]

# each option from the categories
pizza = {1:"Cheese Pizza", 2:"Pepperoni Pizza", 3:"Veggie Pizza", 4:"Hawaiian Pizza", 5:"Ham & Cheese Pizza", 6:"Margherita Pizza"}
side = { 1:"Garlic Bread", 2:"Cheesy & Garlic Scrolls", 3:"Pepperoni Puff Roll", 4:"French Fries"}
dessert = {1:"Choc Lava Cake", 2:"Fudge Brownies", 3:"Churros"}
drink = {1:"Pepsi", 2:"Fanta", 3:"Sprite"}

# when making a custom pizza
crust = {1:"Classic Crust", 2:"Stuffed Crust", 3:"Gluten-Free Crust"}
sauce = {1:"Marinara Sauce", 2:"Pesto Sauce", 3:"BBQ Sauce", 4:"White Garlic Sauce"}
cheese = {1:"Mozzarella", 2:"Cheddar", 3:"Parmesan", 4:"Goat Cheese", 5:"Gorgonzola"}
toppings = {1:"Pepperoni", 2:"Chicken", 3:"Ham", 4:"Peppers", 5:"Mushrooms", 6:"Black Olives", 7:"Basil", 8:"Onions", 9:"Pineapple"}

# cost of a product in each category
cost = [12.99, 3.99, 3.99, 0.99]

# prints pizza pre-made menu
def pizzaMenu():
    print("Here's the menu:")
    print("PIZZAS:")
    for x in pizza:
        print(x, pizza[x])

# prints sides menu
def sideMenu():
    print("Here's the menu:")
    print("SIDES:")
    for x in side:
        print(x, side[x])

# prints desserts menu
def dessertMenu():
    print("Here's the menu:")
    print("DESSERT:")
    for x in dessert:
        print(x, dessert[x])

# prints drinks menu
def drinkMenu():
    print("Here's the menu:")
    print("DRINKS:")
    for x in drink:
        print(x, drink[x])

# prints or returns dictionary of each product
def getDict(product, prin):
    if product == "pizza":
        if prin == "n":
            return pizza
        else:
            pizzaMenu()
    elif product == "side":
        if prin == "n":
            return side
        else:
            sideMenu()
    elif product == "dessert":
        if prin == "n":
            return dessert
        else:
            dessertMenu()
    elif product == "drink":
        if prin == "n":
            return drink
        else:
            drinkMenu()

# prints crust menu
def crustMenu():
    print("CRUSTS:")
    for x in crust:
        print(x, crust[x])

# prints sauce menu
def sauceMenu():
    print("SAUCES:")
    for x in sauce:
        print(x, sauce[x])

# prints cheese menu
def cheeseMenu():
    print("CHEESES:")
    for x in cheese:
        print(x, cheese[x])

# prints toppings menu
def toppingsMenu():
    print("TOPPINGS:")
    for x in toppings:
        print(x, toppings[x])

# checks if user input is a valid choice among given options
def checkValidQ(varb, val1, val2, alpdig):
    check = "n"
    # raises ValueError: invalid literal for int() with base 10 so this is needed
    while str(val1).isdigit() and str(val2).isdigit() and str(varb).isalpha():
        varb = input("Enter a valid option: (" + str(val1) + "-" + str(val2) + ") ")

    # checking if numbers are a range or just two options
    if str(val1).isdigit() and str(val2).isdigit():
        varb = int(varb)
        if abs(val1 - val2) > 1:
            check = "y"
    # numbers in a range
    if check == "y":
    # while the numbers are below or above the given range
        while varb < val1 and varb > val2:
            try:
            # see if the user's input is within that range
                assert varb >= val1 or varb <= val2
            except:
            # if not, it will continue to ask the user for valid input until it's given
                varb = input("Enter a valid option: (" + str(val1) + alpdig + str(val2) + ") ")
                varb = int(varb)
    # for strings and when nums are next to each other (ex. 1 and 2)
    else:
    # while the vals are not either one of the given vals
        while varb != val1 and varb != val2:
            try:
                # see if user's input matches one of two given vals
                assert varb == val1 or varb == val2
            except:
                # if not, it will continue to ask the user for valid input until it's given
                varb = input("Enter a valid option: (" + str(val1) + alpdig + str(val2) + ") ")
            # so there are no errors when comparing two ints as input is always a string
                if str(val1).isdigit() and str(val2).isdigit():
                    varb = int(varb)
    return varb

# asks user for delivery date
def deliveryDate():
    root = tk.Tk()
    root.geometry("300x100")

# gets the date and asks if the user wants to confirm this date
    def getEntry():
        res = cal.get()
        ans = messagebox.askquestion("Confirmation", "Are you sure?")
        if ans == "yes":
            print("Your delivery is set for: " + res)
        # program will continue after window is destroyed
            root.destroy()

# calendar
    cal=DateEntry(root, selectmode='day')
    cal.pack(pady = 20)

# select button
    btn = tk.Button(root, height=1, width=10, text="Select", command=getEntry)
    btn.pack()

    root.mainloop()

# writes receipt to text file
def printReceipt(customer_order, costs, subtotal, afterTax, deliveryFee, totalCost):
    f = open("receipt.txt", "w")
    f.write("-----------RECEIPT-----------")
# know the values for costs to print
    i = len(costs)
# prints product, amount, and cost
    for x in customer_order:
        f.write(str(x) + " (" + str(customer_order[x]) + ")     $" + str(round(costs[-i], 2)))
    f.write("-----------------------------")
    f.write("Subtotal: $" + str(subtotal) + "\n")
    f.write("Tax: $" + str(afterTax) + "\n")
    f.write("Delivery fee: $" + str(deliveryFee))
    f.write("Total: $" + str(totalCost))
    f.write("-----------------------------")
    f.close()
