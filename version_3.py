# version_3.py
# This is the third iteration of the Cafe Menu application.
# B.Singh 22/04/2023

# Libraries are imported for using GUI and external files
from tkinter import *
from tkinter import ttk
import json

# The external file holds the account logins of the users
accounts = json.load(open("accounts.json", "r"))

# This is where the GUI is created
root = Tk()
root.title("Cafe Menu")
root.geometry("300x200")

# These are the variables which store the quantity, price, and total_prices of each item
nachos = 0
quiches = 0
chicken_burgers = 0
sushi = 0
nachos_price = 4.80
quiches_price = 4.80
chicken_burgers_price = 4.80
sushi_price = 5.80

# This is the main routine
def main_frame():
    global main_frame

    # Here the main routine frame is created
    main_frame = Frame(root)
    main_frame.grid()
    menu_frame.grid_forget()

    # Welcome message label is created
    welcome_message = Label(main_frame, text="Welcome to the Cafe Menu application!")
    
    # Buttons are created for the actions the user can do
    login_button = Button(main_frame, text="Login", command=login_frame)
    create_account_button = Button(main_frame, text="Create Account", command=create_account_frame)

    # All the labels and buttons are called here
    welcome_message.pack(padx=5, pady=5)
    login_button.pack(padx=5, pady=5)
    create_account_button.pack(padx=5, pady=5)

# This is the how the user can login
def login_frame():
    global login_frame

    # This is where the login frame is created
    root.title("Login")
    login_frame = Frame(root)
    login_frame.grid()
    main_frame.grid_forget()

    # This is where the username is checked
    def login_function():
        global accounts
        if username_entry.get() in accounts:

            # This is where the password is checked
            if password_entry.get() == accounts.get(username_entry.get(), None):
                menu_frame.grid()
                login_frame.grid_forget()
            else:
                access_label.configure(text="Incorrect password.")
        else:
            access_label.configure(text="Account does not exist")

    # This is how the user can leave the login frame
    def back_function():
        root.title("Cafe Menu")
        main_frame.grid()
        login_frame.grid_forget()

    # This is where the Labels are created for the user to see where to input
    username_label = Label(login_frame, text="Username")
    password_label = Label(login_frame, text="Password")
    access_label = Label(login_frame)

    # This is where the user can input
    username_entry = Entry(login_frame)
    password_entry = Entry(login_frame, show="*")

    # These are the buttons to submit or leave
    login_button = Button(login_frame, text="Login", command=login_function)
    back_button = Button(login_frame, text="Back", command=back_function)

    # Here all the labels, entries and buttons are called
    username_label.grid(row=0, column=0)
    password_label.grid(row=1, column=0)
    login_button.grid(row=2, column=0)
    access_label.grid(row=3, column=0)
    username_entry.grid(row=0, column=1)
    password_entry.grid(row=1, column=1)
    back_button.grid(row=2, column=1)

# This is where the user can create their account
def create_account_frame():
    global create_account_frame

    # This is where the frame is created for the user to create their account
    root.title("Create Account")
    create_account_frame = Frame(root)
    create_account_frame.grid()
    main_frame.grid_forget()

    def create_account_function():
        global accounts

        # This is where the users age is checked to make sure they are allowed to create an account
        while True:
            try:
                age = int(age_entry.get())
                if age >= 13 and age <= 18:
                    username = username_entry.get()

                    # This is where the username is checked if it is taken
                    if username in accounts:
                        valid_label.configure(text="Username taken.")
                        break

                    # This is where the password is saved to the username in the external file
                    else:
                        accounts[username] = password_entry.get()
                        json.dump(accounts, open("accounts.json", "w"))
                        valid_label.configure(text="Account created")
                        break
                
                # This is the message the user receives if the user is not allowed to create an account
                else:
                    valid_label.configure(text="You are not allowed to create an account.")
                    break

            # This is the message the user receives if the user inputs an invalid age 
            except ValueError:
                valid_label.configure(text="Invalid age.")
                break

    # This is where the user can leave the create account frame
    def back_function():
        root.title("Cafe Menu")
        main_frame.grid()
        create_account_frame.grid_forget()

    # These are the labels which help indentify where the user should input
    age_label = Label(create_account_frame, text="Age")
    username_label = Label(create_account_frame, text="Username")
    password_label = Label(create_account_frame, text="Password")
    valid_label = Label(create_account_frame)

    # These are the buttons where the user can submit or leave
    create_button = Button(create_account_frame, text="Create", command=create_account_function)
    back_button = Button(create_account_frame, text="Back", command=back_function)

    # These are the entries where the user can input
    age_entry = Entry(create_account_frame)
    username_entry = Entry(create_account_frame)
    password_entry = Entry(create_account_frame)

    # This is where all the labels, buttons and entries are called
    age_label.grid(row=0, column=0)
    username_label.grid(row=1, column=0)
    password_label.grid(row=2, column=0)
    create_button.grid(row=3, column=0)
    back_button.grid(row=4, column=0)
    age_entry.grid(row=0, column=1)
    username_entry.grid(row=1, column=1)
    password_entry.grid(row=2, column=1)
    valid_label.grid(row=3, column=1)

