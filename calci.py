import tkinter as tk
from tkinter import messagebox

# Function Definitions
def get_inputs():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        return num1, num2
    except:
        raise ValueError("Invalid input")

def add():
    try:
        num1, num2 = get_inputs()
        result.set(f"{num1} + {num2} = {num1 + num2}")
    except:
        show_error()

def sub():
    try:
        num1, num2 = get_inputs()
        result.set(f"{num1} - {num2} = {num1 - num2}")
    except:
        show_error()

def multiply():
    try:
        num1, num2 = get_inputs()
        result.set(f"{num1} × {num2} = {num1 * num2}")
    except:
        show_error()

def divide():
    try:
        num1, num2 = get_inputs()
        if num2 == 0:
            messagebox.showerror("Math Error", "Cannot divide by zero.")
            return
        result.set(f"{num1} ÷ {num2} = {num1 / num2:.2f}")
    except:
        show_error()

def average():
    try:
        num1, num2 = get_inputs()
        result.set(f"Avg({num1}, {num2}) = {(num1 + num2)/2:.2f}")
    except:
        show_error()

def show_error():
    messagebox.showerror("Input Error", "Please enter valid numbers.")

# GUI Window
root = tk.Tk()
root.title("Beautiful Calculator")
root.geometry("400x400")
root.config(bg="#f7f7ff")
root.resizable(False, False)

# Style
label_font = ("Helvetica", 12)
button_font = ("Helvetica", 11, "bold")
entry_bg = "#e8f0fe"
button_bg = "#4CAF50"
button_fg = "white"
result_font = ("Helvetica", 13, "bold")

# Heading
tk.Label(root, text="Simple Calculator", font=("Helvetica", 16, "bold"), bg="#f7f7ff", fg="#333").pack(pady=10)


tk.Label(root, text="Enter First Number", font=label_font, bg="#f7f7ff").pack()
entry1 = tk.Entry(root, width=25, font=label_font, bg=entry_bg, relief=tk.FLAT)
entry1.pack(pady=5)

tk.Label(root, text="Enter Second Number", font=label_font, bg="#f7f7ff").pack()
entry2 = tk.Entry(root, width=25, font=label_font, bg=entry_bg, relief=tk.FLAT)
entry2.pack(pady=5)

# Buttons 
button_frame = tk.Frame(root, bg="#f7f7ff")
button_frame.pack(pady=20)

def create_button(text, command, row, col, colspan=1):
    tk.Button(button_frame, text=text, width=12, height=2, font=button_font,
              bg=button_bg, fg=button_fg, activebackground="#45a049",
              command=command, relief=tk.FLAT, bd=0).grid(row=row, column=col, columnspan=colspan, padx=10, pady=10)

# operations
create_button("Add", add, 0, 0)
create_button("Subtract", sub, 0, 1)
create_button("Multiply", multiply, 1, 0)
create_button("Divide", divide, 1, 1)
create_button("Average", average, 2, 0, colspan=2)

# display result
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=result_font,
                        bg="#fff9c4", fg="#333", wraplength=350,
                        bd=2, relief=tk.GROOVE, padx=10, pady=10)
result_label.pack(pady=10)

# 
root.mainloop()
