# version_5.py
# This is the fifth iteration of the Cafe Menu application.
# B.Singh 12/05/2023

# Libraries are imported to use GUI, images, and external files
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import json

# If the external file is not present, it is created, else it is simply read
json.dump({}, open("accounts.json", "w"), indent=4)
accounts = json.load(open("accounts.json", "r"))

# The main widget is created with a set size and color
root = Tk()
root.geometry("315x390")
root.configure(bg="#ffffff")

# Lists are created which store items, their prices, quantities, and total prices
items = [ "Nachos", "Quiches", "Chicken Burgers", "Sushi", "Pizza", "Water", "Ice Tea", "Slushies"]
item_quantities = [0, 0, 0, 0, 0, 0, 0, 0]
item_prices = [4.8, 4.8, 4.8, 5.8, 3.8, 3.5, 4.5, 2.5]
item_total_prices = [0, 0, 0, 0, 0, 0, 0, 0]

# This is the main routine which is where the user can decide if they want to login or create an account
def main_function():
    global main_function
    global main_frame

    # Window title is changed and main frame is created
    root.title("Cafe Menu Application")
    main_frame = Frame(root)
    main_frame.grid()
    main_frame.configure(bg="#ffffff")

    # The front image and welcome message labels are created
    main_image = ImageTk.PhotoImage(Image.open("main_image.jpg"))
    main_image_label = Label(main_frame, bg="#ffffff", image=main_image)
    main_image_label.image = main_image
    welcome_message_label = Label(main_frame, text="Welcome to the Cafe Menu application!", font=("Helvetica", 12, "bold"), bg="#ffffff")
    
    # Login and create account buttons are created
    login_button = Button(main_frame, text="Login", fg="#ffffff", bg="#55c2da", font=("Helvetica", 10, "bold"), height=2, width=15, command=login_function)
    create_account_button = Button(main_frame, text="Create Account", fg="#ffffff", bg="#55c2da", font=("Helvetica", 10, "bold"), height=2, width=15, command=create_account_function)

    # All labels and buttons are displayed
    main_image_label.grid(row=0, column=0, columnspan=2, padx=5, pady=15)
    welcome_message_label.grid(row=1, column=0, columnspan=2, padx=5, pady=15)
    login_button.grid(row=2, column=0, padx=5, pady=15)
    create_account_button.grid(row=2, column=1, padx=5, pady=15)

# This is the login function where the user can login
def login_function():
    global login_function
    global login_frame

    # Window title is changed, login frame is created, main frame is forgotten
    root.title("Login")
    login_frame = Frame(root)
    login_frame.grid()
    login_frame.configure(bg="#ffffff")
    main_frame.grid_forget()

    # This is where credentials entered are checked
    def login_button_function():
        global accounts
        # This is where the username is checked
        if username_entry.get() in accounts:
            # This is where the password is checked
            if password_entry.get() == accounts.get(username_entry.get(), None):
                options_function()
                login_frame.grid_forget()
            else:
                access_label.configure(text="Invalid Password")
        else:
            access_label.configure(text="Invalid Username")

    # This is how the user can go to the create account frame
    def create_account_button_function():
        create_account_function()
        login_frame.grid_forget()
    
    # Profile image, username, password and access labels are created
    profile_image = ImageTk.PhotoImage(Image.open("login_image.png"))
    profile_image_label = Label(login_frame, bg="#ffffff", image=profile_image)
    profile_image_label.image = profile_image
    username_label = Label(login_frame, text="Username", bg="#ffffff", font=10)
    password_label = Label(login_frame, text="Password", bg="#ffffff", font=10)
    access_label = Label(login_frame, bg="#ffffff", font=10)

    # Username and password entries are created
    username_entry = Entry(login_frame, bg="#ffffff", width=20)
    password_entry = Entry(login_frame, show="*", bg="#ffffff", width=20)

    # Login and create account buttons are created
    login_button = Button(login_frame, text="Login", fg="#ffffff", bg="#55c2da", font=("Helvetica", 10, "bold"), height=2, width=17, command=login_button_function)
    create_account_button = Button(
        login_frame, 
        text="Go to create account", 
        fg="#ffffff", 
        bg="#55c2da", 
        font=("Helvetica", 10, "bold"), 
        height=2, 
        width=17, 
        command=create_account_button_function
        )

    # Labels, entries and buttons are created
    profile_image_label.grid(row=0, column=0, columnspan=2, padx=5, pady=20)
    username_label.grid(row=1, column=0, padx=5, pady=20)
    password_label.grid(row=2, column=0, padx=5, pady=20)
    create_account_button.grid(row=3, column=0, padx=5, pady=15)
    access_label.grid(row=4, column=0, columnspan=2, padx=5)
    username_entry.grid(row=1, column=1, padx=5, pady=20)
    password_entry.grid(row=2, column=1, padx=5, pady=20)
    login_button.grid(row=3, column=1, padx=5, pady=15)

