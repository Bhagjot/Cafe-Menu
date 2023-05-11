# version_4.py
# This is the fourth iteration of the Cafe Menu application.
# B.Singh 10/05/2023

# Libraries are imported for using GUI and external files
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import json

# The external file holds the account logins of the users
accounts = json.load(open("accounts.json", "r"))

# This is where the GUI is created
root = Tk()
root.geometry("315x390")
root.configure(bg="#ffffff")

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
def main_function():
    global main_function
    global main_frame

    # Here the main routine frame is created
    main_frame = Frame(root)
    main_frame.grid()
    main_frame.configure(bg="#ffffff")
    root.title("Cafe Menu Application")

    # Image is located, resized, and set as a variable
    front_image = ImageTk.PhotoImage(Image.open("front_image.jpg").resize((300,200)))

    # The image is now converted in to a label
    front_image_label = Label(main_frame, bg="#ffffff", image=front_image)
    front_image_label.image = front_image

    # Welcome message label is created
    welcome_message = Label(
        main_frame, 
        text="Welcome to the Cafe Menu application!", 
        font=("Helvetica", 12, "bold"), 
        bg="#ffffff"
        )
    
    # Buttons are created for the actions the user can do
    login_button = Button(
        main_frame, 
        text="Login", 
        fg="#ffffff", 
        bg="#55c2da", 
        font=("Helvetica", 10, "bold"), 
        height=2, 
        width=15, 
        command=login_function
        )
    
    create_account_button = Button(
        main_frame, 
        text="Create Account", 
        fg="#ffffff", 
        bg="#55c2da", 
        font=("Helvetica", 10, "bold"), 
        height=2, 
        width=15, 
        command=create_account_function
        )

    # All the labels and buttons are called here
    front_image_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    welcome_message.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    login_button.grid(row=2, column=0, padx=5, pady=5)
    create_account_button.grid(row=2, column=1, padx=5, pady=5)

# This is the how the user can login
def login_function():
    global login_function
    global login_frame

    # This is where the login frame is created
    root.title("Login")
    login_frame = Frame(root)
    login_frame.grid()
    main_frame.grid_forget()
    login_frame.configure(bg="#ffffff")

    # This is where the username is checked
    def login_button_function():
        global accounts

        if username_entry.get() in accounts:
            # This is where the password is checked
            if password_entry.get() == accounts.get(username_entry.get(), None):
                options_function()
                login_frame.grid_forget()
            else:
                access_label.configure(text="Invalid Password")
        else:
            access_label.configure(text="Invalid Username")

    # This is how the user can leave the login frame
    def create_account_button_function():
        create_account_function()
        login_frame.grid_forget()
    
    # This is where the image is resized to display on the login page
    profile_image = ImageTk.PhotoImage(Image.open("profile_image.png").resize((100,100)))

    # This is where the image in converted into a label
    profile_image_label = Label(login_frame, bg="#ffffff", image=profile_image)
    profile_image_label.image = profile_image

    # This is where the Labels are created for the user to see where to input
    username_label = Label(login_frame, text="Username", bg="#ffffff", font=10)
    password_label = Label(login_frame, text="Password", bg="#ffffff", font=10)
    access_label = Label(login_frame, bg="#ffffff", font=10)

    # This is where the user can input
    username_entry = Entry(login_frame, bg="#ffffff", width=20)
    password_entry = Entry(login_frame, show="*", bg="#ffffff", width=20)

    # These are the buttons to submit or leave
    login_button = Button(
        login_frame, 
        text="Login", 
        fg="#ffffff", 
        bg="#55c2da", 
        font=("Helvetica", 10, "bold"), 
        width=17, 
        command=login_button_function
        )
    
    create_account_button = Button(
        login_frame, 
        text="Go to create account", 
        fg="#ffffff", 
        bg="#55c2da", 
        font=("Helvetica", 10, "bold"), 
        width=17, 
        command=create_account_button_function
        )

    # Here all the labels, entries and buttons are called
    profile_image_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    username_label.grid(row=1, column=0, padx=5, pady=5)
    password_label.grid(row=2, column=0, padx=5, pady=5)
    create_account_button.grid(row=3, column=0, padx=5, pady=5)
    access_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
    username_entry.grid(row=1, column=1, padx=5, pady=5)
    password_entry.grid(row=2, column=1, padx=5, pady=5)
    login_button.grid(row=3, column=1, padx=5, pady=5)

