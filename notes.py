import tkinter as tk
from tkinter import messagebox

# Create the main window
def create_window():
    window = tk.Tk()
    window.title("To-Do List App")
    window.geometry("500x400")
    return window

# Function to add task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)  
        task_entry.delete(0, tk.END)  
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete task
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]  
        tasks_listbox.delete(selected_task_index)  
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to mark task as completed
def mark_as_completed():
    try:
        selected_task_index = tasks_listbox.curselection()[0]  
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(selected_task_index, f"✔️ {task}")  
    except:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Build the GUI
def build_gui(window):
    global task_entry, tasks_listbox

    # Task Entry (Input field)
    task_entry = tk.Entry(window, width=25, font=("Arial", 14))
    task_entry.pack(pady=10)

    # Add Task Button
    add_task_btn = tk.Button(window, text="Add Task", command=add_task, font=("Arial", 12))
    add_task_btn.pack(pady=5)

    # Listbox to display tasks
    tasks_listbox = tk.Listbox(window, width=40, height=10, font=("Arial", 12))
    tasks_listbox.pack(pady=10)

    # Mark as Completed Button
    complete_task_btn = tk.Button(window, text="Mark as Completed", command=mark_as_completed, font=("Arial", 12))
    complete_task_btn.pack(pady=5)

    # Delete Task Button
    delete_task_btn = tk.Button(window, text="Delete Task", command=delete_task, font=("Arial", 12))
    delete_task_btn.pack(pady=5)

# Main function to run the app
if __name__ == "__main__":
    window = create_window()  
    build_gui(window)  
    window.mainloop()  