# This is the create account function where the user can create an account
def create_account_function():
    global create_account_function
    global create_account_frame

    # Window title is changed, create account frame is created and main frame is forgotten
    root.title("Create Account")
    create_account_frame = Frame(root)
    create_account_frame.grid()
    create_account_frame.configure(bg="#ffffff")
    main_frame.grid_forget()

    # This is where the user's entries are checked
    def create_button_function():
        global accounts
        while True:
            try:
                # This is where the users age is checked if it meets the requirements
                age = int(age_entry.get())
                if age >= 13 and age <= 18:
                    username = username_entry.get()
                    password = password_entry.get()
                    # This is where the username is checked if it is taken
                    if username in accounts:
                        valid_label.configure(text="Username taken")
                        break
                    # This is where the username is checked to make sure the user did input something
                    elif username == "":
                        valid_label.configure(text="Please type an username")
                        break
                    # This is where the username is valid
                    else:
                        # This is where it is made sure that the user input something for a password
                        if password == "":
                            valid_label.configure(text="Please type a password")
                            break
                        # This is where the password is valid
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

    # This is where the user can go and login
    def login_button_function():
        login_function()
        create_account_frame.grid_forget()

    # Profile image, age, username, password, and valid labels are created
    profile_image = ImageTk.PhotoImage(Image.open("login_image.png"))
    profile_image_label = Label(create_account_frame, bg="#ffffff", image=profile_image)
    profile_image_label.image = profile_image
    age_label = Label(create_account_frame, text="Age", bg="#ffffff", font=10)
    username_label = Label(create_account_frame, text="Username", bg="#ffffff", font=10)
    password_label = Label(create_account_frame, text="Password", bg="#ffffff", font=10)
    valid_label = Label(create_account_frame, bg="#ffffff", font=10)

    # age, username and password entries are created
    age_entry = Entry(create_account_frame, bg="#ffffff", width=20)
    username_entry = Entry(create_account_frame, bg="#ffffff", width=20)
    password_entry = Entry(create_account_frame, bg="#ffffff", width=20)

    # Create and accounts and go to login buttons are created
    create_button = Button(create_account_frame, text="Create",fg="#ffffff", bg="#55c2da", font=("Helvetica", 10, "bold"), height=2, width=17,  command=create_button_function)
    login_button = Button(create_account_frame, text="Go to login",fg="#ffffff", bg="#55c2da", font=("Helvetica", 10, "bold"), height=2, width=17,  command=login_button_function)

    # All the labels, buttons, and entries are created
    profile_image_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)
    age_label.grid(row=1, column=0, padx=5, pady=15)
    username_label.grid(row=2, column=0, padx=5, pady=15)
    password_label.grid(row=3, column=0, padx=5, pady=15)
    login_button.grid(row=4, column=0, padx=5, pady=5)
    valid_label.grid(row=5, column=0, columnspan=2, padx=5)
    age_entry.grid(row=1, column=1, padx=5, pady=15)
    username_entry.grid(row=2, column=1, padx=5, pady=15)
    password_entry.grid(row=3, column=1, padx=5, pady=15)
    create_button.grid(row=4, column=1, padx=5, pady=5)

