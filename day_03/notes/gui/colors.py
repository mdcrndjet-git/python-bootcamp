import tkinter

root = tkinter.Tk()
root.title("Python Haiku")
root.geometry("250x100")

text = "Hello World"
font = ("Terminal", 14,"bold italic")
fg_color = "white"
bg_color = "blue"

label = tkinter.Label(root, text=text, font=font, fg=fg_color,bg=bg_color)
label.pack()

root.mainloop()
