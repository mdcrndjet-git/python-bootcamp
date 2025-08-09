import tkinter

root = tkinter.Tk()
root.title("Entry Demo")
root.geometry("250x250")

text = tkinter.StringVar(root, value="Hello")
label = tkinter.Label(root,textvariable=text)
label.pack()

root.mainloop()
