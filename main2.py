import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from configparser import ConfigParser

def icon(name):
    ico = Image.open('ico.jpg')
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
        a, b = i.split(",")
        b = b.strip()
        if name == a and password == b:
            window.destroy()
            new_window()
        else:
            name_var.set("")
            passw_var.set("")


def new_window():
    global app
    app = tk.Tk()
    app.title('Hasbolah')
    app.resizable(True, True)
    mid(app)
    icon(app)
    global fra
    fra = tk.Frame(app)
    fra.place(x=10, y=10)
    global btn_1
    btn_1 = tk.Button(app, command=settings, text='Settings', width=7, height=1, relief=GROOVE)
    btn_1.place(x=238, y=3)
    app.mainloop()


def settings():
    # ===========================================================
    def var_dump(var, prefix=''):
        """
        You know you're a php developer when the first thing you ask for
        when learning a new language is 'Where's var_dump?????'
        """
        my_type = '[' + var.__class__.__name__ + '(' + str(len(var)) + ')]:'
        print(prefix, my_type, sep='')
        prefix += '    '
        for i in var:
            if type(i) in (list, tuple, dict, set):
                var_dump(i, prefix)
            else:
                if isinstance(var, dict):
                    print(prefix, i, ': (', var[i].__class__.__name__, ') ', var[i], sep='')
                else:
                    print(prefix, '(', i.__class__.__name__, ') ', i, sep='')

    # ===========================================================
    lab = tk.Label(fra, text="Wybierz wygląd okna")
    lab.pack(padx=1, pady=1)

    var = IntVar()
    R1 = Radiobutton(app, text="WHITE", variable=var, value=1)
    R1.place(x=25, y=30)
    # R1.select()

    R2 = Radiobutton(app, text="DARK", variable=var, value=2)
    R2.place(x=115, y=30)

    btn_1.config(state=DISABLED)


    config = ConfigParser()
    config.read('config.ini')
    # print(config.get('main','radio'))
    # print(config['main']['radio'])
    # var.set(1)
    E = config['main']['radio']

    if E == 'R1':
        R1.select()
    elif E == 'R2':
        R2.select()
    else:
        messagebox.showerror("Error", "Sprawdź ustawienia pliku config.ini")
    # config['main']['radio'].select()

    # F = str(E)
    # print(E)
    #
    # def gif():
    #     F = select()
    #     G = config['main']['radio']
    #     return G +"."+ F
    # gif()
    #
    # E.format(select())
    # select(F)
    # select(E)



    def save():
        print(str(var.get()))

    R3 = Button(app, text="Zapisz", command=save)
    R3.place(x=6, y=170)

window = tk.Tk()
window.title('Login')
window.resizable(False, False)
icon(window)
mid(window)

frame = Frame(window)
# frame.pack()
frame.place(relx=.5, rely=.5, anchor="c")

name_var = tk.StringVar()
passw_var = tk.StringVar()
name_label = tk.Label(frame, text='Username', font=('monospace', 10, 'bold'))
name_entry = tk.Entry(frame, textvariable=name_var, font=('calibre', 10, 'normal'))
passw_label = tk.Label(frame, text='Password', font=('calibre', 10, 'bold'))
passw_entry = tk.Entry(frame, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')
sub_btn = tk.Button(frame, text='Submit', command=submit, width=20)

# name_entry.focus()
name_entry.insert(END, '1')
passw_entry.insert(END, '1')

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

window.mainloop()



