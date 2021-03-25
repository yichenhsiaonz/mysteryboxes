from tkinter import *
from functools import partial  # To prevent unwanted windows
from random import *


def number_checker(input_number):
    try:
        if 0 <= int(input_number) <= 50:
            return int(input_number)
        elif int(input_number) > 50:
            return "Too High"
        else:
            return "Too Low"
    except ValueError:
        return "Not int"


def regex_check(file_name):
    if re.search("[.<>:\"/|?*\\\\\040]", file_name):
        return "Invalid file name - illegal character(s)\n. < > : \" / \\ | ? *)"
    if file_name == "":
        return "Invalid file name - can't be blank"
    return "No Error"


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

        # Error Label (row 1)
        self.error_label = Label(self.start_frame, text="", bg=background_color)
        self.error_label.grid(row=1, column=0)

        # Start input (row 2)

        self.input_frame = Frame(self.start_frame, bg=background_color)

        self.input_frame.grid(row=2)

        self.money_entry = Entry(self.input_frame, width=15, font=("Arial", "15"))
        self.money_entry.insert(0, "0")

        self.money_entry.grid(row=0, column=0)

        self.add_funds_button = Button(self.input_frame, text="Add funds",
                                       font=("Arial", "10"),
                                       padx=2, command=self.update_balance)
        self.add_funds_button.grid(row=0, column=1)

        # Balance label (row 3)

        self.balance_label = Label(self.start_frame, text="Balance: {}".format(self.balance),
                                   font=("Arial", "10"),
                                   bg=background_color,
                                   padx=10, pady=10)
        self.balance_label.grid(row=3, pady=2)

        # Play buttons (row 4)

        self.play_button_frame = Frame(self.start_frame, bg=background_color)
        self.play_button_frame.grid(row=4)

        self.play_button_low = Button(self.play_button_frame, text="Low ($5)",
                                      font=("Arial", "10"), bg="green yellow",
                                      width=10, pady=5, command=lambda: self.open_play_box(1))
        self.play_button_low.grid(row=0, column=0, padx=5)

        self.play_button_mid = Button(self.play_button_frame, text="Medium ($10)",
                                      font=("Arial", "10"), bg="yellow",
                                      width=10, pady=5, command=lambda: self.open_play_box(2))
        self.play_button_mid.grid(row=0, column=1, padx=5)

        self.play_button_high = Button(self.play_button_frame, text="High ($15)",
                                       font=("Arial", "10"), bg="orange",
                                       width=10, pady=5, command=lambda: self.open_play_box(3))
        self.update_balance()
        self.play_button_high.grid(row=0, column=2, padx=5)

    def open_play_box(self, stakes):
        self.stakes = stakes
        Play(self)
        root.withdraw()

    def update_balance(self):
        self.balance = number_checker(self.money_entry.get())
        if type(self.balance) == int:
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

        elif self.balance == "Too High":
            self.error_label.config(text="No adding more than $50")
        elif self.balance == "Too Low":
            self.error_label.config(text="No adding less than $0")
        else:
            self.error_label.config(text="Please enter a valid integer")


