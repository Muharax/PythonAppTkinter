import tkinter as tk
from tkinter import *
from tkinter import messagebox, StringVar
from configparser import ConfigParser
from PIL import ImageTk, Image

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
    if name != '' and password != '':
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
                name_entry.focus()
    else:
        messagebox.showerror("Error", "Uzupełnij dane")
        name_entry.focus()


def new_window():
    global app
    app = tk.Tk()
    app.title('Hasbolah')
    app.resizable(False, False)
    mid(app)
    icon(app)
    global fra
    fra = tk.Frame(app)
    fra.place(x=10, y=10)
    global btn_1
    btn_1 = tk.Button(app, command=settings, text='Settings', width=7, height=1, relief=GROOVE)
    btn_1.place(x=238, y=3)
    app.mainloop()

def save():
    import configparser
    cfg = configparser.ConfigParser()
    vari = var.get()
    print(vari)
    if vari == 'R1':
        print(cfg.sections())
        cfg.add_section('mainn')
        cfg['mainn']['radio'] = 'R1'
        cfg['mainn']['mainCol'] = 'RR1'
        with open('config.ini', 'w') as configfile:
            cfg.write(configfile)

    elif vari == 'R2':
        print(cfg.sections())
        cfg.add_section('mainn')
        cfg['mainn']['radio'] = 'R2'
        cfg['mainn']['mainCol'] = 'RR2'
        with open('config.ini', 'w') as configfile:
            cfg.write(configfile)
    else:
        print(cfg.sections())
        print('GIT')

def settings():
    lab = tk.Label(fra, text="Wybierz wygląd okna")
    lab.pack(padx=1, pady=1)

    global var
    var = StringVar()
    R1 = Radiobutton(app, text="WHITE", variable=var, value='R1', **opt)
    R1.place(x=25, y=30)
    R2 = Radiobutton(app, text="DARK", variable=var, value='R2', **opt)
    R2.place(x=115, y=30)

    btn_1.config(state=DISABLED)

    config = ConfigParser()
    config.read('config.ini')
    E = config['mainn']['radio']

    if E == 'R1':
        R1.select()
    elif E == 'R2':
        R2.select()
    else:
        messagebox.showerror("Error", "Sprawdź ustawienia pliku config.ini")

    R3 = Button(app, text="Zapisz", command=save, **opt)
    R3.place(x=6, y=170)


window = tk.Tk()
window.title('Login')
window.resizable(False, False)

icon(window)
mid(window)

config = ConfigParser()
config.read('config.ini')
EE = config['mainn']['mainCol']

if EE == 'RR1':
    opt = {'bg': '#f0f0f0','font':('calibre',10)}
elif EE == 'RR2':
    opt = {'bg': 'white','font':('calibre',10)}


frame = tk.Frame(window)
# frame.pack()
frame.place(relx=.5, rely=.5, anchor="c")

name_var = tk.StringVar()
passw_var = tk.StringVar()
name_label = tk.Label(frame, text='Username', **opt)
name_entry = tk.Entry(frame, textvariable=name_var, **opt)
passw_label = tk.Label(frame, text='Password', **opt)
passw_entry = tk.Entry(frame, textvariable=passw_var, **opt, show='*')
sub_btn = tk.Button(frame, text='Sign in', command=submit, width=20, **opt)

name_entry.insert(END, '1')
passw_entry.insert(END, '1')

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

window.mainloop()



