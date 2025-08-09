import tkinter

root = tkinter.Tk()
root.title("Entry Demo")
root.geometry("250x250")

entry = tkinter.Entry(root)
entry.pack()

def show_input(event):
    print("Enter pressed")

root.bind("<Return>",show_input)
root.mainloop()
