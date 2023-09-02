import tkinter as tk

# Initialize the shopping cart as a set
shopping_cart = set()

# Function to add items to the shopping cart
def add_item():
    item = entry.get("1.0", tk.END).strip()  # Retrieve text from the Text widget
    if item and item not in shopping_cart:
        shopping_cart.add(item)
        cart_listbox.insert(tk.END, item)
        entry.delete("1.0", tk.END)

# Function to remove items from the shopping cart
def remove_item():
    selected_item_index = cart_listbox.curselection()
    if selected_item_index:
        selected_item = cart_listbox.get(selected_item_index)
        shopping_cart.remove(selected_item)
        cart_listbox.delete(selected_item_index)

# Create the main window
root = tk.Tk()
root.title("Shopping Cart")

# Entry for adding items
entry = tk.Text(root, width=70, height=3)
entry.pack()

# Buttons for adding and removing items
add_button = tk.Button(root, width=40, text="Add Item", command=add_item,)
remove_button = tk.Button(root, width=40, text="Remove Item", command=remove_item)
add_button.pack()
remove_button.pack()

# Listbox to display the shopping cart
cart_listbox = tk.Listbox(root, width=60, selectmode=tk.SINGLE)
cart_listbox.pack()

# Run the GUI main loop
root.mainloop()
