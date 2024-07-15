import random
import string
from tkinter import Tk, Canvas, Label, Button, PhotoImage, Entry, messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generatePassword():
    number = random.randint(9, 12)
    characters = string.ascii_letters + string.digits + string.punctuation
    randompassword = "".join(random.choice(characters) for i in range(number))
    passwordEntry.insert(0, randompassword)


# ---------------------------- SAVE PASSWORD ------------------------------- #
import json
from tkinter import messagebox


def savePassword():
    # Check for Empty Inputs
    if not websiteEntry.get() or not passwordEntry.get() or not userEntry.get():
        messagebox.showerror("Error", "Please enter a valid website, username, and password.")
        return
    # Retrieve Input Values
    website = websiteEntry.get().strip()
    username = userEntry.get().strip()
    password = passwordEntry.get().strip()

    # New entry to be added or updated
    new_entry = {
        website: {
            "username": username,
            "password": password
        }
    }

    # Initialize data dictionary
    data = {}

    # Attempt to read existing data from the file
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo("Info", "Data file not found. A new one will be created.")
        with open("data.json", "w") as file:
            json.dump(new_entry)
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Data file is corrupt or not in proper JSON format.")
        return
    data.update(new_entry)
    try:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while writing to the file: {e}")
        return

    # Clear Input Fields after successful operation
    websiteEntry.delete(0, 'end')
    userEntry.delete(0, 'end')
    passwordEntry.delete(0, 'end')

    # Inform the user of success
    messagebox.showinfo("Success", "Your credentials have been saved successfully.")


# ---------------------------- GET PASSWORD ------------------------------- #
def getPassword():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError as e:
        messagebox.showerror("Error", "Data file not found.")
        return
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Data file is corrupt or not in proper JSON format.")
        return
    site = websiteEntry.get().strip()
    user = userEntry.get().strip()
    if site in data and data[site]["username"]==user:
        passwordEntry.delete(0, 'end')  # Clear any existing content in passwordEntry
        password = data[site]["password"]
        passwordEntry.insert(0, password)
    else:
        messagebox.showinfo("Info","No such site/username combo exists.")
        websiteEntry.delete(0, 'end')
        userEntry.delete(0, 'end')



# ---------------------------- UI SETUP ------------------------------- #
tk = Tk()
tk.title("Password Manager")
tk.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)

photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

websiteLabel = Label(text="Site")
websiteLabel.grid(row=2, column=0)
userNameLabel = Label(text="User")
userNameLabel.grid(row=3, column=0)
passwordLabel = Label(text="Password")
passwordLabel.grid(row=4, column=0)

websiteEntry = Entry(width=35)
websiteEntry.grid(column=1, row=2)
userEntry = Entry(width=35)
userEntry.grid(column=1, row=3)
passwordEntry = Entry(width=35)
passwordEntry.grid(column=1, row=4)

generatePasswordButton = Button(text="Generate", command=generatePassword)
generatePasswordButton.grid(row=4, column=2)
addButton = Button(text="Add", width=15, command=savePassword)
addButton.grid(row=5, column=1, columnspan=2)

getPasswordButton = Button(text="GetPassword", command=getPassword)
getPasswordButton.grid(row=2, column=2)

tk.mainloop()
