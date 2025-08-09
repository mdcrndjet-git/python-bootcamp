import tkinter

root = tkinter.Tk()
root.title("Python Haiku")
root.geometry("250x100")

text = """
Loops within loops,
A silent function returns,
The logic is clear.
"""
label = tkinter.Label(root, text=text)
label.pack()

root.mainloop()
