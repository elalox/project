from tkinter import *
from tkinter import ttk
import database

window = Tk()
window.title('Authorization')
window.geometry('450x230')
window.resizable(False, False)

font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)

notebook.add(frame1, text="Sign In")
notebook.add(frame2, text="Register")

n = ''
def clicked():
    global n
    username = username_entry.get()
    password = password_entry.get()
    print(username, password)
    print(type(username), type(password))
    if database.check_user(username, password) == True:
        n = username
        window.destroy()

    else:
        print("Invalid")
        exit()


def reg_command():
    name = reg_username_entry.get()
    password = reg_password_entry.get()
    database.add_user(name, password)

# Title
reg_main_label = Label(frame2, text='Registration', font=font_header, justify=CENTER, **header_padding)
reg_main_label.pack()

# Username
reg_username_label = Label(frame2, text='Useranme', font=label_font, **base_padding)
reg_username_label.pack()

reg_username_entry = Entry(frame2, bg='#fff', fg='#444', font=font_entry)
reg_username_entry.pack()

# Password
reg_password_label = Label(frame2, text='Password', font=label_font, **base_padding)
reg_password_label.pack()

reg_password_entry = Entry(frame2, bg='#fff', fg='#444', font=font_entry)
reg_password_entry.pack()

# Button
reg_send_btn = Button(frame2, text='Register', command=reg_command)
reg_send_btn.pack(**base_padding)



# Title
main_label = Label(frame1, text='Sign In', font=font_header, justify=CENTER, **header_padding)
main_label.pack()

# Username
username_label = Label(frame1, text='Useranme', font=label_font , **base_padding)
username_label.pack()

username_entry = Entry(frame1, bg='#fff', fg='#444', font=font_entry)
username_entry.pack()

# Password
password_label = Label(frame1, text='Password', font=label_font , **base_padding)
password_label.pack()

password_entry = Entry(frame1, bg='#fff', fg='#444', font=font_entry)
password_entry.pack()

# Button
send_btn = Button(frame1, text='Sign In', command=clicked)
send_btn.pack(**base_padding)



window.mainloop()