# This is where the user is sent when they have logged in, they can view the menu or basket
def options_function():
    global options_function
    global options_frame

    # Window title is changed and options frame is created
    root.title("Options")
    options_frame = Frame(root)
    options_frame.grid()
    options_frame.configure(bg="#ffffff")

    # This is where the user can view the menu
    def view_menu_button_function():
        menu_function()
        options_frame.grid_forget()

    # This is where the user can view the basket
    def view_basket_button_function():
        basket_function()
        options_frame.grid_forget()

    # Menu image label is created
    options_image = ImageTk.PhotoImage(Image.open("options_image.jpg"))
    options_image_label = Label(options_frame, bg="#ffffff", image=options_image)
    options_image_label.image = options_image

    # View menu and view basket buttons are created
    view_menu_button = Button(options_frame, text="View Menu",fg="#ffffff", bg="#55c2da", font=("Helvetica", 10, "bold"), height=2, width=15,  command=view_menu_button_function)
    view_basket_button = Button(options_frame, text="View basket",fg="#ffffff", bg="#55c2da", font=("Helvetica", 10, "bold"), height=2, width=15,  command=view_basket_button_function)

    # All labels and buttons are displayed
    options_image_label.grid(row=0, column=0, columnspan=2, padx=5, pady=30)
    view_menu_button.grid(row=1, column=0, padx=5, pady=30)
    view_basket_button.grid(row=1, column=1, padx=5, pady=30)

