import tkinter

root = tkinter.Tk()
root.title("Python Haiku")
root.geometry("250x100")

text = "Hello World"
font = ("Arial", 14,"bold italic")
label = tkinter.Label(root, text=text, font=font)
label.pack()

root.mainloop()
