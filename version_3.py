# version_3.py
# This is the third iteration of the Cafe Menu application.
# B.Singh 22/04/2023

# Libraries are imported for using GUI and external files
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import json

# The external file holds the account logins of the users
accounts = json.load(open("accounts.json", "r"))

# This is where the GUI is created
root = Tk()
root.title("Cafe Menu")
root.geometry("300x350")

# These are the variables which store the quantity, price, and total_prices of each item
items = [
    "Nachos", 
    "Quiches", 
    "Chicken Burgers", 
    "Sushi", 
    "Pizza", 
    "Water", 
    "Ice Tea", 
    "Slushies"
    ]
item_quantities = [0, 0, 0, 0, 0, 0, 0, 0]
item_prices = [4.8, 4.8, 4.8, 5.8, 3.8, 3.5, 4.5, 2.5]
item_total_prices = [0, 0, 0, 0, 0, 0, 0, 0]

# This is the main routine
def main_frame():
    global main_frame

    # Here the main routine frame is created
    main_frame = Frame(root)
    main_frame.grid()
    menu_frame.grid_forget()

    # Image is located, resized, and set as a variable
    front_image_file = Image.open("front_image.jpg")
    front_image_resized = front_image_file.resize((290,193))
    front_image = ImageTk.PhotoImage(front_image_resized)

    # The image is now converted in to a label
    front_image_label = Label(main_frame, image=front_image)
    front_image_label.image = front_image

    # Welcome message label is created
    welcome_message = Label(main_frame, text="Welcome to the Cafe Menu application!")
    
    # Buttons are created for the actions the user can do
    login_button = Button(main_frame, text="Login", command=login_frame)
    create_account_button = Button(main_frame, text="Create Account", command=create_account_frame)

    # All the labels and buttons are called here
    front_image_label.grid()
    welcome_message.grid()
    login_button.grid()
    create_account_button.grid()

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
            access_label.configure(text="Account does not exist.")

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

                    elif username == "":
                        valid_label.configure(text="Please type an username.")
                        break

                    # This is where the password is saved to the username in the external file
                    else:
                        if password_entry.get() == "":
                            valid_label.configure(text="Please type a password.")
                            break

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

# This is where the the user gets to when they login, 
# they can choose options to add items to basket, view the basket or to logout
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

    # This is when the user clicks the add button
    def add_function():
        global items
        global item_quantities

        # This is where the program checks what is selected and adds the quantity
        i = 0
        for item_for_sale in items:
            if items_combobox.get() == item_for_sale:
                item_quantities[i] += int(quantity_combobox.get())
            else:
                i += 1

    # This is when the user can remove items from the basket
    def remove_function():
        global items
        global item_quantities

        # This is where the program checks what was selected and substracts the quantity
        i = 0
        for item_for_sale in items:
            if items_combobox.get() == item_for_sale:
                item_quantities[i] -= int(quantity_combobox.get())
                # If the quantity is negative, it is changed to zero
                if item_quantities[i] < 0:
                    item_quantities[i] = 0
            else:
                i += 1

    # This is where the user can leave the add to basket frame
    def back_function():
        root.title("Menu")
        menu_frame.grid()
        add_items_frame.grid_forget()

    # This is where the lists are created for the comboboxes to use
    quantity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Here are the labels created of the items so the user knows what they can order
    items_label = Label(add_items_frame, text="Items")
    item_1_label = Label(add_items_frame, text=items[0])
    item_2_label = Label(add_items_frame, text=items[1])
    item_3_label = Label(add_items_frame, text=items[2])
    item_4_label = Label(add_items_frame, text=items[3])
    item_5_label = Label(add_items_frame, text=items[4])
    item_6_label = Label(add_items_frame, text=items[5])
    item_7_label = Label(add_items_frame, text=items[6])
    item_8_label = Label(add_items_frame, text=items[7])

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
    items_price_label = Label(add_items_frame, text="Price")
    item_1_price_label = Label(add_items_frame, text="${:.2f}".format(item_prices[0]))
    item_2_price_label = Label(add_items_frame, text="${:.2f}".format(item_prices[1]))
    item_3_price_label = Label(add_items_frame, text="${:.2f}".format(item_prices[2]))
    item_4_price_label = Label(add_items_frame, text="${:.2f}".format(item_prices[3]))
    item_5_price_label = Label(add_items_frame, text="${:.2f}".format(item_prices[4]))
    item_6_price_label = Label(add_items_frame, text="${:.2f}".format(item_prices[5]))
    item_7_price_label = Label(add_items_frame, text="${:.2f}".format(item_prices[6]))
    item_8_price_label = Label(add_items_frame, text="${:.2f}".format(item_prices[7]))

    # Here are all the labels, comboboxes, and buttons displayed
    column_0_widgets = [
        items_label, 
        item_1_label, 
        item_2_label, 
        item_3_label, 
        item_4_label, 
        item_5_label, 
        item_6_label, 
        item_7_label, 
        item_8_label, 
        items_combobox, 
        add_button, 
        back_button
        ]
    
    column_1_widgets = [
        items_price_label, 
        item_1_price_label, 
        item_2_price_label, 
        item_3_price_label, 
        item_4_price_label, 
        item_5_price_label, 
        item_6_price_label, 
        item_7_price_label, 
        item_8_price_label, 
        quantity_combobox, 
        remove_button
        ]

    i = 0
    r = 0
    for label in column_0_widgets:
        column_0_widgets[i].grid(row=r, column=0)
        i += 1
        r += 1

    i = 0
    r = 0
    for label in column_1_widgets:
        column_1_widgets[i].grid(row=r, column=1)
        i += 1
        r += 1

