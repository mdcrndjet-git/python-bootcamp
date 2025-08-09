import tkinter
from tkinter import messagebox

root = tkinter.Tk()

response = messagebox.askyesno("Ask Yes/No","Do you want to continue?")
messagebox.showinfo("Response",response)

root.mainloop()