# This is where the user can create their account
def create_account_function():
    global create_account_function
    global create_account_frame

    # This is where the frame is created for the user to create their account
    root.title("Create Account")
    create_account_frame = Frame(root)
    create_account_frame.grid()
    main_frame.grid_forget()
    create_account_frame.configure(bg="#ffffff")

    def create_button_function():
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
                        valid_label.configure(text="Username taken")
                        break
                    elif username == "":
                        valid_label.configure(text="Please type an username")
                        break
                    # This is where the password is saved to the username in the external file
                    else:
                        if password == "":
                            valid_label.configure(text="Please type a password")
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
    def login_button_function():
        login_function()
        create_account_frame.grid_forget()

    # This is where the profile image is resized
    profile_image = ImageTk.PhotoImage(Image.open("profile_image.png").resize((100,100)))

    # This is where the profile image is converted into a label
    profile_image_label = Label(create_account_frame, bg="#ffffff", image=profile_image)
    profile_image_label.image = profile_image

    # These are the labels which help indentify where the user should input
    age_label = Label(create_account_frame, text="Age", bg="#ffffff", font=10)
    username_label = Label(create_account_frame, text="Username", bg="#ffffff", font=10)
    password_label = Label(create_account_frame, text="Password", bg="#ffffff", font=10)
    valid_label = Label(create_account_frame, bg="#ffffff", font=10)

    # These are the buttons where the user can submit or leave
    create_button = Button(
        create_account_frame, 
        text="Create",
        fg="#ffffff", 
        bg="#55c2da", 
        font=("Helvetica", 10, "bold"), 
        width=17,  
        command=create_button_function
        )
    
    login_button = Button(
        create_account_frame, 
        text="Go to login",
        fg="#ffffff", 
        bg="#55c2da", 
        font=("Helvetica", 10, "bold"), 
        width=17,  
        command=login_button_function
        )

    # These are the entries where the user can input
    age_entry = Entry(create_account_frame, bg="#ffffff", width=20)
    username_entry = Entry(create_account_frame, bg="#ffffff", width=20)
    password_entry = Entry(create_account_frame, bg="#ffffff", width=20)

    # This is where all the labels, buttons and entries are called
    profile_image_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    age_label.grid(row=1, column=0, padx=5, pady=5)
    username_label.grid(row=2, column=0, padx=5, pady=5)
    password_label.grid(row=3, column=0, padx=5, pady=5)
    login_button.grid(row=4, column=0, padx=5, pady=5)
    valid_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
    age_entry.grid(row=1, column=1, padx=5, pady=5)
    username_entry.grid(row=2, column=1, padx=5, pady=5)
    password_entry.grid(row=3, column=1, padx=5, pady=5)
    create_button.grid(row=4, column=1, padx=5, pady=5)

# This is where the the user gets to when they login, 
# they can choose options to add items to basket, view the basket or to logout
def options_function():
    global options_function
    global options_frame

    # This is where the menu frame is created
    root.title("Menu")
    options_frame = Frame(root)
    options_frame.grid()
    options_frame.configure(bg="#ffffff")

    def menu_button_function():
        menu_function()
        options_frame.grid_forget()

    def view_basket_button_function():
        basket_function()
        options_frame.grid_forget()

    # This is where the menu image is resized
    menu_image = ImageTk.PhotoImage(Image.open("menu_image.jpg").resize((300,169)))

    # This is where teh menu image in covnerted into a label
    menu_image_label = Label(options_frame, bg="#ffffff", image=menu_image)
    menu_image_label.image = menu_image

    # These are the option buttons being created
    add_items_button = Button(
        options_frame, 
        text="View Menu",
        fg="#ffffff", 
        bg="#55c2da", 
        font=("Helvetica", 10, "bold"), 
        height=2, 
        width=15,  
        command=menu_button_function
        )
    
    view_basket_button = Button(
        options_frame, 
        text="View basket",
        fg="#ffffff", 
        bg="#55c2da", 
        font=("Helvetica", 10, "bold"), 
        height=2, 
        width=15,  
        command=view_basket_button_function
        )

    # This is where all the labels and buttons are called
    menu_image_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    add_items_button.grid(row=1, column=0, padx=5, pady=5)
    view_basket_button.grid(row=1, column=1, padx=5, pady=5)

