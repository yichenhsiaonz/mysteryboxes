from tkinter import *
import random


class Foo:
    def __init__(self, parent):
        print("hello world")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Foo(root)
    root.mainloop()
