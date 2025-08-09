import tkinter

root = tkinter.Tk()
root.title("Example Window Application")
root.geometry("1200x400")
label = tkinter.Label(root, text="Hello World")
label.pack()

new_label = tkinter.Label(root, text="Another one")
new_label.pack()

message = """
Hello 
World
"""
multi_line_label = tkinter.Label(root, text=message)
multi_line_label.pack()

root.mainloop()
