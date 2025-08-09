import tkinter

root = tkinter.Tk()
root.title("Password Checker")
root.geometry("450x250")

text = "Enter password:"
font = ("Arial", 14,"bold italic")
label = tkinter.Label(root, text=text, font=font)
label.pack()

password_entry = tkinter.Entry(root, show="*")
password_entry.pack()

password_input = tkinter.StringVar()
access_label = tkinter.Label(root, textvariable=password_input)
access_label.pack()

"""
def modified(event):
    given_text = password_entry.get()
    access_message = ""
    if given_text == "password":
        access_message = "Password correct! Access granted"
    else:
        access_message = "Incorrect password correct. Try again."

    password_input.set(access_message)

root.bind("<Return>",modified)
"""

def clicked():
    given_text = password_entry.get()
    access_message = None
    if given_text == "password":
        access_message = "Password correct! Access granted"
    else:
        access_message = "Incorrect password correct. Try again."

    password_input.set(access_message)

submit_button = tkinter.Button(root,text="Submit",command=clicked)
submit_button.pack()

root.mainloop()
