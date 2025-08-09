import tkinter

root = tkinter.Tk()
root.title("Python Haiku")
root.geometry("500x500")

font = ("Terminal", 14,"bold italic")
fg_color = "white"
bg_color = "blue"
width = 10
height = 10
padx = 5
pady = 25

text = "Left"
left_label = tkinter.Label(root, text=text, font=font,
                      fg=fg_color,bg=bg_color,
                      padx=padx,pady=pady)
left_label.pack(side="left")

text = "Right"
bg_color = "green"
right_label = tkinter.Label(root, text=text, font=font,
                      fg=fg_color,bg=bg_color,
                      padx=padx,pady=pady)
right_label.pack(side="right")

root.mainloop()
