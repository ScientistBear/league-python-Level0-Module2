import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    random_numbe1 = 1
    random_number = random.randint(1, 5)
    if random_number == 5:
        random_numbe1 = random.randint(1, 100000000000)
    else:
        random_number = 2
    print(random_number)


    # TODO 1) Use each value of random_number to give the user a random compliment
    if random_number == 1:
        messagebox.showinfo(message='ur cool')
    elif random_number == 2:
        messagebox.showinfo(message='ur awesome')
    elif random_number == 3:
        messagebox.showinfo(message='i like ur shirt')
    elif random_number == 4:
        messagebox.showinfo(message='i like ur shoes')
    if random_numbe1 == 1111111111:
        messagebox.showinfo(message='you got the rare message. ur lucky')
    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
