from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self):

        # Formatting variables
        background_color = "bisque"

        # Start Main Screen GUI
        self.start_frame = Frame(width=300, height=300, bg=background_color, pady=10)
        self.start_frame.grid()

        # Temperature Conversion Heading {row 0)
        self.temp_start_label = Label(self.start_frame, text="Mystery Boxes Game",
                                      font=("Arial", "16", "bold"),
                                      bg=background_color,
                                      padx=10, pady=10)
        self.temp_start_label.grid(row=0)

        # Play input

        self.money_entry = Entry(self.start_frame, width=40)

        self.money_entry.grid(row=1, pady=10)

        # Play button (row 1)
        self.play_button = Button(self.start_frame, text="Low stakes",
                                  font=("Arial", "14"),
                                  padx=10, pady=10, command=lambda:Play(self))
        self.play_button.grid(row=2)


class Play:
    def __init__(self, partner):

        self.balance = int(partner.money_entry.get())

        print(1, self.balance)

        background = "orange"

        # disable play button
        partner.play_button.config(state=DISABLED)

        # Sets up child window (ie) play box
        self.play_box = Toplevel()

        # Set up GUI Frame
        self.play_frame = Frame(self.play_box, width=300, bg=background)
        self.play_frame.grid()
        # Set up Play heading (row 0)
        self.play_label = Label(self.play_frame, text="Play",
                                font=("Arial", "14", "bold"),
                                bg=background,
                                padx=10, pady=10)
        self.play_label.grid(row=0)

        # Play text (label, row 1)
        self.play_text = Label(self.play_frame, text="balance: {}".format(self.balance),
                               justify=LEFT, width=40,
                               bg=background, wrap=250,)
        self.play_text.grid(row=1)

        # Add button (row 2)
        self.add_btn = Button(self.play_frame, text="Add balance",
                              width=10, bg="orange", font="arial 10 bold",
                              command=partial(self.add))
        self.add_btn.grid(row=2, pady=10)

    def add(self):
        self.balance += 2
        output = "balance: {}".format(self.balance)
        print(output)
        self.play_text.configure(text=output)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Start")
    something = Start()
    root.mainloop()
