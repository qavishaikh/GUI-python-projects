import tkinter as tk
from tkinter import messagebox

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    
    if len(phone) != 11:
        messagebox.showerror("Invalid Input", "Phone number must be exactly 11 digits.")
    else:
        contacts[name] = phone
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"{name} has been added to your contacts.")

# Function to update a contact
def update_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    
    if name in contacts:
        if len(phone) != 11:
            messagebox.showerror("Invalid Input", "Phone number must be exactly 11 digits.")
        else:
            contacts[name] = phone
            name_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"{name}'s phone number has been updated.")
    else:
        messagebox.showerror("Not Found", f"{name} is not in your contacts.")

# Function to delete a contact
def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"{name} has been deleted from your contacts.")
    else:
        messagebox.showerror("Not Found", f"{name} is not in your contacts.")

# Function to search for a contact
def search_contact():
    name = name_entry.get()
    if name in contacts:
        phone = contacts[name]
        phone_label.config(text=f"{name}'s phone number is {phone}")
    else:
        phone_label.config(text=f"{name} is not in your contacts.")

# Create the main window
root = tk.Tk()
root.title("Contact Manager")

# Initialize contacts dictionary
contacts = {}

# Create and pack labels, entry fields, and buttons
name_label = tk.Label(root, text="Name:")
name_label.pack()

name_entry = tk.Entry(root, width=40)  # Increase width
name_entry.pack()

phone_label = tk.Label(root, text="")
phone_label.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()

phone_entry = tk.Entry(root, width=40)  # Increase width
phone_entry.pack()

add_button = tk.Button(root, text="Add Contact", command=add_contact, width=20, height=2)  # Increase width and height
add_button.pack()

update_button = tk.Button(root, text="Update Contact", command=update_contact, width=20, height=2)  # Increase width and height
update_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, width=20, height=2)  # Increase width and height
delete_button.pack()

search_button = tk.Button(root, text="Search Contact", command=search_contact, width=20, height=2)  # Increase width and height
search_button.pack()

exit_button = tk.Button(root, text="Exit", command=root.destroy, width=20, height=2)  # Increase width and height
exit_button.pack()

root.mainloop()