# This is where the user can view the menu and order items
def menu_function():
    global menu_function
    global menu_frame
    global items
    global item_quantities

    # Window title and size are changed and menu frame is created
    root.title("Menu")
    root.geometry("340x680")
    menu_frame = Frame(root)
    menu_frame.grid()
    menu_frame.configure(bg="#ffffff")

    # This is when the user wants to add an item
    def add_button_function(i):
        item_quantities[i] += 1
        inform_label.configure(text=f"There are now {item_quantities[i]} {items[i]}.")

    # This is when the user wants to view the basket
    def view_basket_button_function():
        basket_function()
        menu_frame.grid_forget()

    # This is where the lists are created for the comboboxes to use
    quantity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # All image labels are created
    item_1_image = ImageTk.PhotoImage(Image.open("nachos_image.jpg"))
    item_1_image_label = Label(menu_frame, bg="#ffffff", image=item_1_image)
    item_1_image_label.image = item_1_image
    
    item_2_image = ImageTk.PhotoImage(Image.open("quiches_image.jpg"))
    item_2_image_label = Label(menu_frame, bg="#ffffff", image=item_2_image)
    item_2_image_label.image = item_2_image
    
    item_3_image = ImageTk.PhotoImage(Image.open("chicken_burger_image.jpg"))
    item_3_image_label = Label(menu_frame, bg="#ffffff", image=item_3_image)
    item_3_image_label.image = item_3_image
    
    item_4_image = ImageTk.PhotoImage(Image.open("sushi_image.jpg"))
    item_4_image_label = Label(menu_frame, bg="#ffffff", image=item_4_image)
    item_4_image_label.image = item_4_image
    
    item_5_image = ImageTk.PhotoImage(Image.open("pizza_image.jpg"))
    item_5_image_label = Label(menu_frame, bg="#ffffff", image=item_5_image)
    item_5_image_label.image = item_5_image
    
    item_6_image = ImageTk.PhotoImage(Image.open("water_image.jpg"))
    item_6_image_label = Label(menu_frame, bg="#ffffff", image=item_6_image)
    item_6_image_label.image = item_6_image
    
    item_7_image = ImageTk.PhotoImage(Image.open("ice_tea_image.jpg"))
    item_7_image_label = Label(menu_frame, bg="#ffffff", image=item_7_image)
    item_7_image_label.image = item_7_image
    
    item_8_image = ImageTk.PhotoImage(Image.open("slushy_image.jpg"))
    item_8_image_label = Label(menu_frame, bg="#ffffff", image=item_8_image)
    item_8_image_label.image = item_8_image

    # All item name labels are created
    item_1_label = Label(menu_frame, text=items[0], bg="#ffffff")
    item_2_label = Label(menu_frame, text=items[1], bg="#ffffff")
    item_3_label = Label(menu_frame, text=items[2], bg="#ffffff")
    item_4_label = Label(menu_frame, text=items[3], bg="#ffffff")
    item_5_label = Label(menu_frame, text=items[4], bg="#ffffff")
    item_6_label = Label(menu_frame, text=items[5], bg="#ffffff")
    item_7_label = Label(menu_frame, text=items[6], bg="#ffffff")
    item_8_label = Label(menu_frame, text=items[7], bg="#ffffff")

    # All item price labels are created
    item_1_price_label = Label(menu_frame, text="${:.2f}".format(item_prices[0]), bg="#ffffff")
    item_2_price_label = Label(menu_frame, text="${:.2f}".format(item_prices[1]), bg="#ffffff")
    item_3_price_label = Label(menu_frame, text="${:.2f}".format(item_prices[2]), bg="#ffffff")
    item_4_price_label = Label(menu_frame, text="${:.2f}".format(item_prices[3]), bg="#ffffff")
    item_5_price_label = Label(menu_frame, text="${:.2f}".format(item_prices[4]), bg="#ffffff")
    item_6_price_label = Label(menu_frame, text="${:.2f}".format(item_prices[5]), bg="#ffffff")
    item_7_price_label = Label(menu_frame, text="${:.2f}".format(item_prices[6]), bg="#ffffff")
    item_8_price_label = Label(menu_frame, text="${:.2f}".format(item_prices[7]), bg="#ffffff")
 
    # Title and inform labels are created
    title_label = Label(menu_frame, bg="#ffffff", text="Cafe Menu", font=("Helvetica", 12, "bold"))
    inform_label = Label(menu_frame, bg="#ffffff")

    # Here are the comboboxes created so the user can select the items
    items_combobox = ttk.Combobox(menu_frame, value=items)
    items_combobox.set("Choose item")
    quantity_combobox = ttk.Combobox(menu_frame, value=quantity)
    quantity_combobox.set("Choose quantity")

    # Here are the buttons created so the user can submite their order or leave
    item_1_add_button = Button(menu_frame, text="Add Nachos", fg="#ffffff", bg="#55c2da", font=("Helvetica", 10, "bold"), width=15, command=lambda:add_button_function(0))
    item_2_add_button = Button(menu_frame,  text="Add Quiche", fg="#ffffff", bg="#55c2da", font=("Helvetica", 10, "bold"), width=15, command=lambda:add_button_function(1))
    item_3_add_button = Button(menu_frame, text="Add Chicken Burger", fg="#ffffff", bg="#55c2da", font=("Helvetica", 10, "bold"), width=15, command=lambda:add_button_function(2))
    item_4_add_button = Button(menu_frame, text="Add Sushi", fg="#ffffff", bg="#55c2da", font=("Helvetica", 10, "bold"), width=15, command=lambda:add_button_function(3))
    item_5_add_button = Button(menu_frame, text="Add Pizza", fg="#ffffff", bg="#55c2da", font=("Helvetica", 10, "bold"), width=15, command=lambda:add_button_function(4))
    item_6_add_button = Button(menu_frame, text="Add Water", fg="#ffffff", bg="#55c2da", font=("Helvetica", 10, "bold"), width=15, command=lambda:add_button_function(5))
    item_7_add_button = Button(menu_frame, text="Add Ice Tea", fg="#ffffff", bg="#55c2da", font=("Helvetica", 10, "bold"), width=15, command=lambda:add_button_function(6))
    item_8_add_button = Button(menu_frame, text="Add Slushy", fg="#ffffff", bg="#55c2da", font=("Helvetica", 10, "bold"), width=15, command=lambda:add_button_function(7))
    view_basket_button = Button(menu_frame, text="View Basket", fg="#ffffff", bg="#55c2da", font=("Helvetica", 10, "bold"), width=15, command=view_basket_button_function)

    # Item 1 labels and buttons are displayed
    item_1_image_label.grid(row=1, column=0, padx=10, pady=5)
    item_1_label.grid(row=2, column=0) 
    item_1_price_label.grid(row=3, column=0) 
    item_1_add_button.grid(row=4, column=0, padx=10, pady=5) 
    # Item 2 labels and buttons are displayed
    item_2_image_label.grid(row=5, column=0, padx=10, pady=5)
    item_2_label.grid(row=6, column=0) 
    item_2_price_label.grid(row=7, column=0) 
    item_2_add_button.grid(row=8, column=0, padx=10, pady=5) 
    # Item 3 labels and buttons are displayed
    item_3_image_label.grid(row=9, column=0, padx=10, pady=5)
    item_3_label.grid(row=10, column=0) 
    item_3_price_label.grid(row=11, column=0) 
    item_3_add_button.grid(row=12, column=0, padx=10, pady=5) 
    # Item 4 labels and buttons are displayed
    item_4_image_label.grid(row=13, column=0, padx=10, pady=5)
    item_4_label.grid(row=14, column=0) 
    item_4_price_label.grid(row=15, column=0) 
    item_4_add_button.grid(row=16, column=0, padx=10, pady=5) 
    # Item 5 labels and buttons are displayed
    item_5_image_label.grid(row=1, column=1, padx=10, pady=5)
    item_5_label.grid(row=2, column=1) 
    item_5_price_label.grid(row=3, column=1) 
    item_5_add_button.grid(row=4, column=1, padx=10, pady=5) 
    # Item 6 labels and buttons are displayed
    item_6_image_label.grid(row=5, column=1, padx=10, pady=5)
    item_6_label.grid(row=6, column=1) 
    item_6_price_label.grid(row=7, column=1) 
    item_6_add_button.grid(row=8, column=1, padx=10, pady=5) 
    # Item 7 labels and buttons are displayed
    item_7_image_label.grid(row=9, column=1, padx=10, pady=5)
    item_7_label.grid(row=10, column=1) 
    item_7_price_label.grid(row=11, column=1) 
    item_7_add_button.grid(row=12, column=1, padx=10, pady=5) 
    # Item 8 labels and buttons are displayed
    item_8_image_label.grid(row=13, column=1, padx=10, pady=5)
    item_8_label.grid(row=14, column=1) 
    item_8_price_label.grid(row=15, column=1) 
    item_8_add_button.grid(row=16, column=1, padx=10, pady=5) 
    # Title and inform labels are displayed, view basket button is displayed
    title_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    view_basket_button.grid(row=17, column=0, padx=5, pady=15)
    inform_label.grid(row=17, column=1, columnspan=2, padx=5, pady=15)

