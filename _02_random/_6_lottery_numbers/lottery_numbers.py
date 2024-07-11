import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    rand_nubs = random.randint(0, 9)
    rand_nubs1 = random.randint(0, 9)
    rand_nubs2 = random.randint(0, 9)
    rand_nubs3 = random.randint(0, 9)
    rand_nubs4 = random.randint(0, 9)
    rand_nubs5 = random.randint(0, 9)

    grand_nubs = random.randint(0, 9)
    grand_nubs1 = random.randint(0, 9)
    grand_nubs2 = random.randint(0, 9)
    grand_nubs3 = random.randint(0, 9)
    grand_nubs4 = random.randint(0, 9)
    grand_nubs5 = random.randint(0, 9)

    score = 0
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo(None, str(rand_nubs) + str(rand_nubs1) + str(rand_nubs2) + str(rand_nubs3) + str(rand_nubs4) + str(rand_nubs5))
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
    if rand_nubs == grand_nubs:
        score + 1

    elif rand_nubs1 == grand_nubs1:
        score + 1

    elif rand_nubs2 == grand_nubs2:
        score + 1

    elif rand_nubs3 == grand_nubs3:
        score + 1

    elif rand_nubs4 == grand_nubs4:
        score + 1

    elif rand_nubs5 == grand_nubs5:
        score + 1

    if score == 6:
        messagebox.showinfo(message='you won')
    else:
        messagebox.showinfo(message='you lost')
