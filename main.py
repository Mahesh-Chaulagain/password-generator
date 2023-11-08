from tkinter import *   # import only constants and classes but not modules
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.randint(8, 10)  # take 8 to 10 letters
    # nr_symbols = random.randint(2, 4)   # take 2 to 4 symbols
    # nr_numbers = random.randint(2, 4)   # take 2 to 4 numbers

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)    # copy password to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    # fetch the current entries text
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()

    # Validate data
    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")

    else:
        # Top-up box
        is_ok = messagebox.askokcancel(title=website_data, message=f"These are the details entered:"
                                                          f"\nEmail:{email_data}"
                                                          f"\nPassword:{password_data}"
                                                          f"\n Is it ok to save?")

        if is_ok:
            with open("data.txt", mode='a') as data_file:
                data_file.write(f"{website_data} | {email_data} | {password_data} \n")

                # Delete the entry data
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
# Add padding
window.config(padx=50, pady=50)

# Set canvas
canvas = Canvas(width=200, height=200)
# Select image
logo_img = PhotoImage(file="logo.png")
# Create image inside canvas
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
# focus the cursor in the entry
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
# populate field with commonly used email
email_entry.insert(0, "example@email.com")
password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