# This is how the user can view the basket
def basket_function():
    global basket_function
    global basket_frame
    global total_price
    global items
    global item_quantities

    # Window title and size is changed and basket frame is created
    root.title("Basket")
    root.geometry("500x500")
    basket_frame = Frame(root)
    basket_frame.grid()
    basket_frame.configure(bg="#ffffff")

    # This is how the user can view the menu
    def menu_button_function():
        root.geometry("330x680")
        menu_function()
        basket_frame.grid_forget()

    # This is how the user can order the item selected
    def order_button_function():
        update_button_function()
        if total_price > 0:
            messagebox.showinfo(title="Order status", message="Order sent!")
        else:
            messagebox.showinfo(title="Order status", message="You have not ordered anything.")
        
    # This is how the user can update the frame when they chenge teh item quantities
    def update_button_function():
        i = 0
        for item in item_values:
            try:
                item_quantities[i] = int(item.get())
                i += 1
            except ValueError:
                item_quantities[i] = 0
                i += 1

        basket_frame.grid_forget()
        basket_function()

    # This is where the total price for each item is found
    total_price = 0
    i = 0
    for item in items:
        item_total_prices[i] = item_quantities[i] * item_prices[i]
        total_price += item_total_prices[i]
        i += 1

    # Item name labels are created
    item_1_label = Label(basket_frame, text=items[0], bg="#ffffff")
    item_2_label = Label(basket_frame, text=items[1], bg="#ffffff")
    item_3_label = Label(basket_frame, text=items[2], bg="#ffffff")
    item_4_label = Label(basket_frame, text=items[3], bg="#ffffff")
    item_5_label = Label(basket_frame, text=items[4], bg="#ffffff")
    item_6_label = Label(basket_frame, text=items[5], bg="#ffffff")
    item_7_label = Label(basket_frame, text=items[6], bg="#ffffff")
    item_8_label = Label(basket_frame, text=items[7], bg="#ffffff")

    # Item price labels are created
    item_1_price_label = Label(basket_frame, text="${:.2f}".format(item_prices[0]), bg="#ffffff")
    item_2_price_label = Label(basket_frame, text="${:.2f}".format(item_prices[1]), bg="#ffffff")
    item_3_price_label = Label(basket_frame, text="${:.2f}".format(item_prices[2]), bg="#ffffff")
    item_4_price_label = Label(basket_frame, text="${:.2f}".format(item_prices[3]), bg="#ffffff")
    item_5_price_label = Label(basket_frame, text="${:.2f}".format(item_prices[4]), bg="#ffffff")
    item_6_price_label = Label(basket_frame, text="${:.2f}".format(item_prices[5]), bg="#ffffff")
    item_7_price_label = Label(basket_frame, text="${:.2f}".format(item_prices[6]), bg="#ffffff")
    item_8_price_label = Label(basket_frame, text="${:.2f}".format(item_prices[7]), bg="#ffffff")

    # Item total price labels are created
    item_1_total_price_label = Label(basket_frame, text="${:.2f}".format(item_total_prices[0]), bg="#ffffff")
    item_2_total_price_label = Label(basket_frame, text="${:.2f}".format(item_total_prices[1]), bg="#ffffff")
    item_3_total_price_label = Label(basket_frame, text="${:.2f}".format(item_total_prices[2]), bg="#ffffff")
    item_4_total_price_label = Label(basket_frame, text="${:.2f}".format(item_total_prices[3]), bg="#ffffff")
    item_5_total_price_label = Label(basket_frame, text="${:.2f}".format(item_total_prices[4]), bg="#ffffff")
    item_6_total_price_label = Label(basket_frame, text="${:.2f}".format(item_total_prices[5]), bg="#ffffff")
    item_7_total_price_label = Label(basket_frame, text="${:.2f}".format(item_total_prices[6]), bg="#ffffff")
    item_8_total_price_label = Label(basket_frame, text="${:.2f}".format(item_total_prices[7]), bg="#ffffff")
 
