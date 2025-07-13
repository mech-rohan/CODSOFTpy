import tkinter as tk
from tkinter import messagebox


tasks = []


def add_task():
    task_text = task_entry.get().strip()
    if task_text and task_text != "Enter your task here...":
        tasks.append({"task": task_text, "done": False})
        task_entry.delete(0, tk.END)
        refresh_task_list()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")


def refresh_task_list():
    task_listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks):
        status = "✔️ Done" if task["done"] else "⏳ Pending"
        display_text = f"{idx + 1}. {task['task']} - {status}"
        task_listbox.insert(tk.END, display_text)

     
        if task["done"]:
            task_listbox.itemconfig(idx, {'fg': 'green'})
        else:
            task_listbox.itemconfig(idx, {'fg': 'red'})


def mark_task_done():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = True
        refresh_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")


def delete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        refresh_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def clear_all_tasks():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
        tasks.clear()
        refresh_task_list()


def on_entry_click(event):
    if task_entry.get() == "Enter your task here...":
        task_entry.delete(0, tk.END)
        task_entry.config(fg="black")


def on_focus_out(event):
    if not task_entry.get():
        task_entry.insert(0, "Enter your task here...")
        task_entry.config(fg="grey")

# Create the main window
root = tk.Tk()
root.title("Cool To-Do List")
root.geometry("450x500")
root.configure(bg="#ADD8E6")  # Light blue background

# Header Label
header = tk.Label(root, text="📝 My To-Do List", font=("Arial", 18, "bold"), bg="#ADD8E6", fg="#333")
header.pack(pady=10)


task_entry = tk.Entry(root, width=35, font=("Arial", 12), fg="grey")
task_entry.insert(0, "Enter your task here...")
task_entry.bind("<FocusIn>", on_entry_click)
task_entry.bind("<FocusOut>", on_focus_out)
task_entry.pack(pady=10)

# Button Frame
button_frame = tk.Frame(root, bg="#ADD8E6")
button_frame.pack(pady=5)

# Add Task Button
add_button = tk.Button(button_frame, text="Add Task", width=12, bg="#4CAF50", fg="white", command=add_task)
add_button.grid(row=0, column=0, padx=5)

# Mark as Done Button
done_button = tk.Button(button_frame, text="Mark as Done", width=12, bg="#2196F3", fg="white", command=mark_task_done)
done_button.grid(row=0, column=1, padx=5)

# Delete Task Button
delete_button = tk.Button(button_frame, text="Delete Task", width=12, bg="#f44336", fg="white", command=delete_task)
delete_button.grid(row=1, column=0, padx=5, pady=5)

# Clear All Tasks Button
clear_button = tk.Button(button_frame, text="Clear All", width=12, bg="#FF9800", fg="white", command=clear_all_tasks)
clear_button.grid(row=1, column=1, padx=5, pady=5)

# box to display tasks
task_listbox = tk.Listbox(root, width=50, height=12, font=("Arial", 11))
task_listbox.pack(pady=15)


root.mainloop()