# This is where the user can add items to their basket
def menu_function():
    global menu_function
    global menu_frame
    global items
    global item_quantities

    # This is where the frame is created so the user can add items to the basket
    root.title("Menu")
    menu_frame = Frame(root)
    menu_frame.grid()
    menu_frame.configure(bg="#ffffff")

    # This is when the user clicks the add button
    def add_button_function():
        i = 0
        for item in items:
            if item == items_combobox.get():
                try:
                    item_quantities[i] += int(quantity_combobox.get())
                    inform_label.configure(text=f"{quantity_combobox.get()} {item} added.")
                except ValueError:
                    inform_label.configure(text="Please choose quantity")
            else:
                i += 1

    # This is when the user can remove items from the basket
    def remove_button_function():
        i = 0
        for item in items:
            if item == items_combobox.get():
                try:
                    item_quantities[i] -= int(quantity_combobox.get())
                    if item_quantities[i] < 0:
                        item_quantities[i] = 0
                    inform_label.configure(text=f"{item_quantities[i]} {item} remaining.")
                except ValueError:
                    inform_label.configure(text="Please choose quantity")
            else:
                i += 1

    # This is where the user can leave the add to basket frame
    def view_basket_button_function():
        basket_function()
        menu_frame.grid_forget()

    # This is where the lists are created for the comboboxes to use
    quantity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Here are the labels created of the items so the user knows what they can order
    items_label = Label(menu_frame, text="Items", font=("Helvetica", 12, "bold"), bg="#ffffff")
    item_1_label = Label(menu_frame, text=items[0], bg="#ffffff")
    item_2_label = Label(menu_frame, text=items[1], bg="#ffffff")
    item_3_label = Label(menu_frame, text=items[2], bg="#ffffff")
    item_4_label = Label(menu_frame, text=items[3], bg="#ffffff")
    item_5_label = Label(menu_frame, text=items[4], bg="#ffffff")
    item_6_label = Label(menu_frame, text=items[5], bg="#ffffff")
    item_7_label = Label(menu_frame, text=items[6], bg="#ffffff")
    item_8_label = Label(menu_frame, text=items[7], bg="#ffffff")

    # Here are the comboboxes created so the user can select the items
    items_combobox = ttk.Combobox(menu_frame, value=items)
    items_combobox.set("Choose item")
    quantity_combobox = ttk.Combobox(menu_frame, value=quantity)
    quantity_combobox.set("Choose quantity")

    # Here are the buttons created so the user can submite their order or leave
    add_button = Button(
        menu_frame, 
        text="Add", 
        fg="#ffffff", 
        bg="#55c2da", 
        font=("Helvetica", 10, "bold"), 
        width=15, 
        command=add_button_function
        )
    
    back_button = Button(
        menu_frame, 
        text="View Basket", 
        fg="#ffffff", 
        bg="#55c2da", 
        font=("Helvetica", 10, "bold"), 
        width=15, 
        command=view_basket_button_function
        )
    
    remove_button = Button(
        menu_frame, 
        text="Remove", 
        fg="#ffffff", 
        bg="#55c2da", 
        font=("Helvetica", 10, "bold"), 
        width=15, 
        command=remove_button_function
        )

    # Here are the labels created to show the prices of the items
    items_price_label = Label(menu_frame, text="Price", font=("Helvetica", 12, "bold"), bg="#ffffff")
    item_1_price_label = Label(menu_frame, text="${:.2f}".format(item_prices[0]), bg="#ffffff")
    item_2_price_label = Label(menu_frame, text="${:.2f}".format(item_prices[1]), bg="#ffffff")
    item_3_price_label = Label(menu_frame, text="${:.2f}".format(item_prices[2]), bg="#ffffff")
    item_4_price_label = Label(menu_frame, text="${:.2f}".format(item_prices[3]), bg="#ffffff")
    item_5_price_label = Label(menu_frame, text="${:.2f}".format(item_prices[4]), bg="#ffffff")
    item_6_price_label = Label(menu_frame, text="${:.2f}".format(item_prices[5]), bg="#ffffff")
    item_7_price_label = Label(menu_frame, text="${:.2f}".format(item_prices[6]), bg="#ffffff")
    item_8_price_label = Label(menu_frame, text="${:.2f}".format(item_prices[7]), bg="#ffffff")

    # Here the label for informing the user about their actions is created
    inform_label = Label(menu_frame, bg="#ffffff")

    # Here all the labels are displayed
    items_label.grid(row=0, column=0, padx=5, pady=5) 
    item_1_label.grid(row=1, column=0, sticky=W, padx=5, pady=5) 
    item_2_label.grid(row=2, column=0, sticky=W, padx=5, pady=5) 
    item_3_label.grid(row=3, column=0, sticky=W, padx=5, pady=5) 
    item_4_label.grid(row=4, column=0, sticky=W, padx=5, pady=5) 
    item_5_label.grid(row=5, column=0, sticky=W, padx=5, pady=5) 
    item_6_label.grid(row=6, column=0, sticky=W, padx=5, pady=5) 
    item_7_label.grid(row=7, column=0, sticky=W, padx=5, pady=5) 
    item_8_label.grid(row=8, column=0, sticky=W, padx=5, pady=5) 
    items_combobox.grid(row=9, column=0, padx=5, pady=5) 
    add_button.grid(row=10, column=0, padx=5, pady=5) 
    back_button.grid(row=11, column=0, padx=5, pady=5)
    items_price_label.grid(row=0, column=1, padx=5, pady=5) 
    item_1_price_label.grid(row=1, column=1, padx=5, pady=5) 
    item_2_price_label.grid(row=2, column=1, padx=5, pady=5) 
    item_3_price_label.grid(row=3, column=1, padx=5, pady=5) 
    item_4_price_label.grid(row=4, column=1, padx=5, pady=5) 
    item_5_price_label.grid(row=5, column=1, padx=5, pady=5) 
    item_6_price_label.grid(row=6, column=1, padx=5, pady=5) 
    item_7_price_label.grid(row=7, column=1, padx=5, pady=5) 
    item_8_price_label.grid(row=8, column=1, padx=5, pady=5) 
    quantity_combobox.grid(row=9, column=1, padx=5, pady=5) 
    remove_button.grid(row=10, column=1, padx=5, pady=5)
    inform_label.grid(row=11, column=1, padx=5, pady=5)

