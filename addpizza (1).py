from tkinter import *

class Pizza:
    def __init__(self, name, price):
        self._name = name
        self._price = price
        pizzas.append(self)
        pizza_names.append(self._name)

def update_label():
    pizza_info.set("")
    for p in pizzas:
        pizza_info.set(pizza_info.get() + p._name + "   $" + str(p._price) + "\n")

def add():
    global pizza_menu
    Pizza(new_pizza.get(), new_price.get())
    update_label()
    pizza_menu.grid_forget()
    pizza_menu = OptionMenu(root, selected_pizza, *pizza_names)
    pizza_menu.grid(row=1)

pizzas = []
pizza_names = []

Pizza("Pepperoni", 10)
Pizza("Vegetarian", 5)

root = Tk()
root.title("Add pizza")
root.geometry('400x400')

pizza_info = StringVar()

pizza_lbl = Label(root, textvariable=pizza_info)
pizza_lbl.grid(row=0)

selected_pizza = StringVar()
selected_pizza.set(pizza_names[0])
pizza_menu = OptionMenu(root, selected_pizza, *pizza_names)
pizza_menu.grid(row=1)

new_pizza = StringVar()
new_price = StringVar()
new_pizza.set("Enter pizza name")
new_price.set("Price")

pizza_entry = Entry(root, textvariable=new_pizza).grid(row=2)
price_entry = Entry(root, textvariable=new_price).grid(row=2, column=1)

selected_pizza_edit = StringVar()
selected_pizza_edit.set(pizza_names[0])
pizza_menu = OptionMenu(root, selected_pizza_edit, *pizza_names)
pizza_menu.grid(row=3)

price_entry = Entry(root, textvariable=new_price).grid(row=3, column=1)

add_btn = Button(root, text="Add new pizza", command=add).grid(row=1, column=1)

update_label()
root.mainloop()
