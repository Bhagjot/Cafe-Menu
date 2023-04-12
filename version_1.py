# version_1.py
# This is the first iteration of the Cafe Menu application.
# B.Singh 09/04/2023

# json is imported to use an external file to store account details
import json

# account.json is imported as a dictionary
accounts = json.load(open("accounts.json", "r"))

# Variables which hold the quantity of items
nachos = 0
quiches = 0
chicken_burgers = 0
sushi = 0

# Variables which hold the price of the items
nachos_price = 4.8
quiches_price = 4.8
chicken_burgers_price = 4.8
sushi_price = 5.8

# Variables which hold the total prices
nachos_total_price = 0
quiches_total_price = 0
chicken_burgers_total_price = 0
sushi_total_price = 0
total_price = 0

# This is the main routine
def main_routine():
    while True:
        print("\nWelcome to the Cafe Menu Application!\n\n1. Login\n2. Create an account\n3. Exit")
        option = input("\nPlease select and option above: ")
        
        # This is when the user wants to log in
        if option == "1":
            login()

        # This is when the user wants to create an account
        elif option == "2":
            create_account()

        # This is when the user wants to exit the program
        elif option == "3":
            quit()

        # This is when the user inputs and invalid input
        else:
            print("Try again!")

# This is the function which works when the user wants to login
def login():
    while True:
        username = input("\nUsername: ")

        # This is where the username is checked 
        if username in accounts:
            password = input("Password: ")

            #This is where the user's password is checked
            if password == accounts.get(username, None):
                menu()
            # This is where if the password is incorrect
            else:
                print("\nInvalid password. Try again!")
                login()

        # This is where the username does not exist
        else:
            try_again = input(f"\nThere is no account with {username} as a username. Do you want to try again? (y/n) ")
            if try_again == "y":
                pass
            else:
                main_routine()

# This is when the user wants to create an account
def create_account():
    global accounts

    while True:
        try:
            # This is where the user's age is being checked
            user_age = int(input("What is your age? "))

            # This is when the user's age is valid
            if user_age >= 13 and user_age <=18:
                username = input("\nPlease choose an username: ")

                # This is where the username is taken
                if username in accounts:
                    try_again = input(f"\nThe username {username} is taken. Do you want to try again? (y/n) ")
                    if try_again == "y":
                        pass   
                    else:
                        main_routine()

                # This is where the username is not taken
                else:
                    password = input("Please choose a password: ")
                    accounts[username] = password
                    json.dump(accounts, open("accounts.json", "w"))
                    print("\nAccount created successfully.")
                    main_routine()
            # This is where the user does not meet the prerequisites 
            else:
                print("You can not create an account.")
                main_routine()
        # This is where the user's age is unvalid
        except ValueError or SyntaxError or IndexError:
            print("\nTry again")

# This is where the user can select if they want to order or view the total
def menu():
    while True:
        option_chosen = input("\n1. View basket\n2. Add to basket\n3. Exit\nPlease select an option above: ")

        # This is if the user wants to view the total
        if option_chosen == "1":
            view_basket()

        # This is if the user wants to order
        elif option_chosen == "2":
            add_to_basket()

        # This is if the user wants to exit
        elif option_chosen == "3":
            main_routine()

        # This is if the user inputs something invalid
        else:
            print("\nTry again!")

# This is where the user can view the total
def view_basket():
    # This is where variables are received which are required to get the total
    global nachos_total_price
    global quiches_total_price
    global chicken_burgers_total_price
    global sushi_total_price
    global total_price

    # This is where the total price is found
    total_price += nachos_total_price + quiches_total_price + chicken_burgers_total_price + sushi_total_price

    # This is where the total prices of each itemare outputed
    while True:
        if nachos > 0:
            print("\nYou ordered {} Nacho boxes which totaled ${:.2f}.".format(sushi, sushi_total_price))
        if quiches > 0:
            print("You ordered {} Quiches which totaled ${:.2f}.".format(quiches, quiches_total_price))
        if chicken_burgers > 0:
            print("You ordered {} Chicken Burgers which totaled ${:.2f}.".format(chicken_burgers, chicken_burgers_total_price))
        if sushi > 0:
            print("You ordered {} Sushi boxes which totaled ${:.2f}.".format(sushi, sushi_total_price))

        # This is if there is nothing in the basket
        if nachos == 0 and quiches == 0 and chicken_burgers == 0 and sushi == 0:
            print("\nYou did not order anything")

        # This is where the total price is outputed
        print("\nThe total price is ${:.2f}".format(total_price))

        # This is so the user can leave
        exit_view_basket = input("\nDo you want to leave? (y/n) ")
        if exit_view_basket == "y":
            menu()

# This is where the user can order items
def add_to_basket():
    # These are all the vriables retrieved which need to be updated when something is added to the basket
    global nachos
    global nachos_price
    global nachos_total_price
    global quiches
    global quiches_price
    global quiches_total_price
    global chicken_burgers
    global chicken_burgers_price
    global chicken_burgers_total_price
    global sushi
    global sushi_price
    global sushi_total_price

    # This is where the menu is displayed
    try:
        while True:
            print("\nItems for sale:\n1. Nachos (v) ${:.2f}\n2. Quiches - varied (v) ${:.2f}\n3. Chicken Burger ${:.2f}\n4. Sushi Box (g) ${:.2f}\n5. Exit".format(nachos_price, quiches_price, chicken_burgers_price, sushi_price))
            order = int(input("\nPlease enter a number from above: "))

            # This is if the user wants to order Nacho Boxes
            if order == 1:
                quantity = int(input("\nHow many Nacho boxes would you like to order? "))
                nachos += quantity
                nachos_total_price += nachos * nachos_price

            # This is if the user wants to order Quiches
            elif order == 2:
                quantity = int(input("\nHow many Quiches would you like to order? "))
                quiches += quantity
                quiches_total_price += quiches * quiches_price
                
            # This is if the user wants to order Chicken Burgers
            elif order == 3:
                quantity = int(input("\nHow many Chicken Burgers would you like to order? "))
                chicken_burgers += quantity
                chicken_burgers_total_price += chicken_burgers * chicken_burgers_price

            # This is if the user wants to order Sushi Boxes
            elif order == 4:
                quantity = int(input("\nHow many Sushi boxes would you like to order? "))
                sushi += quantity
                sushi_total_price += sushi * sushi_price

            # This is if the user wants to exit
            elif order == 5:
                menu()
            
    # This is if the user inputs something invalid
    except ValueError or SyntaxError or IndexError:
        print("\nTry again!")

# This is so the program can not be run through another program
if __name__ == "__main__":
    main_routine()