# This is where the the user gets to when they login, they can choose options to add items to basket, view the basket or to logout
def menu_frame():
    global menu_frame

    # This is where the menu frame is created
    root.title("Menu")
    menu_frame = Frame(root)
    menu_frame.grid()

    # This is the function which allows the user to logout
    def logout_function():
        main_frame.grid()
        menu_frame.grid_forget()

    # This is where the label is created to tell the user to select an option
    option_label = Label(menu_frame, text="Please choose an option below.")

    # These are the option buttons being created
    add_items_button = Button(menu_frame, text="Add items to basket", command=add_items_frame)
    view_basket_button = Button(menu_frame, text="View basket", command=view_basket_frame)
    logout_button = Button(menu_frame, text="Logout", command=logout_function)

    # This is where all the labels and buttons are called
    option_label.pack()
    add_items_button.pack()
    view_basket_button.pack()
    logout_button.pack()

# This is where the user can add items to their basket
def add_items_frame():
    global add_items_frame

    # This is where the frame is created so the user can add items to the basket
    root.title("Add items to basket")
    add_items_frame = Frame(root)
    add_items_frame.grid()
    menu_frame.grid_forget()

    # This is where the user clicks the add button
    def add_function():
        global nachos
        global quiches
        global chicken_burgers
        global sushi

        # This is where the program checks what is selected and adds the quantity
        if items_combobox.get() == "Nachos":
            nachos += int(quantity_combobox.get())

        elif items_combobox.get() == "Quiches":
            quiches += int(quantity_combobox.get())
        
        elif items_combobox.get() == "Chicken Burgers":
            chicken_burgers += int(quantity_combobox.get())
        
        elif items_combobox.get() == "Sushi":
            sushi += int(quantity_combobox.get())

    # This is where the user can remove items from the list so they do not order anything on accident
    def remove_function():
        global nachos
        global quiches
        global chicken_burgers
        global sushi

        # This is where the program checks what was selected and substracts the quantity, if the item goes into negatives it changes it to zero
        if items_combobox.get() == "Nachos":
            nachos -= int(quantity_combobox.get())
            if nachos < 0:
                nachos = 0

        elif items_combobox.get() == "Quiches":
            quiches -= int(quantity_combobox.get())
            if quiches < 0:
                quiches = 0
        
        elif items_combobox.get() == "Chicken Burgers":
            chicken_burgers -= int(quantity_combobox.get())
            if chicken_burgers < 0:
                chicken_burgers = 0
        
        elif items_combobox.get() == "Sushi":
            sushi -= int(quantity_combobox.get())
            if sushi < 0:
                sushi = 0

    # This is where the user can leave the add to basket frame
    def back_function():
        root.title("Menu")
        menu_frame.grid()
        add_items_frame.grid_forget()

    # This is where the lists are created for the comboboxes to use
    items = ["Nachos", "Quiches", "Chicken Burgers", "Sushi"]
    quantity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Here are the labels created of the items so the user knows what they can order
    nachos_label = Label(add_items_frame, text="Nachos")
    quiches_label = Label(add_items_frame, text="Quiches")
    chicken_burgers_label = Label(add_items_frame, text="Chicken Burgers")
    sushi_label = Label(add_items_frame, text="Sushi")

    # Here are the comboboxes created so the user can select the items
    items_combobox = ttk.Combobox(add_items_frame, value=items)
    items_combobox.set("Select an item")
    quantity_combobox = ttk.Combobox(add_items_frame, value=quantity)
    quantity_combobox.set("Select an amount")

    # Here are the buttons created so the user can submite their order or leave
    add_button = Button(add_items_frame, text="Add", command=add_function)
    back_button = Button(add_items_frame, text="Back", command=back_function)
    remove_button = Button(add_items_frame, text="Remove", command=remove_function)

    # Here are the labels created to show the prices of the items
    nachos_price_label = Label(add_items_frame, text="${:.2f}".format(nachos_price))
    quiches_price_label = Label(add_items_frame, text="${:.2f}".format(quiches_price))
    chicken_burgers_price_label = Label(add_items_frame, text="${:.2f}".format(chicken_burgers_price))
    sushi_price_label = Label(add_items_frame, text="${:.2f}".format(sushi_price))

    # Here are all teh labels, comboboxes, and buttons called
    nachos_label.grid(row=0, column=0)
    quiches_label.grid(row=1, column=0)
    chicken_burgers_label.grid(row=2, column=0)
    sushi_label.grid(row=3, column=0)
    items_combobox.grid(row=4, column=0)
    add_button.grid(row=5, column=0)
    back_button.grid(row=6, column=0)
    nachos_price_label.grid(row=0, column=1)
    quiches_price_label.grid(row=1, column=1)
    chicken_burgers_price_label.grid(row=2, column=1)
    sushi_price_label.grid(row=3, column=1)
    quantity_combobox.grid(row=4, column=1)
    remove_button.grid(row=5, column=1)