# Lists are created which hold all of the labels created above
    item_labels = [item_1_label, item_2_label, item_3_label, item_4_label, item_5_label, item_6_label, item_7_label, item_8_label]
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
    
    # Heading labels are created
    items_label = Label(basket_frame, text="Items", bg="#ffffff", font=10)
    quantity_label = Label(basket_frame, text="Quantity", bg="#ffffff", font=10)
    price_label = Label(basket_frame, text="Price each", bg="#ffffff", font=10)
    total_prices_label = Label(basket_frame, text="Total Prices", bg="#ffffff", font=10)

    # Total heading and total price labels are created
    total_label = Label(basket_frame, text="Total:", bg="#ffffff", font=10)
    total_price_label = Label(basket_frame, text="${:.2f}".format(total_price), bg="#ffffff", font=10)

    # Add items, order and update buttons are created
    add_items_button = Button(basket_frame, text="Menu", fg="#ffffff", bg="#55c2da", font=("Helvetica", 10, "bold"), width=5,command=menu_button_function)
    order_button = Button(basket_frame, text="Order", fg="#ffffff", bg="#55c2da", font=("Helvetica", 10, "bold"), width=5, command=order_button_function)
    update_button = Button(basket_frame, text="Update", fg="#ffffff", bg="#55c2da", font=("Helvetica", 10, "bold"), width=5, command=update_button_function)

    # Spinbox default varibles are created
    item_1_quantity = StringVar()
    item_2_quantity = StringVar()
    item_3_quantity = StringVar()
    item_4_quantity = StringVar()
    item_5_quantity = StringVar()
    item_6_quantity = StringVar()
    item_7_quantity = StringVar()
    item_8_quantity = StringVar()

    # Spinbox default variables are set in a list to use for update button function
    item_values = [
        item_1_quantity, 
        item_2_quantity, 
        item_3_quantity, 
        item_4_quantity, 
        item_5_quantity, 
        item_6_quantity, 
        item_7_quantity, 
        item_8_quantity
        ]

    # Item quantity spinboxes are created
    item_1_quantity_spinbox = Spinbox(basket_frame, bg="#ffffff", from_=0, to=10, width=5, textvariable=item_1_quantity)
    item_2_quantity_spinbox = Spinbox(basket_frame, bg="#ffffff", from_=0, to=10, width=5, textvariable=item_2_quantity)
    item_3_quantity_spinbox = Spinbox(basket_frame, bg="#ffffff", from_=0, to=10, width=5, textvariable=item_3_quantity)
    item_4_quantity_spinbox = Spinbox(basket_frame, bg="#ffffff", from_=0, to=10, width=5, textvariable=item_4_quantity)
    item_5_quantity_spinbox = Spinbox(basket_frame, bg="#ffffff", from_=0, to=10, width=5, textvariable=item_5_quantity)
    item_6_quantity_spinbox = Spinbox(basket_frame, bg="#ffffff", from_=0, to=10, width=5, textvariable=item_6_quantity)
    item_7_quantity_spinbox = Spinbox(basket_frame, bg="#ffffff", from_=0, to=10, width=5, textvariable=item_7_quantity)
    item_8_quantity_spinbox = Spinbox(basket_frame, bg="#ffffff", from_=0, to=10, width=5, textvariable=item_8_quantity)

    # Spinbox default values are set
    item_1_quantity.set(item_quantities[0])
    item_2_quantity.set(item_quantities[1])
    item_3_quantity.set(item_quantities[2])
    item_4_quantity.set(item_quantities[3])
    item_5_quantity.set(item_quantities[4])
    item_6_quantity.set(item_quantities[5])
    item_7_quantity.set(item_quantities[6])
    item_8_quantity.set(item_quantities[7])
    
    # The spinboxes are set in a list to use
    item_quantity_spinboxes = [
        item_1_quantity_spinbox, 
        item_2_quantity_spinbox, 
        item_3_quantity_spinbox, 
        item_4_quantity_spinbox, 
        item_5_quantity_spinbox, 
        item_6_quantity_spinbox, 
        item_7_quantity_spinbox, 
        item_8_quantity_spinbox
        ]

    # This is where the labels and buttons which always show are called
    items_label.grid(row=0, column=0, padx=5, pady=5)
    add_items_button.grid(row=9, column=0, padx=5, pady=5)
    quantity_label.grid(row=0, column=1, padx=5, pady=5)
    order_button.grid(row=10, column=0, padx=5, pady=5)
    price_label.grid(row=0, column=2, padx=5, pady=5)
    total_label.grid(row=9, column=2, padx=5, pady=5)
    total_prices_label.grid(row=0, column=3, padx=5, pady=5)
    total_price_label.grid(row=9, column=3, padx=5, pady=5)
    update_button.grid(row=9, column=1, padx=5, pady=5)

# This is where the program only displays the item if the item was ordered
    i = 0
    r = 1
    for item in items:
        if item_quantities[i] > 0:
            item_labels[i].grid(row=r, column=0, padx=5, pady=5, sticky=W)
            item_quantity_spinboxes[i].grid(row=r, column=1, padx=5, pady=5)
            item_price_labels[i].grid(row=r, column=2, padx=5, pady=5)
            item_total_price_labels[i].grid(row=r, column=3, padx=5, pady=5)
            i += 1
            r += 1
        else:
            i += 1

# This is where program is called to make sure it can only be run through the terminal and not through another program for a safety measure.
if __name__ == "__main__":
    main_function()

# This is where the GUI is ended
root.mainloop()