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

# This list store the items avaible for sale
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

# These are lists which store the quantities, prices and total prices for each item available for sale
item_quantities = [0, 0, 0, 0, 0, 0, 0, 0]
item_prices = [4.8, 4.8, 4.8, 5.8, 3.8, 3.5, 4.5, 2.5]
item_total_prices = [0, 0, 0, 0, 0, 0, 0, 0]

# This is the main routine
def main_frame():
    global main_frame

    # Here the main routine frame is created
    main_frame = Frame(root)
    main_frame.grid()

    # Image is located, resized, and set as a variable
    front_image_file = Image.open("front_image.jpg")
    front_image_resized = front_image_file.resize((290,193))
    front_image = ImageTk.PhotoImage(front_image_resized)

    # The image is now converted in to a label
    front_image_label = Label(main_frame, image=front_image)
    front_image_label.image = front_image

    # Welcome message label is created
    welcome_message = Label(main_frame, text="Welcome to the Cafe Menu application!", font=20)
    
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

    # This is where the image is resized to display on the login page
    profile_image_file = Image.open("profile_image.png")
    profile_image_resized = profile_image_file.resize((200,200))
    profile_image = ImageTk.PhotoImage(profile_image_resized)

    # This is where the username is checked
    def login_function():
        global accounts
        username = username_entry.get()
        password = password_entry.get()

        if username in accounts:
            # This is where the password is checked
            if password == accounts.get(username, None):
                menu_frame_function()
                login_frame.grid_forget()
            
            elif password == "":
                access_label.configure(text="Please type a password.")
                
            else:
                access_label.configure(text="Incorrect password.")

        elif username == "":
            access_label.configure(text="Please type an username.")

        else:
            access_label.configure(text="Account does not exist.")

    # This is how the user can leave the login frame
    def back_function():
        root.title("Cafe Menu")
        main_frame.grid()
        login_frame.grid_forget()

    # This is where the image in converted into a label
    profile_image_label = Label(login_frame, image=profile_image)
    profile_image_label.image = profile_image

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
    profile_image_label.grid(row=0, column=0, columnspan=2)
    username_label.grid(row=1, column=0)
    password_label.grid(row=2, column=0)
    login_button.grid(row=3, column=0)
    access_label.grid(row=4, column=0, columnspan=2)
    username_entry.grid(row=1, column=1)
    password_entry.grid(row=2, column=1)
    back_button.grid(row=3, column=1)

# This is where the user can create their account
def create_account_frame():
    global create_account_frame

    # This is where the frame is created for the user to create their account
    root.title("Create Account")
    create_account_frame = Frame(root)
    create_account_frame.grid()
    main_frame.grid_forget()

    # This is where the profile image is resized
    profile_image_file = Image.open("profile_image.png")
    profile_image_resized = profile_image_file.resize((200,200))
    profile_image = ImageTk.PhotoImage(profile_image_resized)

    def create_account_function():
        global accounts

        # This is where the users age is checked to make sure they are allowed to create an account
        while True:
            try:
                age = int(age_entry.get())
                if age >= 13 and age <= 18:
                    username = username_entry.get()
                    password = password_entry.get()

                    # This is where the username is checked if it is taken
                    if username in accounts:
                        valid_label.configure(text="Username taken.")
                        break

                    elif username == "":
                        valid_label.configure(text="Please type an username.")
                        break

                    elif " " in username:
                        valid_label.configure(text="Space is not allowed in username.")
                        break

                    # This is where the password is saved to the username in the external file
                    else:
                        if password == "":
                            valid_label.configure(text="Please type a password.")
                            break

                        elif " " in password:
                            valid_label.configure(text="Space is not allowed in password.")
                            break

                        else:
                            accounts[username] = password_entry.get()
                            json.dump(accounts, open("accounts.json", "w"))
                            valid_label.configure(text="Account created")
                            login_button.grid(row=5, column=0)
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

    def login_function():
        root.title("Login")
        login_frame()
        create_account_frame.grid_forget()

    # This is where the profile image is converted into a label
    profile_image_label = Label(create_account_frame, image=profile_image)
    profile_image_label.image = profile_image

    # These are the labels which help indentify where the user should input
    age_label = Label(create_account_frame, text="Age")
    username_label = Label(create_account_frame, text="Username")
    password_label = Label(create_account_frame, text="Password")
    valid_label = Label(create_account_frame)

    # These are the buttons where the user can submit or leave
    create_button = Button(create_account_frame, text="Create", command=create_account_function)
    back_button = Button(create_account_frame, text="Back", command=back_function)
    login_button = Button(create_account_frame, text="Go to login", command=login_function)

    # These are the entries where the user can input
    age_entry = Entry(create_account_frame)
    username_entry = Entry(create_account_frame)
    password_entry = Entry(create_account_frame)

    # This is where all the labels, buttons and entries are called
    profile_image_label.grid(row=0, column=0, columnspan=2)
    age_label.grid(row=1, column=0)
    username_label.grid(row=2, column=0)
    password_label.grid(row=3, column=0)
    create_button.grid(row=4, column=0)
    back_button.grid(row=5, column=0)
    age_entry.grid(row=1, column=1)
    username_entry.grid(row=2, column=1)
    password_entry.grid(row=3, column=1)
    valid_label.grid(row=4, column=1, columnspan=2)

