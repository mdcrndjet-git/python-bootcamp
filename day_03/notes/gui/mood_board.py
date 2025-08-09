import tkinter

root = tkinter.Tk()
root.title("Mood Board")
root.geometry("250x250")

font = ("Terminal", 14,"bold italic")
fg_color = "white"
bg_color = "green"
width = 10
height = 10
padx = 5
pady = 5

text = ":)Happy"
left_label = tkinter.Label(root, text=text, font=font,
                      fg=fg_color,bg=bg_color,
                      width=width, height=height,
                      padx=padx,pady=pady)
left_label.pack(side="left")

text = ":(Sad"
bg_color = "blue"
right_label = tkinter.Label(root, text=text, font=font,
                      fg=fg_color,bg=bg_color,
                      width=width, height=height,
                      padx=padx,pady=pady)
right_label.pack(side="right")

root.mainloop()