# This is where the user can view what they have ordered
def basket_function():
    global basket_function
    global basket_frame
    global total_price
    global items

    # This is where the frame is created for the user to view what they have ordered
    root.title("Basket")
    root.geometry("400x370")
    basket_frame = Frame(root)
    basket_frame.grid()
    basket_frame.configure(bg="#ffffff")

    # This is the function which allows the user to leave
    def menu_button_function():
        root.geometry("315x390")
        menu_function()
        basket_frame.grid_forget()

    def order_button_function():
        if total_price > 0:
            messagebox.showinfo(title="Order status", message="Order sent!")
        else:
            messagebox.showinfo(title="Order status", message="You have not ordered anything.")

    # This is where the totals are found
    total_price = 0
    i = 0
    for item in items:
        item_total_prices[i] = item_quantities[i] * item_prices[i]
        total_price += item_total_prices[i]
        i += 1

    # This is where the labels are created to show the items
    items_label = Label(basket_frame, text="Items", bg="#ffffff", font=10)
    item_1_label = Label(basket_frame, text=items[0], bg="#ffffff")
    item_2_label = Label(basket_frame, text=items[1], bg="#ffffff")
    item_3_label = Label(basket_frame, text=items[2], bg="#ffffff")
    item_4_label = Label(basket_frame, text=items[3], bg="#ffffff")
    item_5_label = Label(basket_frame, text=items[4], bg="#ffffff")
    item_6_label = Label(basket_frame, text=items[5], bg="#ffffff")
    item_7_label = Label(basket_frame, text=items[6], bg="#ffffff")
    item_8_label = Label(basket_frame, text=items[7], bg="#ffffff")
    
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
    add_items_button = Button(
        basket_frame, 
        text="Menu", 
        fg="#ffffff", 
        bg="#55c2da", 
        font=("Helvetica", 10, "bold"), 
        width=5,
        command=menu_button_function
        )
    
    order_button = Button(
        basket_frame, 
        text="Order", 
        fg="#ffffff", 
        bg="#55c2da", 
        font=("Helvetica", 10, "bold"), 
        width=5, 
        command=order_button_function
        )

    # This is where the labels are created to show the quantity of each item
    quantity_label = Label(basket_frame, text="Quantity", bg="#ffffff", font=10)
    item_1_quantity_label = Label(basket_frame, text=f"{item_quantities[0]}", bg="#ffffff")
    item_2_quantity_label = Label(basket_frame, text=f"{item_quantities[1]}", bg="#ffffff")
    item_3_quantity_label = Label(basket_frame, text=f"{item_quantities[2]}", bg="#ffffff")
    item_4_quantity_label = Label(basket_frame, text=f"{item_quantities[3]}", bg="#ffffff")
    item_5_quantity_label = Label(basket_frame, text=f"{item_quantities[4]}", bg="#ffffff")
    item_6_quantity_label = Label(basket_frame, text=f"{item_quantities[5]}", bg="#ffffff")
    item_7_quantity_label = Label(basket_frame, text=f"{item_quantities[6]}", bg="#ffffff")
    item_8_quantity_label = Label(basket_frame, text=f"{item_quantities[7]}", bg="#ffffff")
    
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
    price_label = Label(basket_frame, text="Price each", bg="#ffffff", font=10)
    item_1_price_label = Label(basket_frame, text="${:.2f}".format(item_prices[0]), bg="#ffffff")
    item_2_price_label = Label(basket_frame, text="${:.2f}".format(item_prices[1]), bg="#ffffff")
    item_3_price_label = Label(basket_frame, text="${:.2f}".format(item_prices[2]), bg="#ffffff")
    item_4_price_label = Label(basket_frame, text="${:.2f}".format(item_prices[3]), bg="#ffffff")
    item_5_price_label = Label(basket_frame, text="${:.2f}".format(item_prices[4]), bg="#ffffff")
    item_6_price_label = Label(basket_frame, text="${:.2f}".format(item_prices[5]), bg="#ffffff")
    item_7_price_label = Label(basket_frame, text="${:.2f}".format(item_prices[6]), bg="#ffffff")
    item_8_price_label = Label(basket_frame, text="${:.2f}".format(item_prices[7]), bg="#ffffff")
    
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
    total_prices_label = Label(basket_frame, text="Total Prices", bg="#ffffff", font=10)
    item_1_total_price_label = Label(basket_frame, text="${:.2f}".format(item_total_prices[0]), bg="#ffffff")
    item_2_total_price_label = Label(basket_frame, text="${:.2f}".format(item_total_prices[1]), bg="#ffffff")
    item_3_total_price_label = Label(basket_frame, text="${:.2f}".format(item_total_prices[2]), bg="#ffffff")
    item_4_total_price_label = Label(basket_frame, text="${:.2f}".format(item_total_prices[3]), bg="#ffffff")
    item_5_total_price_label = Label(basket_frame, text="${:.2f}".format(item_total_prices[4]), bg="#ffffff")
    item_6_total_price_label = Label(basket_frame, text="${:.2f}".format(item_total_prices[5]), bg="#ffffff")
    item_7_total_price_label = Label(basket_frame, text="${:.2f}".format(item_total_prices[6]), bg="#ffffff")
    item_8_total_price_label = Label(basket_frame, text="${:.2f}".format(item_total_prices[7]), bg="#ffffff")
    
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
    total_label = Label(basket_frame, text="Total:", bg="#ffffff", font=10)
    total_price_label = Label(basket_frame, text="${:.2f}".format(total_price), bg="#ffffff", font=10)

    # This is where the labels and buttons which always show are called
    items_label.grid(row=0, column=0, padx=5, pady=5)
    add_items_button.grid(row=9, column=0, padx=5, pady=5)
    quantity_label.grid(row=0, column=1, padx=5, pady=5)
    order_button.grid(row=9, column=1, padx=5, pady=5)
    price_label.grid(row=0, column=2, padx=5, pady=5)
    total_label.grid(row=9, column=2, padx=5, pady=5)
    total_prices_label.grid(row=0, column=3, padx=5, pady=5)
    total_price_label.grid(row=9, column=3, padx=5, pady=5)

# This is where the program only displays the item if the item was ordered
    i = 0
    c = 0
    r = 1
    for item in items:
        if item_quantities[i] > 0:
            item_labels[i].grid(row=r, column=c, padx=5, pady=5)
            item_quantity_labels[i].grid(row=r, column=(c+1), padx=5, pady=5)
            item_price_labels[i].grid(row=r, column=(c+2), padx=5, pady=5)
            item_total_price_labels[i].grid(row=r, column=(c+3), padx=5, pady=5)
            i += 1
            r += 1
        else:
            i += 1

# This is where program is called to make sure it can only be run through the terminal 
# and not through another program for a safety measure.
if __name__ == "__main__":
    main_function()

# This is where the GUI is ended
root.mainloop()