from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    global letters, numbers, symbols
    pass_entry.delete(0, END)
    nb_letters = random.randint(8,10)
    nb_numbers = random.randint(2,4)
    nb_symbols = random.randint(2,4)
    let_comp = [random.choice(letters) for i in range(0,nb_letters)]
    num_comp = [random.choice(numbers) for i in range(0,nb_numbers)]
    sym_comp = [random.choice(symbols) for i in range(0,nb_symbols)]
    prov = let_comp + num_comp + sym_comp
    password ="".join(prov)
    pass_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    global web_entry, pass_entry, user_entry
    web = web_entry.get()
    pas = pass_entry.get()
    user = user_entry.get()
    temp_dict = {web:{"Username:":user, "Password:": pas}}
    if min(len(web), len(pas))==0:
        messagebox.askokcancel(title="Empty spaces", message="Please fill all the spaces")
    else:
        validation = messagebox.askokcancel(title=website, message = f"These are the details entered:\nEmail: "
                                                                     f"{web}\nUsername: {user}\nPassword: {pas}")
        if validation:
            try:
                with open("passwords.json", "r") as f:
                    data = json.load(f)
            except FileNotFoundError:
                with open("passwords.json", "w") as f:
                    json.dump(temp_dict, f, indent=4)
            else:
                with open("passwords.json", "w") as f:
                    data.update(temp_dict)
                    json.dump(data, f, indent=4)
            finally:

                pass_entry.delete(0, END)
                web_entry.delete(0, END)
##--------------------------------- Search Password ---------------------------------######
def search():
    if len(web_entry.get())==0:
        messagebox.askokcancel(title="Empty space", message="Please enter a website")
    else:
        web = web_entry.get()
        try:
            with open("passwords.json", "r") as f:
                try:
                    temp_dict = json.load(f)[web]
                except KeyError:
                    messagebox.askokcancel(title="Error", message="There is no password for this website.")
                else:
                    messagebox.askokcancel(title=f"{web}", message=f"Username:{temp_dict['Username:']}\n"
                                                               f"Password:{temp_dict['Password:']}")
        except FileNotFoundError:
            messagebox.askokcancel(title=f"{Error}", message="There are no password saved yet.")





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(width=400, height=500, padx=50, pady=50)
logo = PhotoImage(file="logo.png")
##CANVAS
canvas = Canvas()
canvas.create_image(120, 120, image=logo)

##LABELS
website = Label()
username = Label()
password = Label()

##BUTTONS
generate_button = Button()
add_button = Button()
search_button = Button()
##ENTRIES
web_entry = Entry()
user_entry = Entry()
pass_entry = Entry()

##LAYOUT
canvas.grid(row=0, column=1)
website.grid(row=1, column=0)
username.grid(row=2, column=0)
password.grid(row=3, column=0, padx=0)
generate_button.grid(row=3, column=2, ipadx=0, sticky="w")
add_button.grid(row=4, column=1, columnspan=2, sticky="e")
search_button.grid(row=1, column=2, sticky ="w")
web_entry.grid(row=1, column=1, sticky="e")
user_entry.grid(row=2, column=1, columnspan=2, sticky="e")
pass_entry.grid(row=3, column=1, ipadx=0, sticky="e")

##CONFIG
website.config(text="Website:")
username.config(text="Username:")
password.config(text="Password:")
generate_button.config(text="Generate", command=generate, width=13)
add_button.config(text="Add", command=add, width=37)
search_button.config(text="Search", command=search, width=13)
user_entry.config(width=36)
web_entry.config(width=22)
pass_entry.config(width=22)
web_entry.focus()
user_entry.insert(0, "denis_langford@hotmail.com")


window.mainloop()