# This is where the the user gets to when they login, 
# they can choose options to add items to basket, view the basket or to logout
def menu_frame_function():
    global menu_frame_function
    global menu_frame

    # This is where the menu frame is created
    root.title("Menu")
    menu_frame = Frame(root)
    menu_frame.grid()

    # This is the function which allows the user to logout
    def logout_function():
        main_frame.grid()
        menu_frame.grid_forget()

    # This is where the menu image is resized
    menu_image_file = Image.open("menu_image.jpg")
    menu_image_resized = menu_image_file.resize((208,117))
    menu_image = ImageTk.PhotoImage(menu_image_resized)

    # This is where teh menu image in covnerted into a label
    menu_image_label = Label(menu_frame, image=menu_image)
    menu_image_label.image = menu_image

    # This is where the label is created to tell the user to select an option
    option_label = Label(menu_frame, text="Please choose an option below.")

    # These are the option buttons being created
    add_items_button = Button(menu_frame, text="Add items to basket", command=add_items_frame_function)
    view_basket_button = Button(menu_frame, text="View basket", command=view_basket_frame_function)
    logout_button = Button(menu_frame, text="Logout", command=logout_function)

    # This is where all the labels and buttons are called
    menu_image_label.grid()
    option_label.grid()
    add_items_button.grid()
    view_basket_button.grid()
    logout_button.grid()

# This is where the user can add items to their basket
def add_items_frame_function():
    global add_items_frame_function
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
        try:
            # This is where the program checks what is selected and adds the quantity
            i = 0
            for item_for_sale in items:
                quantity = int(quantity_combobox.get())
                if items_combobox.get() == item_for_sale:
                    item_quantities[i] += quantity
                    inform_label.configure(text=f"{quantity} {item_for_sale} added.")
                else:
                    i += 1
        except ValueError:
            inform_label.configure(text="Please choose quantity")

    # This is when the user can remove items from the basket
    def remove_function():
        global items
        global item_quantities
        try:
            # This is where the program checks what was selected and substracts the quantity
            i = 0
            for item_for_sale in items:
                quantity = int(quantity_combobox.get())
                if items_combobox.get() == item_for_sale:
                    item_quantities[i] -= quantity
                    inform_label.configure(text=f"{quantity} {item_for_sale} removed.")
                    # If the quantity is negative, it is changed to zero
                    if item_quantities[i] < 0:
                        item_quantities[i] = 0
                else:
                    i += 1
        except ValueError:
            inform_label.configure(text="Please choose quantity")

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
    quantity_combobox.set("Select quantity")

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

    # Here the label for informing the user about their actions is created
    inform_label = Label(add_items_frame)

    # Here all the labels are displayed
    items_label.grid(row=0, column=0) 
    item_1_label.grid(row=1, column=0) 
    item_2_label.grid(row=2, column=0) 
    item_3_label.grid(row=3, column=0) 
    item_4_label.grid(row=4, column=0) 
    item_5_label.grid(row=5, column=0) 
    item_6_label.grid(row=6, column=0) 
    item_7_label.grid(row=7, column=0) 
    item_8_label.grid(row=8, column=0) 
    items_combobox.grid(row=9, column=0) 
    add_button.grid(row=10, column=0) 
    back_button.grid(row=11, column=0)
    items_price_label.grid(row=0, column=1) 
    item_1_price_label.grid(row=1, column=1) 
    item_2_price_label.grid(row=2, column=1) 
    item_3_price_label.grid(row=3, column=1) 
    item_4_price_label.grid(row=4, column=1) 
    item_5_price_label.grid(row=5, column=1) 
    item_6_price_label.grid(row=6, column=1) 
    item_7_price_label.grid(row=7, column=1) 
    item_8_price_label.grid(row=8, column=1) 
    quantity_combobox.grid(row=9, column=1) 
    remove_button.grid(row=10, column=1)
    inform_label.grid(row=11, column=1)

# This is where the user can view what they have ordered
def view_basket_frame_function():
    global view_basket_frame_function
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
        if total_price > 0:
            order_state_label.configure(text="Order sent!")
        else:
            order_state_label.configure(text="Please add item/s to basket.")

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
    order_state_label.grid(row=6, column=0, columnspan=3)
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
    main_frame()

# This is where the GUI is ended
root.mainloop()