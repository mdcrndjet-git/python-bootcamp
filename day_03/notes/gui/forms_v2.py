import tkinter
import json

class Application(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Class Structure")
        self.geometry("300x400")
        self.name = tkinter.StringVar()
        self.age = tkinter.StringVar()
        self.radio_var = tkinter.StringVar(value="Light")
        self.check_value = tkinter.BooleanVar()
        self.slider_value = tkinter.IntVar(value=0)
        self.create_widgets()

    def create_widgets(self):
        name_label = tkinter.Label(self, text="Name")
        name_label.pack()

        name_entry = tkinter.Entry(self,textvariable=self.name)
        name_entry.pack()

        age_label = tkinter.Label(self, text="Age")
        age_label.pack()

        age_entry = tkinter.Entry(self,textvariable=self.age)
        age_entry.pack()

        theme_label = tkinter.Label(self, text="Theme: ")
        theme_label.pack()

        #self.radio_var = tkinter.StringVar(value="Option A")
        radio1 = tkinter.Radiobutton(
            self, text="Light", variable=self.radio_var, value="Light")
        radio1.pack()

        radio2 = tkinter.Radiobutton(
            self, text="Dark", variable=self.radio_var, value="Dark")
        radio2.pack()

        #self.check_value = tkinter.BooleanVar()
        checkbox = tkinter.Checkbutton(
            self,
            text="Subscribe",
            variable=self.check_value
        )
        checkbox.pack()

        rate_label = tkinter.Label(self, text="Rate: ")
        rate_label.pack()

        #slider_value = tkinter.IntVar(value=0)
        slider = tkinter.Scale(
            self,
            from_=0,
            to=100,
            orient="horizontal",
            variable=self.slider_value
        )
        slider.pack()

        button = tkinter.Button(self, text="Submit", command=self.save_to_file)
        button.pack()

    def save_to_file(self):
        tmp_data =  {
                "name":self.name.get(),
                "age":self.age.get(),
                "theme":self.radio_var.get(),
                "subscribe":self.check_value.get(),
                "rate":self.slider_value.get()
            }
        filepath = "C:\\Users\\User\\PycharmProjects\\python-bootcamp\\day_03\\notes\\gui"
        outputfile = filepath +"\\user.json"
        #inventory_file = filepath +"\\inventory.json"
        with open(outputfile, "w") as file:
            json.dump(tmp_data, file)

app = Application()
app.mainloop()
