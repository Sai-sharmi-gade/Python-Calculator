import tkinter as tk
import math

# Create the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x550")  # Increased height for elegance
root.configure(bg="#1E1E1E")

# Entry widget for input/output (Glassmorphism effect)
entry_frame = tk.Frame(root, bg="#2C2C2C", bd=5, relief=tk.FLAT)
entry_frame.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10, pady=15, padx=10, sticky="nsew")

entry = tk.Entry(entry_frame, font=("Arial", 24), bd=0, relief=tk.FLAT, justify="right", bg="#1E1E1E", fg="white")
entry.pack(ipadx=10, ipady=15, fill="both", expand=True)

# Function to update the entry field
def on_button_click(char):
    entry.insert(tk.END, char)

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Function to delete last character (Backspace)
def backspace():
    entry.delete(len(entry.get()) - 1, tk.END)

# Function to evaluate the expression
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)  # Use eval() to compute result
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to calculate square
def square():
    try:
        num = float(entry.get())
        result = num ** 2
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.insert(tk.END, "Error")

# Function to calculate square root
def square_root():
    try:
        num = float(entry.get())
        result = math.sqrt(num)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.insert(tk.END, "Error")

# Button styling (Glass effect)
btn_bg = "#3B3B3B"
btn_hover = "#505050"
btn_fg = "white"
btn_font = ("Arial", 20)

# Button grid
buttons = [
    ('7', '8', '9', '⌫'),
    ('4', '5', '6', '/'),
    ('1', '2', '3', '*'),
    ('0', '.', '=', '-'),
    ('+', 'C', 'x²', '√x')
]

buttons_list = []  # Store buttons for effects

# Create buttons dynamically
for r, row in enumerate(buttons, start=1):
    for c, char in enumerate(row):
        action = (
            backspace if char == '⌫' else
            clear_entry if char == 'C' else
            calculate if char == '=' else
            square if char == 'x²' else
            square_root if char == '√x' else
            lambda ch=char: on_button_click(ch)
        )

        btn = tk.Button(root, text=char, font=btn_font, bg=btn_bg, fg=btn_fg, width=6, height=2, command=action, relief=tk.FLAT)
        btn.grid(row=r, column=c, padx=8, pady=8, sticky="nsew")

        # Button hover effect
        def on_enter(e, b=btn):
            b.config(bg=btn_hover)
        def on_leave(e, b=btn):
            b.config(bg=btn_bg)

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

        buttons_list.append(btn)

# Adjust column and row weights for responsiveness
for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(6):
    root.rowconfigure(i, weight=1)

# Run the Tkinter event loop
root.mainloop()
