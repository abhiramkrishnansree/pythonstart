import tkinter as tk
from tkinter import messagebox

def calculate_simple_interest():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get()) / 100
    time = float(time_entry.get())

    simple_interest = (principal * rate * time) / 100

    result_label.config(text=f"Simple Interest: {simple_interest:.2f}")

def calculate_compound_interest():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get()) / 100
    time = float(time_entry.get())
    periods = float(periods_entry.get())

    compound_interest = principal * ((1 + rate / periods) ** (periods * time)) - principal

    result_label.config(text=f"Compound Interest: {compound_interest:.2f}")

# Create main window
root = tk.Tk()
root.title("Interest Calculator")

# Create labels
principal_label = tk.Label(root, text="Principal:")
rate_label = tk.Label(root, text="Rate (%):")
time_label = tk.Label(root, text="Time (years):")
periods_label = tk.Label(root, text="Number of periods per year:")

# Create entry fields
principal_entry = tk.Entry(root)
rate_entry = tk.Entry(root)
time_entry = tk.Entry(root)
periods_entry = tk.Entry(root)

# Create buttons
simple_interest_button = tk.Button(root, text="Calculate Simple Interest", command=calculate_simple_interest)
compound_interest_button = tk.Button(root, text="Calculate Compound Interest", command=calculate_compound_interest)

# Create result label
result_label = tk.Label(root, text="Result will be displayed here")

# Grid layout
principal_label.grid(row=0, column=0)
rate_label.grid(row=1, column=0)
time_label.grid(row=2, column=0)
periods_label.grid(row=3, column=0)

principal_entry.grid(row=0, column=1)
rate_entry.grid(row=1, column=1)
time_entry.grid(row=2, column=1)
periods_entry.grid(row=3, column=1)

simple_interest_button.grid(row=4, column=0, columnspan=2, pady=10)
compound_interest_button.grid(row=5, column=0, columnspan=2)
result_label.grid(row=6, column=0, columnspan=2)

# Start the GUI
root.mainloop()
