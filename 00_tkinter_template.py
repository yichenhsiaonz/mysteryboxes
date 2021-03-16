from tkinter import *
import random


class Game:
    def __init__(self):

        self.background = "bisque"

        # Game frame setup
        self.game_frame = Frame(bg=self.background, pady=10)
        self.game_frame.grid()

        # Game Label

        self.game_label = Label(self.game_frame, text="Mystery Boxes Game", bg=self.background,
                                font=("Arial", 16, "bold"))

        self.game_label.grid(row=0)

        # Game text

        self.game_text = Label(self.game_frame, text="Haha yes", width=40, bg=self.background)

        self.game_text.grid(row=1)

        # Game input

        self.game_entry = Entry(self.game_frame, width=40)

        self.game_entry.grid(row=2, pady=10)

        # Stakes buttons

        self.stake_button_frame = Frame(self.game_frame, bg=self.background)
        self.stake_button_frame.grid(row=3)

        # Low stakes button

        self.low_button = Button(self.stake_button_frame, width=10, height=2, text="Low ($5)",
                                 command=self.launch_gambling_room)
        self.low_button.grid(row=0, column=0, pady=10, padx=5)

        # Mid stakes button

        self.mid_button = Button(self.stake_button_frame, width=10, height=2, text="Mid ($10)",
                                 command=self.launch_gambling_room)
        self.mid_button.grid(row=0, column=1, pady=10, padx=5)

        # High stakes button

        self.high_button = Button(self.stake_button_frame, width=10, height=2, text="High ($15)",
                                 command=self.launch_gambling_room)
        self.high_button.grid(row=0, column=2, pady=10, padx=5)

    def launch_gambling_room(self):
        print("button pushed")
        gambling_window = GamblingBox(self)
        gambling_window.gambling_text.configure(text="wow!")


class GamblingBox:
    def __init__(self, partner):

        self.balance = partner.game_entry.get()

        self.gambling_frame = Frame(bg=partner.background)
        self.gambling_frame.grid()

        self.gambling_label = Label(self.gambling_frame, text=self.balance, bg=partner.background,
                               font=("Arial", 16, "bold"))
        self.gambling_label.grid(row=0)

        # Game text

        self.gambling_text = Label(self.gambling_frame, width=40, bg=partner.background)
        self.gambling_text.grid(row=1)



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Boxes")
    something = Game()
    root.mainloop()
