import tkinter as tk
from tkinter import messagebox
class CosmeticProduct:
    def __init__(self, name, brand, quantity, price):
        self.name = name
        self.brand = brand
        self.quantity = quantity
        self.price = price

    def display_details(self):
        return f"{self.name} - {self.brand} - {self.quantity} in stock - ${self.price}"

class CosmeticsInventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return True
        return False

    def display_products(self):
        return [product.display_details() for product in self.products]
##########################################################################################################
def handle_login(username, password, selected_brand):

    if username == "layan" and password == "123":
        open_cosmetics_page(selected_brand)
    else:
        messagebox.showerror("Login Error", "Invalid username or password.")
##############################################################################################################
def open_cosmetics_page(brand):
    cosmetics_page = tk.Toplevel(root)
    cosmetics_page.title(f"{brand} Cosmetics Inventory")
    brand_inventory = CosmeticsInventory()

    brand_inventory.add_product(CosmeticProduct("Product1", brand, 10, 25.99))
    brand_inventory.add_product(CosmeticProduct("Product2", brand, 15, 19.99))
    brand_inventory.add_product(CosmeticProduct("Product3", brand, 20, 29.99))

root = tk.Tk()
root.title("Cosmetics Management System")


welcome_label = tk.Label(root, text="Welcome to the Cosmetics Management System!")
welcome_label.pack(pady=20)

brand_selection_button = tk.Button(root, text="Select a Brand", command=lambda: open_brand_selection_page())
brand_selection_button.pack(pady=10)

##################################################################################################################
def open_brand_selection_page():
    brand_selection_page = tk.Toplevel(root)
    brand_selection_page.title("Brand Selection")

    brand_label = tk.Label(brand_selection_page, text="Select a Cosmetic Brand:")
    brand_label.pack(pady=10)

    brands = ["Chanel", "Maybelline", "MAC"]

    brand_var = tk.StringVar()
    brand_var.set(brands[0])

    brand_dropdown = tk.OptionMenu(brand_selection_page, brand_var, *brands)
    brand_dropdown.pack(pady=10)

    login_button = tk.Button(brand_selection_page, text="Login",
                    command=lambda: open_login_page(brand_var.get()))
    login_button.pack(pady=10)


##################################################################################################################
def open_login_page(selected_brand):
    login_page = tk.Toplevel(root)
    login_page.title("Login")

    username_label = tk.Label(login_page, text="Username:")
    username_label.pack(pady=10)

    username_entry = tk.Entry(login_page)
    username_entry.pack(pady=10)

    password_label = tk.Label(login_page, text="Password:")
    password_label.pack(pady=10)

    password_entry = tk.Entry(login_page, show="*")
    password_entry.pack(pady=10)

    login_button = tk.Button(login_page, text="Login",
                             command=lambda: handle_login(username_entry.get(), password_entry.get(), selected_brand))
    login_button.pack(pady=10)

################################################################################################################




def close_program():
    root.destroy()

ending_label = tk.Label(root, text="Thank you for using the Cosmetics Management System!")
ending_label.pack(pady=20)

exit_button = tk.Button(root, text="Exit", command=close_program)
exit_button.pack(pady=10)

root.mainloop()
