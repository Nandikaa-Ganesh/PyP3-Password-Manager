from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT = "Amithen"
SIZE = 15

CREAM = "#F1ECC3"
YELLOW = "#FFD523"
D_BLUE = "#FF7600"
BLACK = "#B2B1B9"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    p_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    p_word = []
    p_word_l = [random.choice(letters) for _ in range(0, nr_letters)]
    p_word_s = [random.choice(symbols) for _ in range(0, nr_symbols)]
    p_word_n = [random.choice(numbers) for _ in range(0, nr_numbers)]
    p_word = p_word_l + p_word_s + p_word_n
    random.shuffle(p_word)
    password = "".join(p_word)
    p_entry.insert(0,password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Password", message=f"Your password {password} is copied to the clipboard")



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    email_name = e_entry.get()
    password_name = p_entry.get()
    website_name = w_entry.get()

    if len(email_name) == 0 or len(password_name) == 0 or len(website_name) == 0:
        messagebox.showinfo(title="Field Empty!!", message="Do not leave any field empty!")
    else:
        message = messagebox.askokcancel(title=website_name,
                                         message=f"These are the credentials you have entered:\n\nWebsite name:     {website_name}\nEmail/Username:     {email_name}\nPassword:     {password_name}")

        if message:
            pyperclip.copy(password_name)
            messagebox.showinfo(title="Password", message=f"Your password {password_name} is copied to the clipboard")
            with open("data.txt", 'a') as f:
                data = (website_name + " | " + email_name + " | " + password_name + "\n")
                f.write(data)
            p_entry.delete(0, END)
            w_entry.delete(0, END)
            w_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50, bg=YELLOW)
window.title("Password Manager")

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website = Label(text="Website :", bg=YELLOW, font=(FONT, SIZE, "normal"))
website.grid(column=0, row=1)

email = Label(text="Email / Username :", bg=YELLOW, font=(FONT, SIZE, "normal"))
email.grid(column=0, row=2)
password = Label(text="Password :", bg=YELLOW, font=(FONT, SIZE, "normal"))
password.grid(column=0, row=3)

w_entry = Entry(width=41)
w_entry.grid(column=1, row=1, columnspan=2, sticky="W")
w_entry.focus()
e_entry = Entry(width=41)
e_entry.grid(column=1, row=2, columnspan=2, sticky="W")
e_entry.insert(0, " ")  #your default email address goes here
p_entry = Entry(width=25)
p_entry.grid(column=1, row=3, sticky="EW")

gp = Button(text="Generate", bg=D_BLUE, font=("mv boli", 8, "normal"), borderwidth=0, command=generate_password)
gp.grid(column=2, row=3)

add = Button(text="Add", width=35, bg=D_BLUE, font=("mv boli", 8, "normal"), borderwidth=0, command=save_password)
add.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
