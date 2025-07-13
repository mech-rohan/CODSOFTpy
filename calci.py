import tkinter as tk
from tkinter import ttk, messagebox

# Functions
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result.set(f"➤ {num1} + {num2} = {num1 + num2}")
        elif operation == "Subtraction":
            result.set(f"➤ {num1} - {num2} = {num1 - num2}")
        elif operation == "Multiplication":
            result.set(f"➤ {num1} × {num2} = {num1 * num2}")
        elif operation == "Division":
            if num2 == 0:
                raise ZeroDivisionError
            result.set(f"➤ {num1} ÷ {num2} = {num1 / num2:.2f}")
        else:
            messagebox.showwarning("Operation Missing", "Please select an operation.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")

def clear_all():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    operation_box.set("Choose Operation")
    result.set("")

def on_entry_click(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg='black')

# GUI setup
root = tk.Tk()
root.title("🌟 Mini Calculator")
root.geometry("400x400")
root.configure(bg="#e6f2ff")
root.resizable(False, False)

# Styles
style = ttk.Style()
style.configure("TCombobox", font=("Segoe UI", 12))
style.configure("TButton", font=("Segoe UI", 12))

# Title
tk.Label(root, text="Mini Calculator", font=("Segoe UI", 20, "bold"), bg="#e6f2ff", fg="#004d99").pack(pady=20)

# Input fields
entry1 = tk.Entry(root, font=("Segoe UI", 14), width=22, fg='gray')
entry1.insert(0, "Enter first number")
entry1.bind("<FocusIn>", lambda e: on_entry_click(e, entry1, "Enter first number"))
entry1.pack(pady=10)

entry2 = tk.Entry(root, font=("Segoe UI", 14), width=22, fg='gray')
entry2.insert(0, "Enter second number")
entry2.bind("<FocusIn>", lambda e: on_entry_click(e, entry2, "Enter second number"))
entry2.pack(pady=10)

# Operation selection
operation_var = tk.StringVar()
operation_box = ttk.Combobox(root, textvariable=operation_var, state="readonly", width=20)
operation_box['values'] = ("Addition", "Subtraction", "Multiplication", "Division")
operation_box.set("Choose Operation")
operation_box.pack(pady=15)

# Result display
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Segoe UI", 14, "bold"), fg="#006600", bg="#e6f2ff")
result_label.pack(pady=15)

# Buttons
btn_frame = tk.Frame(root, bg="#e6f2ff")
btn_frame.pack(pady=10)

calc_btn = tk.Button(btn_frame, text="Calculate", font=("Segoe UI", 12), bg="#0080ff", fg="white", width=12, command=calculate)
calc_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(btn_frame, text="Clear", font=("Segoe UI", 12), bg="#ff4d4d", fg="white", width=12, command=clear_all)
clear_btn.grid(row=0, column=1, padx=10)

# Run app
root.mainloop()
