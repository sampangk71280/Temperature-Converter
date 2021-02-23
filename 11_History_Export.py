from tkinter import *
from functools import partial # to prevent unwanted windows

import random


class Converter:
    def __init__(self, parent):

        # Formatting variables...
        background_color = "light blue"

        # Initialise list to hold calculation history
        self.all_calculation = []

        # Initialise list to hold calculation history
        self.all_calculations = ['10 degrees C is -12.2 degrees F',
                                 '20 degrees C is -6.7 degrees F',
                                 '30 degrees C is -1.1 degrees F',
                                 '40 degrees C is 4.4 degrees F',
                                 '50 degrees C is 10 degrees F']

        self.converter_frame = Frame(width=600, height=600, bg=background_color, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label (self.converter_frame, text="Temperature Converter",
                                           font=("Arial", "16", "bold"),
                                           bg=background_color,
                                           padx=10, pady=10)
        self.temp_converter_label.grid(row=0)\

        # History Button (row 1)
        self.history_button = Button(self.converter_frame, text="History",
                                  font=("Arial", "14"),
                                  padx=10, pady=10, command=lambda: self.history(self.all_calculations))
        self.history_button.grid(row=1)

        #if len(self.all_calculation) == 0:
            #self.history_button.config(state=DISABLED)


    def history(self, calc_history):
        History(self, calc_history)

class History:
    def __init__(self, partner, calc_history):

        background = "#E0FFC9" # pale green

        calc_history = []

        # disable history button
        partner.history_button.config(state=DISABLED)

            # Sets up child window (ie: history box)
        self.history_box = Toplevel()

        # If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()

        # Set up History heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # History text (label, row 1)
        self.history_text = Label(self.history_frame,
                                  text="Here are your most recent "
                                  "calculations. Please use the "
                                  "export button to create a text "
                                  "file of all your calculations for "
                                  "this session", wrap=250,
                                font="Arial 10 italic",
                                justify=LEFT, width=40, bg=background,
                                padx=10, pady=10)
        self.history_text.grid(column=0, row=1)

        # History output goes here... (row 2)

        # Generaet string from list of calculations...
        history_string = ""

        if len(calc_history) >= 7:
            for item in range(0,7):
                history_string += calc_history[len(calc_history) - item - 1] + "\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                                                calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here is your calculation "
                                              "history. You can use the "
                                              "export button to save this "
                                              "data to a text file if "
                                              "desired.")

        # Label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background, font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # Export / Dismiss Button Frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold",
                                    command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

        # Dismss button
        self.export_button = Button(self.export_dismiss_frame, text="Dismiss",
                                    font="Arial 12 bold", command=partial(self.close_history, partner))
        self.export_button.grid(row=0, column=1)

    def close_history(self, partner):
        # Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, calc_history):
        Export(self, calc_history)

class Export:
    def __init__(self, partner, calc_history):

        print(calc_history)
        background = "#FFD47E"  # pale orange

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()

        # If users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, bg=background)
        self.export_frame.grid()

        # Set up Export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Export text (label, row 1)
        self.export_text = Label(self.export_frame, text="",
                                 justify=LEFT, width=40, bg=background, wrap=250)
        self.export_text.grid(column=0, row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.export_frame, text="Dismiss", width=10, bg="orange",
                                  font="arial 10 bold",
                                  command=partial(self.close_export, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Converter(root)
    root.mainloop()
