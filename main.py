import tkinter as tk
from tkinter import *
from PIL import  ImageTk, Image

def icon(name):
    ico = Image.open(r'C:\Users\Neo\PycharmProjects\pythonProject\ico.jpg')
    photo = ImageTk.PhotoImage(ico)
    name.wm_iconphoto(False, photo)

def mid(name):
    width = 500
    height = 350
    screen_width = name.winfo_screenwidth()
    screen_height = name.winfo_screenheight()

    center_x = int(screen_width / 2 - width / 2)
    center_y = int(screen_height / 2 - height / 2)

    name.geometry("%dx%d+%d+%d" % (width, height, int(center_x), int(center_y)))
    name.geometry("300x200")
def submit():
    name = name_var.get()
    password = passw_var.get()

    lines = open("login.txt", "r")
    for i in lines:
        a,b = i.split(",")
        b = b.strip()
        if name == a and password == b:
            window.destroy()
            new_window()
        else:
            name_var.set("")
            passw_var.set("")


def new_window():
    app = tk.Tk()
    app.title('Hasbolah')
    app.resizable(True, True)
    mid(app)
    icon(app)
    fra = Frame(app, width=160, height=170, bg="yellow")
    fra.place(x=10,y=10)
    btn_1 = tk.Button(app, command=settings, text='Settings', width=7, height=1, relief=GROOVE)
    btn_1.place(x=238,y=3)

    app.mainloop()

def settings():
    lab = tk.Label(fra, text="HELLO")
    lab.pack()
    lab.grid(row="0", column="0")




window = tk.Tk()
window.title('Login')
window.resizable(False,False)
icon(window)
mid(window)

frame = Frame(window)
# frame.pack()
frame.place(relx=.5,rely=.5,anchor="c")

name_var = tk.StringVar()
passw_var = tk.StringVar()
name_label = tk.Label(frame, text='Username', font=('monospace', 10, 'bold'))
name_entry = tk.Entry(frame, textvariable=name_var, font=('calibre', 10, 'normal'))
passw_label = tk.Label(frame, text='Password', font=('calibre', 10, 'bold'))
passw_entry = tk.Entry(frame, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')
sub_btn = tk.Button(frame, text='Submit', command=submit, width=20)

# name_entry.focus()
name_entry.insert(END, '1')
passw_entry.insert(END,'1')

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

window.mainloop()



