from tkinter import *
from functools import partial # to prevent unwanted windows

import random


class Converter:
    def __init__(self):

        # Formatting variables...
        background_color = "#D4BDFF" # light purple

        # Converter Frame
        self.converter_frame = Frame(bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Converter Heading (row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text="Temperature Converter",
                                            font="Arial 19 bold",
                                            bg=background_color,
                                            padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # User instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be "
                                                    "converted and then push "
                                                    "one of the buttons below...",
                                             font="Arial 10 italic", wrap=290,
                                             justify=LEFT, bg=background_color,
                                             padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        # Conversion buttons frame (row 3)
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centigrade", font="Arial 10 bold",
                                  bg="#CFECFF", padx=10, pady=10,
                                  cosmmand=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  bg="#FFF1AA", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        # Answer label (row 4)
        self.converted_label = Label(self.converter_frame, font="Arial 14 bold",
                                     fg="purple", text="Calculation goes here", bg=background_color, pady=10)
        self.converted_label.grid(row=4)

        # History / Help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                       text="Calculation History", width=15)
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, low):
        print(low)

        error = "#FF6969" # Pale pink backgground for when entry box has errors

        # Retrieve amount entered into Entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_error = "no"

            # Check amount is a valid number

            # Convert to F
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert, fahrenheit)

            # Convert to C
            elif low == -459 and to_convert >= low:
                celcius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celcius = self.round_it(celcius)
                answer = "{} degrees C is {} degrees F".format(to_convert, celcius)

            else:
                # input is invalid (too cold)
                answer = "Too cold!"
                has_errors = "yes"

            # Display answer
                if has_errors == "no":
                    self.converted_label.configure(text=answer, fg="blue")
                    self.to_convert_entry.configure(bg="white")
                else:
                    self.converted_label.configure(text=answer, fg="red")
                    self.to_convert_entry.configure(bg=error)
            # Add answer to list for History

        except ValueError:
            self.converted_label.configure(text="Enter a number!", fg="red")
            self.to_convert_entry.configure(bg=error)

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return round


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Converter()
    root.mainloop()
