from tkinter import *

root = Tk()
root.title("Settings")
root.geometry("300x400")
root['bg'] = '#873e23'
root.resizable(False, False)

speed = 10
r = 50
g = 153
b = 113

def start():
    root.destroy()

def speed_conf(event):
    global speed
    speed = int(entry_speed.get())

def r_conf(event):
    global r
    r = int(entry_r.get())
def g_conf(event):
    global g
    g = int(entry_g.get())
def b_conf(event):
    global b
    b = int(entry_b.get())

#Title
title = Label(text="Settings", font="Arial 32", bg='#873e23')
title.pack()

# Name
label_name = Label(text="Background: ", font="Arial 16", bg='#873e23')
label_name.place(x=10, y=100)

entry_r = Entry(bg="red")
entry_r.place(x=130, y=105, width=20)

entry_g = Entry(bg="green")
entry_g.place(x=155, y=105, width=20)

entry_b = Entry(bg="blue")
entry_b.place(x=180, y=105, width=20)

#Speed
label_speed = Label(text="Speed: ", font="Arial 16", bg='#873e23')
label_speed.place(x=10, y=150)

entry_speed = Entry()
entry_speed.place(x=100, y=155)


#Alert
label_bg = Label(text="* For saving configuration, press Enter! *", font="Arial 12", bg='#873e23', fg="#0900BA")
label_bg.place(x=10, y=250)

#Events
entry_speed.bind("<Return>", speed_conf)
entry_r.bind("<Return>", r_conf)
entry_g.bind("<Return>", g_conf)
entry_b.bind("<Return>", b_conf)

#Start
button_start = Button(text="Start", bg='#1e81b0', command=start)
button_start.place(x=100, y=300, width=100)

root.mainloop()
