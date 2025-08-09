import tkinter

root = tkinter.Tk()

left_frame = tkinter.Frame(root,bg="lightblue")
left_frame.pack(side="left")

right_frame = tkinter.Frame(root,bg="lightgreen")
right_frame.pack(side="right")

root.mainloop()