# This is where the user can view what they have ordered
def view_basket_frame():
    global view_basket_frame

    # This is where the frame is created for the user to view what they have ordered
    root.title("View Basket")
    view_basket_frame = Frame(root)
    view_basket_frame.grid()
    menu_frame.grid_forget()

    # This is the function which allows the user to leave
    def back_function():
        root.title("Menu")
        menu_frame.grid()
        view_basket_frame.grid_forget()

    def order_function():
        order_state_label.configure(text="Order sent!")

    # This is where the totals are found
    nachos_total_price = nachos * nachos_price
    quiches_total_price = quiches * quiches_price
    chicken_burgers_total_price = chicken_burgers * chicken_burgers_price
    sushi_total_price = sushi * sushi_price
    total_price = nachos_total_price + quiches_total_price + chicken_burgers_total_price + sushi_total_price

    # This is where the labels are created to show the items
    items_label = Label(view_basket_frame, text="Items")
    nachos_label = Label(view_basket_frame, text="Nachos")
    quiches_label = Label(view_basket_frame, text="Quiches")
    chicken_burgers_label = Label(view_basket_frame, text="Chicken Burgers")
    sushi_label = Label(view_basket_frame, text="Sushi")

    # This is where the button is created to leave
    back_button = Button(view_basket_frame, text="Back", command=back_function)
    order_button = Button(view_basket_frame, text="Order", command=order_function)

    # This is where the labels are created to show the quantity of each item
    quantity_label = Label(view_basket_frame, text="Quantity")
    nachos_quantity_label = Label(view_basket_frame, text=f"{nachos}")
    quiches_quantity_label = Label(view_basket_frame, text=f"{quiches}")
    chicken_burgers_quantity_label = Label(view_basket_frame, text=f"{chicken_burgers}")
    sushi_quantity_label = Label(view_basket_frame, text=f"{sushi}")

    # This is where the labels are created to show the price of each item
    price_label = Label(view_basket_frame, text="Price each")
    nachos_price_label = Label(view_basket_frame, text="${:.2f}".format(nachos_price))
    quiches_price_label = Label(view_basket_frame, text="${:.2f}".format(quiches_price))
    chicken_burgers_price_label = Label(view_basket_frame, text="${:.2f}".format(chicken_burgers_price))
    sushi_price_label = Label(view_basket_frame, text="${:.2f}".format(sushi_price))

    # This is where the labels are created to show the total prices of each item
    total_prices_label = Label(view_basket_frame, text="Total Prices")
    nachos_total_price_label = Label(view_basket_frame, text="${:.2f}".format(nachos_total_price))
    quiches_total_price_label = Label(view_basket_frame, text="${:.2f}".format(quiches_total_price))
    chicken_burgers_total_price_label = Label(view_basket_frame, text="${:.2f}".format(chicken_burgers_total_price))
    sushi_total_price_label = Label(view_basket_frame, text="${:.2f}".format(sushi_total_price))

    # This is where the label is created to show the total
    total_label = Label(view_basket_frame, text="Total:")
    total_price_label = Label(view_basket_frame, text="${:.2f}".format(total_price))

    # This is where the state of the order is displayed
    order_state_label = Label(view_basket_frame)

    # This is where the labels and buttons which always show are called
    items_label.grid(row=0, column=0)
    back_button.grid(row=5, column=0)
    order_state_label.grid(row=6, column=0)
    quantity_label.grid(row=0, column=1)
    order_button.grid(row=5, column=1)
    price_label.grid(row=0, column=2)
    total_label.grid(row=5, column=2)
    total_prices_label.grid(row=0, column=3)
    total_price_label.grid(row=5, column=3)

    # This is where it is checked if the user ordered this item, if not then the labels for this item will not show
    if nachos > 0:
        nachos_label.grid(row=1, column=0)
        nachos_quantity_label.grid(row=1, column=1)
        nachos_price_label.grid(row=1, column=2)
        nachos_total_price_label.grid(row=1, column=3)

    # This is where it is checked if the user ordered this item, if not then the labels for this item will not show
    if quiches > 0:
        quiches_label.grid(row=2, column=0)
        quiches_quantity_label.grid(row=2, column=1)
        quiches_price_label.grid(row=2, column=2)
        quiches_total_price_label.grid(row=2, column=3)

    # This is where it is checked if the user ordered this item, if not then the labels for this item will not show
    if chicken_burgers > 0:
        chicken_burgers_label.grid(row=3, column=0)
        chicken_burgers_quantity_label.grid(row=3, column=1)
        chicken_burgers_price_label.grid(row=3, column=2)
        chicken_burgers_total_price_label.grid(row=3, column=3)

    # This is where it is checked if the user ordered this item, if not then the labels for this item will not show
    if sushi > 0:
        sushi_label.grid(row=4, column=0)
        sushi_quantity_label.grid(row=4, column=1)
        sushi_price_label.grid(row=4, column=2)
        sushi_total_price_label.grid(row=4, column=3)

# This is where program is called to make sure it can only be run through the terminal and not through another program for a safety measure.
if __name__ == "__main__":
    # The menu frame is called incase through the usages of the program, the user wants to re-login after logging out
    menu_frame()
    main_frame()

# This is where the GUI is ended
root.mainloop()