class Play:
    def __init__(self, partner):

        self.stakes = partner.stakes

        self.rounds_played = 0

        self.history_list = []

        self.balance = partner.balance

        self.temp_balance = partner.balance

        print(partner.stakes, self.temp_balance)

        if partner.stakes == 1:
            prefix = "low"
        elif partner.stakes == 2:
            prefix = "med"
        else:
            prefix = "high"

        self.prize_list = []
        self.prize_list += 2 * [["Mystery_box_images/lead.gif", 0]]
        self.prize_list += 4 * [["Mystery_box_images/copper_{}.gif".format(prefix), 1]]
        self.prize_list += 5 * [["Mystery_box_images/silver_{}.gif".format(prefix), 2]]
        self.prize_list += [["Mystery_box_images/gold_{}.gif".format(prefix), 5]]

        background = "bisque"

        # Sets up child window (ie) play box

        self.play_box = Toplevel()

        self.play_box.protocol('WM_DELETE_WINDOW', partial(root.destroy))

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

        self.play_text = Label(self.play_frame, text="instructions here",
                               justify=LEFT, width=40,
                               bg=background, wrap=250,)
        self.play_text.grid(row=1)

        # Mystery boxes images (Image Labels, row 2)

        self.image_frame = Frame(self.play_frame, width=300, bg=background)
        self.image_frame.grid(row=2)

        self.image_1 = PhotoImage(file="Mystery_box_images/question.gif")
        self.image_box_1 = Label(self.image_frame, image=self.image_1)
        self.image_box_1.grid(row=0, column=0, padx=5)

        self.image_2 = PhotoImage(file="Mystery_box_images/question.gif")
        self.image_box_2 = Label(self.image_frame, image=self.image_2)
        self.image_box_2.grid(row=0, column=1, padx=5)

        self.image_3 = PhotoImage(file="Mystery_box_images/question.gif")
        self.image_box_3 = Label(self.image_frame, image=self.image_3)
        self.image_box_3.grid(row=0, column=2, padx=5)

        # Spin button (button, row 3)

        self.spin_button = Button(self.play_frame, text="Open Boxes! (Cost: ${})".format(partner.stakes * 5),
                                  padx=80, pady=10,
                                  font=("Arial", "10", "bold"), command=partial(self.open_boxes, partner))
        self.spin_button.grid(row=3, pady=10)

        # Balance label (label, row 4)

        self.balance_text = Label(self.play_frame,
                                  text="Game cost: ${}\nBalance: ${}".format(partner.stakes * 5, self.temp_balance),
                                  width=40, bg=background, wrap=250)
        self.balance_text.grid(row=4)

        # Export / Help buttons (row 5)

        self.export_help_frame = Frame(self.play_frame, bg=background, pady=10)
        self.export_help_frame.grid(row=5)

        self.help_button = Button(self.export_help_frame, text="Help / Rules",
                                  font=("Arial", "14"),
                                  padx=10, pady=3, command=self.open_help)
        self.help_button.grid(row=0, column=0, padx=5)

        self.export_button = Button(self.export_help_frame, text="Game Stats",
                                    font=("Arial", "14"),
                                    padx=10, pady=3, command=self.open_history)
        self.export_button.grid(row=0, column=1, padx=5)

        # quit button (row 6)

        self.quit_button = Button(self.play_frame, text="Quit",
                                  padx=80, pady=10,
                                  font=("Arial", "10", "bold"), command=partial(root.destroy))
        self.quit_button.grid(row=6, pady=10)

    def open_boxes(self, partner):
        prize_1 = self.prize_list[randint(0, 11)]
        prize_2 = self.prize_list[randint(0, 11)]
        prize_3 = self.prize_list[randint(0, 11)]
        self.image_1.config(file=prize_1[0])
        self.image_2.config(file=prize_2[0])
        self.image_3.config(file=prize_3[0])
        self.temp_balance -= 5 * partner.stakes
        earnings = prize_1[1]*partner.stakes + prize_2[1]*partner.stakes + prize_3[1]*partner.stakes
        loss = prize_1[1]*partner.stakes + prize_2[1]*partner.stakes + prize_3[1]*partner.stakes - partner.stakes * 5
        self.temp_balance += earnings
        self.rounds_played += 1

        self.history_list.append(earnings)

        payout_text = "\nGame cost: ${}\nPayout: ${}\n".format(partner.stakes * 5, earnings)

        if earnings > partner.stakes * 5:
            self.balance_text.config(text="You won ${}!{}Balance: ${}".format(loss, payout_text,
                                                                              self.temp_balance))
        elif earnings < partner.stakes * 5:
            self.balance_text.config(text="You lost ${}.{}Balance: ${}".format(-1 * loss, payout_text,
                                                                               self.temp_balance))
        else:
            self.balance_text.config(text="You didn't win anything.{}Balance: ${}".format(payout_text,
                                                                                          self.temp_balance))

        if self.temp_balance < partner.stakes * 5:
            self.spin_button.configure(state=DISABLED)
            error_append = self.balance_text.cget("text") + "\nGame over. " \
                                                            "You have run out of funds and can no longer play. " \
                                                            "You may export or quit the game."
            self.balance_text.config(text=error_append)

    def open_history(self):
        self.export_button.configure(state=DISABLED)
        get_history = History(self)
        get_history.history_text.config(justify=LEFT)

    def open_help(self):
        self.help_button.configure(state=DISABLED)
        get_help = Help(self)
        get_help.help_text.config(text="Choose an amount to play with and then choose the stakes. "
                                       "Higher stakes will cost more per round but you can win more as well.\n\n"
                                       "When you enter the play area, wou will see three mystery boxes. "
                                       "To reveal the contents of the boxes, click the `Open Boxes` button. "
                                       "If you don't have enough money to play, "
                                       "the button will turn red and you will need to quit the game.\n\n"
                                       "The contents of the boxes will be added to your balance. "
                                       "The boxes could contain...\n\n"
                                       "Low: Lead($0) | Copper($1) | Silver($2) | Gold($5)\n\n"
                                       "Medium: Lead($0) | Copper($2) | Silver($4) | Gold($10)\n\n"
                                       "High: Lead($0) | Copper($3) | Silver($6) | Gold($15)\n\n"
                                       "If each box contains gold, you will earn $30 (low stakes). "
                                       "If they contained copper, silver, and gold, "
                                       "you would receive $13 ($1 + $2 + $10) and so on.")


class Help:
    def __init__(self, partner):
        background = "bisque"

        self.help_box = Toplevel()

        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Help frame

        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        self.help_title = Label(self.help_frame, justify=LEFT, text="Help / Payout Schedule",
                                font=("Arial", "14", "bold"), bg=background, anchor='nw')
        self.help_title.grid(row=0)

        self.help_text = Label(self.help_frame, justify=LEFT, bg=background, wrap=400)
        self.help_text.grid(row=1, padx=5)

        self.exit_button = Button(self.help_frame, text="Close", command=partial(self.close_help, partner),
                                  width=20,
                                  pady=5)
        self.exit_button.grid(row=2, pady=5)

    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


