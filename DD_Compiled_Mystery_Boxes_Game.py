from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self):

        # Formatting variables
        self.balance = 0
        background_color = "bisque"
        self.stakes = ""

        # Start Main Screen GUI
        self.start_frame = Frame(width=300, height=300, bg=background_color, pady=10)
        self.start_frame.grid()

        # Start Heading {row 0)
        self.start_label = Label(self.start_frame, text="Mystery Boxes Game",
                                 font=("Arial", "16", "bold"),
                                 bg=background_color,
                                 padx=10, pady=10)
        self.start_label.grid(row=0)

        # Start input (row 1)

        self.input_frame = Frame(self.start_frame, bg=background_color)

        self.input_frame.grid(row=1)

        self.money_entry = Entry(self.input_frame, width=15, font=("Arial", "15"))
        self.money_entry.insert(0, "0")

        self.money_entry.grid(row=0, column=0)

        self.add_funds_button = Button(self.input_frame, text="Add funds",
                                       font=("Arial", "10"),
                                       padx=2, command=self.update_balance)
        self.add_funds_button.grid(row=0, column=1)

        # Balance label (row 2)

        self.balance_label = Label(self.start_frame, text="Balance: {}".format(self.balance),
                                   font=("Arial", "10"),
                                   bg=background_color,
                                   padx=10, pady=10)
        self.balance_label.grid(row=2, pady=2)

        # Play buttons (row 3)

        self.play_button_frame = Frame(self.start_frame, bg=background_color)
        self.play_button_frame.grid(row=3)

        self.play_button_low = Button(self.play_button_frame, text="Low (5)",
                                      font=("Arial", "10"), bg="green yellow",
                                      width=9, pady=5, command=lambda: self.open_play_box(1))
        self.play_button_low.grid(row=0, column=0, padx=5)

        self.play_button_mid = Button(self.play_button_frame, text="Medium (10)",
                                      font=("Arial", "10"), bg="yellow",
                                      width=9, pady=5, command=lambda: self.open_play_box(2))
        self.play_button_mid.grid(row=0, column=1, padx=5)

        self.play_button_high = Button(self.play_button_frame, text="High (15)",
                                       font=("Arial", "10"), bg="orange",
                                       width=9, pady=5, command=lambda: self.open_play_box(3))
        self.update_balance()
        self.play_button_high.grid(row=0, column=2, padx=5)

        # Export / Help buttons (row 4)

        self.export_help_frame = Frame(self.start_frame, bg=background_color, pady=10)
        self.export_help_frame.grid(row=4)

        self.export_button = Button(self.export_help_frame, text="Export",
                                    font=("Arial", "14"),
                                    padx=10, pady=3)
        self.export_button.grid(row=0, column=0, padx=5)

        self.help_button = Button(self.export_help_frame, text="Help",
                                  font=("Arial", "14"),
                                  padx=10, pady=3)
        self.help_button.grid(row=0, column=1, padx=5)

    def open_play_box(self, stakes):
        self.stakes = stakes
        Play(self)

    def update_balance(self):
        self.balance = int(self.money_entry.get())
        self.balance_label.config(text="Balance: {}".format(self.balance))
        self.play_button_low.config(state=DISABLED)
        self.play_button_mid.config(state=DISABLED)
        self.play_button_high.config(state=DISABLED)
        if self.balance >= 5:
            self.play_button_low.config(state=NORMAL)
            if self.balance >= 10:
                self.play_button_mid.config(state=NORMAL)
                if self.balance >= 15:
                    self.play_button_high.config(state=NORMAL)

class Play:
    def __init__(self, partner):

        self.temp_balance = partner.balance

        print(partner.stakes, self.temp_balance)

        background = "orange"

        # disable play button
        partner.play_button_low.config(state=DISABLED)
        partner.play_button_mid.config(state=DISABLED)
        partner.play_button_high.config(state=DISABLED)

        # Sets up child window (ie) play box
        self.play_box = Toplevel()

        self.play_box.protocol('WM_DELETE_WINDOW', partial(self.close_play, partner))

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
        self.play_text = Label(self.play_frame, text="balance: {}".format(self.temp_balance),
                               justify=LEFT, width=40,
                               bg=background, wrap=250,)
        self.play_text.grid(row=1)

        # Add button (row 2)
        self.add_btn = Button(self.play_frame, text="Add balance",
                              width=10, bg="orange", font="arial 10 bold",
                              command=partial(self.add, partner))
        self.add_btn.grid(row=2, pady=10)

    def add(self, partner):
        self.temp_balance += partner.stakes*2
        output = "balance: {}".format(self.temp_balance)
        print(output)
        self.play_text.configure(text=output)

    def close_play(self, partner):
        partner.update_balance()
        self.play_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery boxes")
    something = Start()
    root.mainloop()
