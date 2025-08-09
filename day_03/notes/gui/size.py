import tkinter

root = tkinter.Tk()
root.title("Python Haiku")
root.geometry("500x500")

text = "Hello World"
font = ("Terminal", 14,"bold italic")
fg_color = "white"
bg_color = "blue"
width = 10
height = 10
padx = 5
pady = 25

label = tkinter.Label(root, text=text, font=font,
                      fg=fg_color,bg=bg_color,
                      width=width, height=height,
                      padx=padx,pady=pady)
label.pack()

root.mainloop()
