import tkinter as tk
from tkinter import Button, Scrollbar,Listbox

def divisible(x,y):
    d = []
    for i in range(x,y):
        if (i%2==0) and (i%5!=0):
            d.append(str(i))
    
    nwindow = tk.Tk()
    nwindow.geometry('400x200')
    nwindow.title('Divisible numbers - output')
    scroll_bar = Scrollbar(nwindow)
    scroll_bar.pack(side='right', fill = 'y' )

    nlist = Listbox(nwindow, yscrollcommand= Scrollbar.set)
    nlist.pack(side='left', fill='both')
    scroll_bar.config(command=nlist.yview)
    
    for number in d:
        nlist.insert('end', number)

def check_user_input():
    ebox1 = entry_box1.get()
    ebox2 = entry_box2.get()
    
    try:
        x = int(ebox1)
        try:
            y = int(ebox2)
        except ValueError:
            error_box['text'] = 'please enter a username'
    except ValueError:
        error_box['text'] = 'please enter a password'
    else:
        divisible(x, y)

window = tk.Tk()
window.geometry('400x200')
window.title('Divisible numbers')

label1 = tk.Label(text = 'enter your first number: ')
label1.place(x = 10, y = 20, height = 25)
entry_box1 = tk.Entry(text = '')
entry_box1.place(x = 10, y = 40, height = 25)
label2 = tk.Label(text = 'enter your secpond number: ')
label2.place(x = 10, y = 80, height = 25)
entry_box2 = tk.Entry(text = '')
entry_box2.place(x = 10, y = 100, height = 25)

button = tk.Button(text = 'click here for result', command=check_user_input)
button.config(font = 16)
button.place(x = 10, y = 170, width = 380, height = 35)
button_quit = Button(window, text='exit program', command=window.quit)
button_quit.pack()
button.place(x = 5, y = 170, width = 340, height = 35)

error_box = tk.Label(text= '')
error_box.place(x = 10, y = 130)

window.mainloop()