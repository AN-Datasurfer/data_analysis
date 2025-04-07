from tkinter import *
import tkinter as tk
from tkinter import simpledialog


root = tk.Tk()
root.withdraw()  # Hide the root window

# Prompt the user for input using a dialog box
my_number = int(simpledialog.askstring("Input", "Please enter a number:"))


# Define the functions to be called
def ex_2(number_1):
    number_x2 = number_1 *2
    return number_x2

def ex_3(number_2):
    number_x3 = number_2 *3
    return number_x3

result_2 = ex_2(my_number)
result_3 = ex_3(my_number)

output_window = tk.Toplevel()
output_window.title("Results")

output_label = tk.Label(output_window, text=f"Result of ex_2: {result_2}\nResult of ex_3: {result_3}")
output_label.pack()

output_window.mainloop()