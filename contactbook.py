import tkinter as tk
from tkinter import messagebox, simpledialog

contact = {}

#to display all contacts
def display_contact():
    display_area.delete('1.0', tk.END)
    if not contact:
        display_area.insert(tk.END, "Contact book is empty.\n")
    else:
        display_area.insert(tk.END, "Name\t\tContact Number\n")
        display_area.insert(tk.END, "-"*40 + "\n")
        for name, number in contact.items():
            display_area.insert(tk.END, f"{name}\t\t{number}\n")

# adding a contact
def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter contact name:")
    if not name:
        return
    number = simpledialog.askstring("Add Contact", "Enter mobile number:")
    if not number:
        return
    contact[name] = number
    messagebox.showinfo("Success", f"Contact {name} added.")
    display_contact()

# search for a contact
def search_contact():
    name = simpledialog.askstring("Search Contact", "Enter contact name:")
    if name in contact:
        messagebox.showinfo("Contact Found", f"{name}'s number is {contact[name]}")
    else:
        messagebox.showwarning("Not Found", "Contact not found.")

#  edit a contact
def edit_contact():
    name = simpledialog.askstring("Edit Contact", "Enter contact name to edit:")
    if name in contact:
        number = simpledialog.askstring("Edit Contact", "Enter new mobile number:")
        contact[name] = number
        messagebox.showinfo("Updated", f"{name}'s contact updated.")
        display_contact()
    else:
        messagebox.showwarning("Not Found", "Contact not found.")

# delete a contact
def delete_contact():
    name = simpledialog.askstring("Delete Contact", "Enter contact name to delete:")
    if name in contact:
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {name}?")
        if confirm:
            contact.pop(name)
            messagebox.showinfo("Deleted", f"{name} deleted.")
            display_contact()
    else:
        messagebox.showwarning("Not Found", "Contact not found.")


root = tk.Tk()
root.title("Contact Book")
root.geometry("450x450")
root.config(bg="#e0f7fa")

title = tk.Label(root, text="Contact Book", font=("Arial", 18, "bold"), bg="#e0f7fa", fg="#00796b")
title.pack(pady=10)

btn_frame = tk.Frame(root, bg="#e0f7fa")
btn_frame.pack(pady=10)


tk.Button(btn_frame, text="Add", width=12, command=add_contact, bg="#00796b", fg="white").grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Search", width=12, command=search_contact, bg="#00796b", fg="white").grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Display", width=12, command=display_contact, bg="#00796b", fg="white").grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Edit", width=12, command=edit_contact, bg="#00796b", fg="white").grid(row=1, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Delete", width=12, command=delete_contact, bg="#00796b", fg="white").grid(row=2, column=0, columnspan=2, pady=5)


display_area = tk.Text(root, height=12, width=50, borderwidth=2, relief="sunken", font=("Courier", 10))
display_area.pack(pady=10)


tk.Button(root, text="Exit", command=root.quit, bg="#d32f2f", fg="white", width=10).pack(pady=5)

root.mainloop()
