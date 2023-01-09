import tkinter as tk


def default_bg_color(widget):

    _ = widget.__class__(widget.master)
    widget['bg'] = _['bg']
    _.destroy()


if __name__ == '__main__':

    root = tk.Tk()

    # tk.Label can be replaced with any widget that has bg option
    label = tk.Label(root, text="This is the red label.", bg='red')
    btn = tk.Button(root, text="Default color!")
    btn['command'] = lambda widget=label: default_bg_color(widget)

    label.pack()
    btn.pack()
    root.mainloop()