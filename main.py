from tkinter import *
import string
import secrets
import pyperclip
import random


# Function to quickly generate password
def quick_generator():
    """takes the desired password length from pass_len, generates a password using secrets module
and stores it in pass_str, min. requirements are :
    - 2 special characters (punctuation)
    - 2 digits
    - 2 upper characters
    """
    length = pass_len.get()

    alphabet = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))

        if sum(char in string.punctuation for char in password) >= 2 \
                and sum(char in string.digits for char in password) >= 2 \
                and sum(char.isupper() for char in password) >= 2:
            return pass_str.set(password)


# Function to custom generate password
def custom_func():
    def custom_generator():
        choice_dict = {'special': string.punctuation, 'upper': string.ascii_uppercase,
                       'lower': string.ascii_lowercase, 'digits': string.digits}
        choice_dict['all'] = ''.join(choice_dict.values())

        nonlocal count_input
        count_input = {'special': special_entry.get(), 'upper': upper_entry.get(), 'lower': lower_entry.get(), 'digits': digits_entry.get()}

        try:
            count_input = {k: int(v or 0) for k, v in count_input.items() if int(v or 0) > 0}
        except ValueError:
            custom_message.config(text="Fields must be integer")
            return

        req_sum = sum(count_input.values())
        if req_sum > length:
            custom_message.config(text=f"Sum of requirements is {req_sum}\n while chosen length is {length}")
            return
        if req_sum < length:
            count_input['all'] = length - req_sum

        password = ''
        for char_type in count_input:
            password += ''.join(secrets.choice(choice_dict[char_type]) for _ in range(count_input[char_type]))
        password = ''.join(random.sample(password, len(password)))

        custom_win.destroy()
        pass_str.set(password)
        return

    length = pass_len.get()
    count_input = {}

    custom_win = Tk()
    custom_win.geometry("+450-250")
    custom_win.resizable(False, False)
    custom_win.title("Custom Generate")
    custom_win.configure(bg=default_color, padx=15, pady=15)

    # Take input of amount of special characters wanted in password
    special_label = Label(custom_win, text='Special Characters :', font=default_font, bg=default_color, fg='white')
    special_entry = Entry(custom_win, font=default_font, width=5)

    # Take input of amount of upper characters wanted in password
    upper_label = Label(custom_win, text='Upper Characters :', font=default_font, bg=default_color, fg='white')
    upper_entry = Entry(custom_win, font=default_font, width=5)

    # Take input of amount of lower characters wanted in password
    lower_label = Label(custom_win, text='Lower Characters :', font=default_font, bg=default_color, fg='white')
    lower_entry = Entry(custom_win, font=default_font, width=5)

    # Take input of amount of digits wanted in password
    digits_label = Label(custom_win, text='Digits :', font=default_font, bg=default_color, fg='white')
    digits_entry = Entry(custom_win, font=default_font, width=5)

    # Button to generate password with current entries
    generate_button = Button(custom_win, text='Generate', command=custom_generator, font=default_font, bg="#8a90a1")

    # Label to display message to user (error, feedback etc.)
    custom_message = Label(custom_win, text='', font=default_font, bg=default_color, fg='white')

    special_label.grid(column=0, row=0)
    special_entry.grid(column=1, row=0)
    upper_label.grid(column=0, row=1)
    upper_entry.grid(row=1, column=1)
    lower_label.grid(column=0, row=2)
    lower_entry.grid(row=2, column=1)
    digits_label.grid(column=0, row=3)
    digits_entry.grid(row=3, column=1)
    generate_button.grid(row=4, columnspan=2, pady=10)
    custom_message.grid(row=5, columnspan=2)


# Function to copy generated password to clipboard
def copy_password():
    """copies the password stored in pass_str and copies to clipboard using pyperclip module"""
    pyperclip.copy(pass_str.get())
    if pass_str.get() != '':
        # Message to user after password successfully copied
        root_message.config(text="Password Copied")
    else:
        # Message to user if copy password clicked and entry line is empty
        root_message.config(text="Generate a password to copy it")


def help_func():
    help_win = Tk()
    help_win.geometry("+450-250")
    help_win.resizable(False, False)
    help_win.title("Help")
    help_win.configure(bg=default_color, padx=15, pady=15)

    help_text = """Hello !
    Welcome to the best password generator !
    All of your questions will soon be answered :)"""
    help_label = Label(help_win, text=help_text, font=default_font, bg=default_color, fg='white')
    help_label.grid(row=0)


def save_func():
    save_win = Tk()
    save_win.geometry("+450-250")
    save_win.resizable(False, False)
    save_win.title("Saved Passwords")
    save_win.configure(bg=default_color, padx=15, pady=15)





root = Tk()
root.resizable(False, False)
root.geometry("+430-225")
root.title("Password Generator")
default_font = ('arial', 12, 'bold')
default_color = "#122554"
root.configure(bg=default_color, padx=20, pady=20)

# Choosing Password Length
length_label = Label(root, text='Password Length', font=default_font, bg=default_color, fg='white')

# Variable to store desired password length, initialized by the following spinbox
pass_len = IntVar()

# User picks password length (integer from 10 to 32) using the spinbox
length_spinbox = Spinbox(root, from_=10, to=32, textvariable=pass_len, width=10, wrap=True, justify='center',
                         font=default_font, state='readonly')

# Variable to store the password , initialized in Generator function
pass_str = StringVar()

# Button to quick generate password
quick_button = Button(root, text="Quick Generate", command=quick_generator, font=default_font, bg="#8a90a1")

# Button to custom generate password
custom_button = Button(root, text="Custom Generate", command=custom_func, font=default_font, bg="#8a90a1")

# Entry line shows the generated password after the button is clicked
output = Entry(root, textvariable=pass_str, font=default_font, width=35)

# Button to copy generated password to clipboard
copy_button = Button(root, text="Copy To Clipboard", command=copy_password, font=default_font, bg="#8a90a1")

# Button to save password
save_button = Button(root, text="Save Password", command=save_func, font=default_font, bg="#8a90a1")

# Exit button to shut down program
exit_button = Button(root, text="Exit", command=root.destroy, font=default_font, bg="#8a90a1")

# Help button to open a window of FAQ
help_button = Button(root, text="Help", command=help_func, font=default_font, bg="#8a90a1")

# Label to display message to user (error, feedback etc.)
root_message = Label(root, text='', font=default_font, bg=default_color, fg='white')

# placing widgets in a grid
length_label.grid(column=0, row=0, columnspan=2)
length_spinbox.grid(column=0, row=1, columnspan=2, pady=(5, 10))
quick_button.grid(column=0, row=2)
custom_button.grid(column=1, row=2)
output.grid(row=3, columnspan=2, pady=10)
copy_button.grid(column=0, row=4, columnspan=2, sticky=W)
save_button.grid(column=1, row=4, columnspan=2, sticky=E)
root_message.grid(row=5, columnspan=2, pady=(0, 10))
exit_button.grid(row=6, columnspan=2, sticky=E)
help_button.grid(row=6, columnspan=2, sticky=W)

# Starts main loop
root.mainloop()

"""
TDL:
- error handling 
- add little question mark next to buttons that opens explanation
- add support for writing in spinbox while staying in range and handle errors
- find way to use same function for quick and custom generate
- ask the user if they want to include specific sub-string in custom generate
- convert application to web page ?
- testing ?
"""