class History:
    def __init__(self, partner):

        background = "bisque"

        self.history_list = partner.history_list

        self.stakes = partner.stakes

        # Sets up child window (ie) history box
        self.history_box = Toplevel()

        # If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, width=400, bg=background)
        self.history_frame.grid()
        # Set up History heading (row 0)
        self.history_label = Label(self.history_frame, text="Game Stats",
                                   font=("Arial", "14", "bold"),
                                   bg=background,
                                   padx=10, pady=10, justify=LEFT)
        self.history_label.grid(row=0)

        # History text (label, row 1)

        if partner.balance - partner.temp_balance <= 0:
            won_lost_text = "Won"
            amount_won_lost = partner.temp_balance - partner.balance
        else:
            won_lost_text = "Lost"
            amount_won_lost = partner.balance - partner.temp_balance
        self.text_entry = "Starting Balance: ${}\n\n" \
                          "Current Balance: ${}\n\n" \
                          "Amount {}: ${}\n\n" \
                          "Rounds Played: {}".format(partner.balance,
                                                     partner.temp_balance,
                                                     won_lost_text,
                                                     amount_won_lost,
                                                     partner.rounds_played)
        self.history_text = Label(self.history_frame, text=self.text_entry,
                                  justify=LEFT, width=40,
                                  bg=background, wrap=250)
        self.history_text.grid(row=1)

        # History entries

        self.export_instructions = Label(self.history_frame, fg="green", text="Please use the \'Export\' button to "
                                                                              "generate a text file showing\nyour "
                                                                              "statistics amd the results of each "
                                                                              "round you played",
                                         bg=background, justify=LEFT)
        self.export_instructions.grid(row=2)

        # Dismiss / export buttons (row 3)
        self.export_calc_history_dismiss_frame = Frame(self.history_frame)
        self.export_calc_history_dismiss_frame.grid(row=3, pady=10)

        self.export_button = Button(self.export_calc_history_dismiss_frame, text="Export Calculation History",
                                    font=("Arial", 10, "bold"),
                                    padx=10, pady=5,
                                    command=self.export)
        self.export_button.grid(row=0, column=0)

        self.dismiss_btn = Button(self.export_calc_history_dismiss_frame, text="Dismiss",
                                  font="arial 10 bold",
                                  padx=10, pady=5,
                                  command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=0, column=1)

    def export(self):
        get_export = Export(self)
        get_export.export_text.configure(text="Enter a filename below and press export to export all previous "
                                              "calculations to a text file")

    def close_history(self, partner):
        # Put history button back to normal...

        partner.export_button.config(state=NORMAL)
        self.history_box.destroy()


class Export:
    def __init__(self, partner):

        background = "bisque"

        # disable export button
        partner.export_button.config(state=DISABLED)
        partner.dismiss_btn.config(state=DISABLED)

        # Sets up child window (ie) export box
        self.export_box = Toplevel()

        # If users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.dismiss_check, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()
        # Set up Export heading (row 0)
        self.export_label = Label(self.export_frame, text="Export Calculation History",
                                  font=("Arial", "14", "bold"),
                                  bg=background,
                                  padx=10, pady=10)
        self.export_label.grid(row=0)

        # Export text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 justify=LEFT, width=40,
                                 bg=background, wrap=250, )
        self.export_text.grid(row=1)

        # File name input

        self.file_name_input = Entry(self.export_frame, width=20,
                                     font=("Arial", 14, "bold"))
        self.file_name_input.grid(row=2)

        self.export_dismiss_frame = Frame(self.export_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export button (row 2)
        self.export_btn = Button(self.export_dismiss_frame, text="Export",
                                 padx=10, pady=5, font="arial 10 bold",
                                 command=partial(self.press_export, partner))
        self.export_btn.grid(row=0, column=0)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.export_dismiss_frame, text="Dismiss",
                                  padx=10, pady=5, font="arial 10 bold",
                                  command=partial(self.dismiss_check, partner))
        self.dismiss_btn.grid(row=0, column=1)

    def dismiss_check(self, partner):
        if partner.history_box.winfo_exists():
            # Put export button back to normal...
            partner.export_button.config(state=NORMAL)
            partner.dismiss_btn.config(state=NORMAL)
            self.export_box.destroy()
        else:
            # prevents errors if history box is closed first
            self.export_box.destroy()

    def press_export(self, partner):
        chosen_name = self.file_name_input.get()
        regex_check_result = regex_check(chosen_name)
        if regex_check_result == "No Error":
            text_file = open("{}.txt".format(chosen_name), "w")
            text_file.write("{}\n\n".format(partner.text_entry))
            text_file.write("Full round history:\n\n")
            text_file.write("Cost Per Round: ${}\n\n".format(partner.stakes))

            loop_count = 1

            for x in partner.history_list:
                text_file.write("Round {} Payout: ${}\n".format(loop_count, x))
                loop_count += 1
            text_file.close()
            self.export_text.config(text="Success!")

        else:
            self.export_text.config(text=regex_check_result)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery boxes")
    something = Start()
    root.mainloop()
