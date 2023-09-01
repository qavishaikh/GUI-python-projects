# Expence Tracker App GUI 
import tkinter as tk

expenses = []

def add_expense():
    category = category_entry.get()
    date = date_entry.get()
    amount = float(amount_entry.get())
    expense = (category, date, amount)
    expenses.append(expense)
    result_label.config(text="Expense added successfully!")

def view_expenses():
    expenses_text.config(state=tk.NORMAL)
    expenses_text.delete(1.0, tk.END)
    
    if not expenses:
        expenses_text.insert(tk.END, "No expenses to display.")
    else:
        for idx, (category, date, amount) in enumerate(expenses, start=1):
            expenses_text.insert(tk.END, f"{idx}. Category: {category}, Date: {date}, Amount: ₨{amount:.2f}\n")
        expenses_text.config(state=tk.DISABLED)

def total_expenses_by_category():
    category_totals = {}
    for category, _, amount in expenses:
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    
    result_text.insert(tk.END, "Total Expenses by Category:\n")
    for category, total in category_totals.items():
        result_text.insert(tk.END, f"{category}: ₨{total:.2f}\n")
    result_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Expense Tracker")

category_label = tk.Label(root, text="Category:")
category_label.pack()
category_entry = tk.Entry(root)
category_entry.pack()

date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
date_label.pack()
date_entry = tk.Entry(root)
date_entry.pack()

amount_label = tk.Label(root, text="Amount (PKR):")
amount_label.pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.pack()

view_button = tk.Button(root, text="View Expenses", command=view_expenses)
view_button.pack()

total_button = tk.Button(root, text="Total Expenses by Category", command=total_expenses_by_category)
total_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

expenses_text = tk.Text(root, height=10, width=50)
expenses_text.pack()
expenses_text.config(state=tk.DISABLED)

result_text = tk.Text(root, height=10, width=50)
result_text.pack()
result_text.config(state=tk.DISABLED)

root.mainloop()
