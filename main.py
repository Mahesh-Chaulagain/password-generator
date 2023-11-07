from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    with open("data.txt", mode='a') as data_file:
        website_data = website_entry.get()
        email_data = email_entry.get()
        password_data = password_entry.get()

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
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
