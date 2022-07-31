import module

class Product:
    def __init__(self, name):
        self.name = name

class Pizza(Product):
    def __init__(self):
        super().__init__(name)
        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings

# contains ordering process
class Main:
# contains customers final order
    customer_order = {}
# contains customers costs for each product
    costs = []
    subtotal = 0
    tax = .0275
    deliveryFee = 3.99

    print("Hello! Welcome to Domino's Pizza!")
# determines whether customer is finished ordering
    order = "n"

# prompts user whether they want to order or not
    yesorno = input("Would you like to order? (y/n) ")
# validates user's input
    yesorno = module.checkValidQ(yesorno, "y", "n", "/")

    if yesorno == "y":
        order = "y"
# if you didn't want to order
    else:
        print("Have a nice day!")

# if user wants to order
    while order == "y":
    # cycling through each product
        for product in module.basicMenu:
            i = 1
            productYN = input("Would you like to order a " + product + "? (y/n) ")
        # checking to see if user inputted a valid answer
            productYN = module.checkValidQ(productYN, "y", "n", "/")

        # if user wants to order that product
            if productYN == "y":
            # will be used for custom pizzas to keep track of which pizza is which
                pizzaCounter = 1
                if product == module.basicMenu[0]:
                # this variable determines whether user wants to continue ordering that product
                    contOrdProd = "y"
                # loops until the user doesn't want to order more of this product
                    while contOrdProd == "y":
                        inp = input("Would you like a pre-made (1) or custom (2) pizza? (1-2) ")
                        inp = module.checkValidQ(inp, 1, 2, "-")

                    # if user wants to order a pre-made pizza
                        if inp == 1:
                        # prints pizza menu
                            module.pizzaMenu()
                        # asking user what pre-made pizza they want
                            choice = int(input("Which pizza would you like? (1-6) "))
                            choice = module.checkValidQ(choice, 1, 6, "-")
                        # how many of selected product
                            amount = int(input("How many would you like (max 10)? (1-10) "))
                            amount = module.checkValidQ(amount, 1, 10, "-")
                        # adds to customer's order
                            customer_order[module.getDict(product, "n")[choice]] = amount
                        # adding the cost to list to print later with products ordered and amount
                            costs.append(module.cost[0] * amount)
                        # adding product's cost to subtotal
                            subtotal += amount * module.cost[0]

                    # if user wants to order a custom pizza
                        else:
                        # asking user how many custom pizzas
                            amount = int(input("How many would you like (max 10)? (1-10) "))
                            amount = module.checkValidQ(amount, 1, 10, "-")

                        # making custom pizza object
                            for p in range(amount):
                            # making and naming custom pizza object
                                obj = Product("Pizza "+str(pizzaCounter))

                            # selecting crust
                                module.crustMenu()
                                crust = int(input("What crust would you like? (1-3) "))
                                crust = module.checkValidQ(amount, 1, 3, "-")
                                obj.crust = module.crust[crust]
                            # selecting sauce
                                module.sauceMenu()
                                sauce = int(input("What sauce would you like? (1-4) "))
                                sauce = module.checkValidQ(amount, 1, 4, "-")
                                obj.sauce = module.sauce[sauce]
                            # selecting cheese
                                module.cheeseMenu()
                                cheese = int(input("What cheese would you like? (1-5) "))
                                cheese = module.checkValidQ(amount, 1, 5, "-")
                                obj.cheese = module.cheese[cheese]
                            # selecting topping
                                module.toppingsMenu()
                                top = int(input("What toppings would you like? (1-9) "))
                                top = module.checkValidQ(amount, 1, 9, "-")
                                obj.toppings = module.toppings[top]

                                pizzaCounter += 1
                            # adds to the user's order
                                customer_order[obj.name + "(" + obj.crust + ", "+ obj.sauce + ", " + obj.cheese + ", " + obj.toppings +")"] = 1
                            # adding the cost to list to print later with products ordered and amount
                                costs.append(module.cost[0] * amount)
                    # adding product's cost to subtotal
                        subtotal += amount * module.cost[0]
                    # asks if user wants to order another of that same product
                        contOrdProd = input("Would you like to order another " + product + "? (y/n) ")
                        contOrdProd = module.checkValidQ(contOrdProd, "y", "n", "/")

            # all other products besides pizza
                else:
                # prints menu for that product
                    module.getDict(product, "")
                    contOrdProd = "y"
                    while contOrdProd == "y":
                    # asks if you want to order this product
                        choice = int(input("Which item would you like? (1-" + str(len(module.getDict(product, "n"))) +
                                           ") "))
                        choice = module.checkValidQ(choice, 1, len(module.getDict(product, "n")), "-")
                    # how many of selected product
                        amount = int(input("How many would you like (max 10)? (1-10) "))
                        amount = module.checkValidQ(amount, 1, 10, "-")
                    # adds to customer's order
                        customer_order[module.getDict(product, "n")[choice]] = amount
                    # adding the cost to list to print later with products ordered and amount
                        costs.append(module.cost[i] * amount)
                    # adding product's cost to subtotal
                        subtotal += amount * module.cost[i]
                    # asks if user wants to order another of that same product
                        contOrdProd = input("Would you like to order another " + product + "? (y/n) ")
                        contOrdProd = module.checkValidQ(contOrdProd, "y", "n", "/")
                # cycle through costs of each product
                    i += 1
    # ordering is finished
        order = "n"
# prompting user when order should be delivered using tkcalendar
    module.deliveryDate()

# rounding values to be accurate to dollars
    subtotal = round(subtotal, 2)
    afterTax = round(subtotal * tax, 2)
    totalCost = round(subtotal + afterTax + deliveryFee, 2)

# write receipt to file
    module.printReceipt(customer_order, costs, subtotal, afterTax, deliveryFee, totalCost)

# printing out receipt
    print("-----------RECEIPT-----------")
# know the values for costs to print
    i = len(costs)
    # prints product, amount, and cost
    for x in customer_order:
        print(x + " (" + str(customer_order[x]) + ")     $" + str(round(costs[-i], 2)))
    print("-----------------------------")
    print("Subtotal: $" + str(subtotal))
    print("Tax: $" + str(afterTax))
    print("Delivery fee: $" + str(deliveryFee))
    print("Total: $" + str(totalCost))
    print("-----------------------------")
    print("Thank you for ordering from us!")


