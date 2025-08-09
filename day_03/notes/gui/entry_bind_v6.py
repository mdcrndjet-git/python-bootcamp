import tkinter

root = tkinter.Tk()
root.title("Entry Demo")
root.geometry("250x250")

entry = tkinter.Entry(root)
entry.pack()

user_input = tkinter.StringVar(value="Enter any input")
label = tkinter.Label(root, textvariable=user_input)
label.pack()

def show_input(event):
    given_text = entry.get()
    user_input.set(given_text)

root.bind("<Return>",show_input)
root.mainloop()