# This is where the user can view what they have ordered
def view_basket_frame():
    global view_basket_frame
    global total_price
    global items

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
    total_price = 0
    i = 0
    for item in items:
        item_total_prices[i] = item_quantities[i] * item_prices[i]
        total_price += item_total_prices[i]
        i += 1

    # This is where the labels are created to show the items
    items_label = Label(view_basket_frame, text="Items")
    item_1_label = Label(view_basket_frame, text=items[0])
    item_2_label = Label(view_basket_frame, text=items[1])
    item_3_label = Label(view_basket_frame, text=items[2])
    item_4_label = Label(view_basket_frame, text=items[3])
    item_5_label = Label(view_basket_frame, text=items[4])
    item_6_label = Label(view_basket_frame, text=items[5])
    item_7_label = Label(view_basket_frame, text=items[6])
    item_8_label = Label(view_basket_frame, text=items[7])
    item_labels = [
        item_1_label, 
        item_2_label, 
        item_3_label, 
        item_4_label, 
        item_5_label, 
        item_6_label, 
        item_7_label, 
        item_8_label
        ]

    # This is where the button is created to leave
    back_button = Button(view_basket_frame, text="Back", command=back_function)
    order_button = Button(view_basket_frame, text="Order", command=order_function)

    # This is where the labels are created to show the quantity of each item
    quantity_label = Label(view_basket_frame, text="Quantity")
    item_1_quantity_label = Label(view_basket_frame, text=f"{item_quantities[0]}")
    item_2_quantity_label = Label(view_basket_frame, text=f"{item_quantities[1]}")
    item_3_quantity_label = Label(view_basket_frame, text=f"{item_quantities[2]}")
    item_4_quantity_label = Label(view_basket_frame, text=f"{item_quantities[3]}")
    item_5_quantity_label = Label(view_basket_frame, text=f"{item_quantities[4]}")
    item_6_quantity_label = Label(view_basket_frame, text=f"{item_quantities[5]}")
    item_7_quantity_label = Label(view_basket_frame, text=f"{item_quantities[6]}")
    item_8_quantity_label = Label(view_basket_frame, text=f"{item_quantities[7]}")
    item_quantity_labels = [
        item_1_quantity_label, 
        item_2_quantity_label, 
        item_3_quantity_label, 
        item_4_quantity_label, 
        item_5_quantity_label, 
        item_6_quantity_label, 
        item_7_quantity_label, 
        item_8_quantity_label
        ]

    # This is where the labels are created to show the price of each item
    price_label = Label(view_basket_frame, text="Price each")
    item_1_price_label = Label(view_basket_frame, text="${:.2f}".format(item_prices[0]))
    item_2_price_label = Label(view_basket_frame, text="${:.2f}".format(item_prices[1]))
    item_3_price_label = Label(view_basket_frame, text="${:.2f}".format(item_prices[2]))
    item_4_price_label = Label(view_basket_frame, text="${:.2f}".format(item_prices[3]))
    item_5_price_label = Label(view_basket_frame, text="${:.2f}".format(item_prices[4]))
    item_6_price_label = Label(view_basket_frame, text="${:.2f}".format(item_prices[5]))
    item_7_price_label = Label(view_basket_frame, text="${:.2f}".format(item_prices[6]))
    item_8_price_label = Label(view_basket_frame, text="${:.2f}".format(item_prices[7]))
    item_price_labels = [
        item_1_price_label, 
        item_2_price_label, 
        item_3_price_label, 
        item_4_price_label, 
        item_5_price_label, 
        item_6_price_label, 
        item_7_price_label, 
        item_8_price_label
        ]

    # This is where the labels are created to show the total prices of each item
    total_prices_label = Label(view_basket_frame, text="Total Prices")
    item_1_total_price_label = Label(view_basket_frame, text="${:.2f}".format(item_total_prices[0]))
    item_2_total_price_label = Label(view_basket_frame, text="${:.2f}".format(item_total_prices[1]))
    item_3_total_price_label = Label(view_basket_frame, text="${:.2f}".format(item_total_prices[2]))
    item_4_total_price_label = Label(view_basket_frame, text="${:.2f}".format(item_total_prices[3]))
    item_5_total_price_label = Label(view_basket_frame, text="${:.2f}".format(item_total_prices[4]))
    item_6_total_price_label = Label(view_basket_frame, text="${:.2f}".format(item_total_prices[5]))
    item_7_total_price_label = Label(view_basket_frame, text="${:.2f}".format(item_total_prices[6]))
    item_8_total_price_label = Label(view_basket_frame, text="${:.2f}".format(item_total_prices[7]))
    item_total_price_labels = [
        item_1_total_price_label, 
        item_2_total_price_label, 
        item_3_total_price_label, 
        item_4_total_price_label, 
        item_5_total_price_label, 
        item_6_total_price_label, 
        item_7_total_price_label, 
        item_8_total_price_label
        ]

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

# This is where the program only displays the item if the item was ordered
    i = 0
    c = 0
    r = 1
    for item in items:
        if item_quantities[i] > 0:
            item_labels[i].grid(row=r, column=c)
            item_quantity_labels[i].grid(row=r, column=(c+1))
            item_price_labels[i].grid(row=r, column=(c+2))
            item_total_price_labels[i].grid(row=r, column=(c+3))
            i += 1
            r += 1
        else:
            i += 1

# This is where program is called to make sure it can only be run through the terminal 
# and not through another program for a safety measure.
if __name__ == "__main__":
    # The menu frame is called incase through the usages of the program, 
    # the user wants to re-login after logging out
    menu_frame()
    main_frame()

# This is where the GUI is ended
root.mainloop()