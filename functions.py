# This script creates a custom dialog for integer input using tkinter.
import tkinter as tk
from tkinter import simpledialog
from tkinter import Tk, simpledialog, Label, Entry

class CustomIntegerDialog(simpledialog.Dialog):
    def __init__(self, parent, title, prompt, minvalue=None, maxvalue=None, initialvalue=None):
        self.prompt = prompt
        self.minvalue = minvalue
        self.maxvalue = maxvalue
        self.initialvalue = initialvalue
        self.result = None
        super().__init__(parent, title)

    def body(self, master):
        self.geometry("400x200")  # Custom window size!

        Label(master, text=self.prompt).pack(pady=10)

        self.entry = Entry(master)
        self.entry.pack(pady=5)

        if self.initialvalue is not None:
            self.entry.insert(0, str(self.initialvalue))

        return self.entry  # focus

    def apply(self):
        try:
            value = int(self.entry.get())
            if (self.minvalue is not None and value < self.minvalue) or \
               (self.maxvalue is not None and value > self.maxvalue):
                self.result = None
            else:
                self.result = value
        except ValueError:
            self.result = None

# Usage
root = Tk()
root.withdraw()

dialog = CustomIntegerDialog(root, "Input", "Please enter a number:", minvalue=1, maxvalue=100, initialvalue=10)
my_number = dialog.result

print("You entered:", my_number)



if my_number is None:
    print("No number entered.")
else:
    print("You entered:", my_number)


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
output_window.geometry("300x200")  # Set the size of the output window (width x height)

output_label = tk.Label(output_window, text=f"Result of ex_2: {result_2}\nResult of ex_3: {result_3}")
output_label.pack(pady=20)  # Add some padding for better layout

output_window.mainloop()