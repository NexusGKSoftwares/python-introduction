#  lets create a simple calculator using tinkter in python
# code 
import tkinter as tk
from tkinter import messagebox
# create a window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x400")
# create a label
label = tk.Label(window, text="Enter two numbers")
label.pack()
# create an entry
entry = tk.Entry(window)
entry.pack()
# create another label
label2 = tk.Label(window, text="Enter the operation")
label2.pack()
# create another entry
entry2 = tk.Entry(window)
entry2.pack()
# create a function to calculate the
# result
def calculate():
    try:
        num1 = int(entry.get())
        num2 = int(entry2.get())
        operation = entry3.get()
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            result = "Invalid operation"
        messagebox.showinfo("Result", result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
# create a button
button = tk.Button(window, text="Calculate", command=calculate)
button.pack()
# create another label
label3 = tk.Label(window, text="Enter the operation")
label3.pack()
# create another entry
entry3 = tk.Entry(window)
entry3.pack()
# run the main loop
window.mainloop()
# output

