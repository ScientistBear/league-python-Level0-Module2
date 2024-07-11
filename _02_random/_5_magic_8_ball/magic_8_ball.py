import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    simpledialog.askstring(title='', prompt='question plz')
    # Make a variable and initialize it to a random number between 0 and 3
    rand = random.randint(0, 3)
    # If the random number is 0
    if rand == 0:
        messagebox.showinfo(message='yes')
        # tell the user "Yes"
    elif rand == 1:
        messagebox.showinfo(message='no')

    elif rand == 2:
        messagebox.showinfo(message='maybe you should ask Google?')
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
    elif rand == 3:
        messagebox.showinfo(message='idk')
        # write your own answer
