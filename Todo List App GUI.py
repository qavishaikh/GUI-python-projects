import tkinter as tk
from tkinter import messagebox

def display_tasks():
    task_display.delete(1.0, tk.END)  # Clear the current task display
    for index, task in enumerate(tasks):
        task_display.insert(tk.END, f"{index + 1}. {task}\n")

def add_task():
    new_task = new_task_entry.get()
    if new_task:
        tasks.append(new_task)
        new_task_entry.delete(0, tk.END)  # Clear the input field
        display_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def mark_completed():
    task_index = int(completed_task_entry.get()) - 1
    if 0 <= task_index < len(tasks):
        completed_task = tasks.pop(task_index)
        messagebox.showinfo("Task Completed", f"Task '{completed_task}' marked as completed!")
        display_tasks()
    else:
        messagebox.showwarning("Invalid Index", "Invalid index.")

def quit_app():
    window.destroy()

tasks = []

window = tk.Tk()
window.title("To-Do List")

# Create and configure GUI elements
task_display = tk.Text(window, height=10, width=40)
new_task_entry = tk.Entry(window, width=30)
completed_task_entry = tk.Entry(window, width=30)
add_button = tk.Button(window, text="Add Task", command=add_task)
mark_button = tk.Button(window, text="Mark Completed", command=mark_completed)
quit_button = tk.Button(window, text="Quit", command=quit_app)

# Place GUI elements in the window
task_display.grid(row=0, column=0, columnspan=2)
new_task_entry.grid(row=1, column=0)
add_button.grid(row=1, column=1)
completed_task_entry.grid(row=2, column=0)
mark_button.grid(row=2, column=1)
quit_button.grid(row=3, column=0, columnspan=2)

# Display tasks initially
display_tasks()

window.mainloop()
