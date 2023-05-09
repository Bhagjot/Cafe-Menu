# version_1.py
# This is the first iteration of the Cafe Menu application.
# B.Singh 09/04/2023

# json library is imported
import json

# account.json file is opened which stores the login information
accounts = json.load(open("accounts.json", "r"))

# These variables hold the quantity of each item available for sale
nachos = 0
quiches = 0
chicken_burgers = 0
sushi = 0

# These variables hold the price of each item available for sale
nachos_price = 4.8
quiches_price = 4.8
chicken_burgers_price = 4.8
sushi_price = 5.8

# These variables hold the total prices of each item available for sale
nachos_total_price = 0
quiches_total_price = 0
chicken_burgers_total_price = 0
sushi_total_price = 0
total_price = 0

# This function is the main routine which the user interacts with first
def main_routine():
    while True:
        # These are options listed for the user to choose
        print("\n1. Login\n2. Create an account\n3. Exit")
        option = input("\nPlease select and option above: ")
        
        # This is when the user wants to log in to their account
        if option == "1":
            login()
            break

        # This is when the user wants to create an account
        elif option == "2":
            create_account()
            break

        # This is when the user wants to exit the program
        elif option == "3":
            print("\nThanks for using the Cafe Menu Application!")
            break

        # This is when the user inputs and invalid input
        else:
            print("Try again!")

# This function is called if the user wants to log in to their account
def login():
    while True:
        # This is where the username is asked
        username = input("\nUsername: ")

        # This is where the username is in the file
        if username in accounts:
            # This is where the password is asked
            password = input("Password: ")

            #This is where the password is correct
            if password == accounts.get(username, None):
                menu()
                break
            
            # This is where if the password is incorrect
            else:
                print("\nWhat would you like to do?")
                main_routine()
                break

        # This is where the username is not in the file
        else:
            print(f"\nThere is no account created with the username: {username}\nWhat would you like to do?")
            main_routine()
            break

# This functio nis called if the user wants to create an account
def create_account():
    global accounts

    while True:
        try:
            # This is where the user's age is asked
            user_age = int(input("What is your age? "))

            # This is where the age is checked if it meets the requirements
            if user_age >= 13 and user_age <=18:
                username = input("\nPlease choose an username: ")

                # This is where the username is taken
                if username in accounts:
                    print(f"\nThe username {username} is taken.\nWhat would you like to do?")
                    main_routine()
                    break

                # This is where the username is not taken
                else:
                    password = input("Please choose a password: ")
                    accounts[username] = password
                    json.dump(accounts, open("accounts.json", "w"))
                    print("\nAccount created successfully.")
                    main_routine()
                    break

            # This is where the user's age does not meet the requirements 
            else:
                print("Age must be between 13 to 18 to create an account.\nThanks for using the Cafe Menu Application!")
                break

        # This is where the user's age is invalid
        except ValueError:
            print("\nThat is not a valid age. What would you like to do?")
            main_routine()
            break

# This function is called when the user has logged in to their account
def menu():
    while True:
        option_chosen = input("\nYou are now logged in, what would you like to do?\n1. View Menu and add items to basket\n2. View Basket\n3. Exit\nPlease select an option above: ")

        # This is if the user wants to view the total
        if option_chosen == "1":
            add_to_basket()
            break

        # This is if the user wants to order
        elif option_chosen == "2":
            view_basket()
            break

        # This is if the user wants to exit
        elif option_chosen == "3":
            print("\nThanks for using the Cafe Menu Application!")
            break

        # This is if the user inputs something invalid
        else:
            print("\nPlease input numbers: 1, 2, or 3")

# This function is called if the user wants to view the menu and add items to basket
def add_to_basket():
    # All variables are called to use in this function
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

    # This is where the items avaible to sale and other options are displayed
    while True:
        try:
            print("\nItems for sale:\n1. Nachos (v) ${:.2f}\n2. Quiches - varied (v) ${:.2f}\n3. Chicken Burger ${:.2f}\n4. Sushi Box (g) ${:.2f}\n5. View Basket\n6. Exit".format(nachos_price, quiches_price, chicken_burgers_price, sushi_price))
            order = int(input("\nPlease enter a number from above to add to basket: "))

            # This is when the user wants to order Nachos
            if order == 1:
                quantity = int(input("\nHow many Nacho boxes would you like to order? "))
                nachos += quantity
                nachos_total_price += nachos * nachos_price

            # This is when the user wants to order Quiches
            elif order == 2:
                quantity = int(input("\nHow many Quiches would you like to order? "))
                quiches += quantity
                quiches_total_price += quiches * quiches_price
                    
                # This is when the user wants to order Chicken Burgers
            elif order == 3:
                quantity = int(input("\nHow many Chicken Burgers would you like to order? "))
                chicken_burgers += quantity
                chicken_burgers_total_price += chicken_burgers * chicken_burgers_price

                # This is when the user wants to order Sushi
            elif order == 4:
                quantity = int(input("\nHow many Sushi boxes would you like to order? "))
                sushi += quantity
                sushi_total_price += sushi * sushi_price

            # This is when the user wants to view the basket
            elif order == 5:
                view_basket()
                break
            
            # This is when the user wants to exit the program
            elif order == 6:
                print("\nThanks for using the Cafe Menu Application!")
                break

            else:
                print("\nPlease enter 1, 2, 3, 4, 5, or 6.\n")
                
        # This is if the user inputs something invalid
        except ValueError:
            print("\nPlease enter 1, 2, 3, 4, 5, or 6.\n")

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
        exit_view_basket = input("\nWhat would you like to do?\n1. View Menu\n2. Exit\nPlease select an option above: ")
        if exit_view_basket == "1":
            add_to_basket()
            break

        elif exit_view_basket == "2":
            print("\nThanks for using the Cafe Menu Application!")
            break

        else:
            print("\nPlease type 1 or 2.\n")

# This is so the program can not be run through another program
if __name__ == "__main__":
    print("Welcome to the Cafe Menu Application!")
    main_routine()