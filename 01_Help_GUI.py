from tkinter import *
from functools import partial # to prevent unwanted windows

import random


class Converter:
    def __init__(self, parent):

        # Formatting variables...
        background_color = "light blue"

        self.converter_frame = Frame(width=600, height=600, bg=background_color, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label (self.converter_frame, text="Temperature Converter",
                                           font=("Arial", "16", "bold"),
                                           bg=background_color,
                                           padx=10, pady=10)
        self.temp_converter_label.grid(row=0)\

        # Help Button (row 1)
        self.help_button = Button(self.converter_frame, text="Help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Converter(root)
    root.mainloop()
