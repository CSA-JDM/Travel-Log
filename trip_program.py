# Jacob Meadows
# Computer Programming II, 6th Period
# 01 October 2018
import tkinter as tk
from tkinter import ttk


class App(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.config(width=390, height=400)
        self.master.title("Travel")
        super().__init__(self.master, width=390, height=400)
        self.place(x=0, y=0)

        try:
            self.travel_log_txt = open("travel_log.txt", "r")
        except FileNotFoundError:
            self.travel_log_txt = open("travel_log.txt", "w")
            self.travel_log_txt.close()
            self.travel_log_txt = open("travel_log.txt", "r")
        self.travel_log_info = self.travel_log_txt.read()
        self.travel_log_txt.close()

        try:
            self.countries = open("countries.txt", "r").read()
        except FileNotFoundError:
            self.countries = "Country File Not Found"
        self.months = "January February March April May June July August September October November December"

        self.widgets = dict()
        self.widget_init()

    def widget_init(self):
        self.widgets["menu"] = tk.Menu(self)
        self.widgets["file_menu"] = tk.Menu(self.widgets["menu"], tearoff=0)
        self.widgets["file_menu"].add_command(label="Save", command=self.submit_command)
        self.widgets["file_menu"].add_command(label="Exit", command=self.quit)
        self.widgets["help_menu"] = tk.Menu(self.widgets["menu"], tearoff=0)
        self.widgets["help_menu"].add_command(label="About", command=self.about_command)
        self.widgets["menu"].add_cascade(label="File", menu=self.widgets["file_menu"])
        self.widgets["menu"].add_cascade(label="Help", menu=self.widgets["help_menu"])
        self.master.config(menu=self.widgets["menu"])
        self.widgets["countries_label"] = tk.Label(self, text="Country")
        self.widgets["countries_str_var"] = tk.StringVar(value=self.countries.split("\n"))
        self.widgets["countries_listbox"] = tk.Listbox(self, listvariable=self.widgets["countries_str_var"], width=28)
        self.widgets["countries_scrollbar"] = tk.Scrollbar(self, command=self.widgets["countries_listbox"].yview)
        self.widgets["countries_listbox"].config(yscrollcommand=self.widgets["countries_scrollbar"], exportselection=0)
        self.widgets["countries_label"].place(x=10 + self.widgets["countries_listbox"]["width"]*2, y=5)
        self.widgets["countries_listbox"].place(x=10, y=30)
        self.widgets["countries_scrollbar"].place(in_=self.widgets["countries_listbox"], x=165, y=-1.5, relheight=1.025)
        self.widgets["months_label"] = tk.Label(self, text="Month")
        self.widgets["months_spinbox"] = tk.Spinbox(self, values=self.months, state="readonly")
        self.widgets["months_label"].place(x=210 + self.widgets["months_spinbox"]["width"]*2, y=5)
        self.widgets["months_spinbox"].place(x=210, y=30)
        self.widgets["description_label"] = tk.Label(self, text="Description")
        self.widgets["description_label"].place(x=10, y=200)
        self.widgets["description_text"] = tk.Text(self, width=42, wrap="word")
        self.widgets["description_text"].place(x=10, y=230)
        self.widgets["travel_label"] = tk.Label(self, text="Method of Travel")
        self.widgets["travel_combobox"] = tk.ttk.Combobox(self, values="Air Train Car", state="readonly")
        self.widgets["travel_label"].place(x=190 + self.widgets["travel_combobox"]["width"]*2, y=60)
        self.widgets["travel_combobox"].place(x=210, y=90)
        self.widgets["submit_button"] = tk.Button(self, text="Submit", command=self.submit_command)
        self.widgets["submit_button"].place(x=210, y=120)
        self.widgets["clear_button"] = tk.Button(self, text="Clear", command=self.clear_command)
        self.widgets["clear_button"].place(x=210, y=150)

    def submit_command(self):
        if self.widgets["countries_listbox"].curselection() != () and self.widgets["travel_combobox"].get() != "":
            self.travel_log_txt = open("travel_log.txt", "w")
            self.travel_log_txt.write(self.travel_log_info +
                                      "Country: " + self.widgets["countries_listbox"].get(self.widgets["countries_listbox"].curselection()[0]) + ", " +
                                      "Month: " + self.widgets["months_spinbox"].get() + ", " +
                                      "Method of Travel: " + self.widgets["travel_combobox"].get() + ", " +
                                      "Description: " + self.widgets["description_text"].get(1.0, "end"))
            self.travel_log_txt.close()

    def clear_command(self):
        for widget in self.winfo_children():
            widget.place_forget()
        self.children.clear()
        self.widgets = dict()
        self.widget_init()

    def about_command(self):
        self.widgets["about_toplevel"] = tk.Toplevel(self)
        self.widgets["about_toplevel"].title("About")
        self.widgets["about_message"] = tk.Message(self.widgets["about_toplevel"], width=200,
                                                   text="A short program that logs inputted data from the user based on"
                                                        " the survey and any information given in the description.")
        self.widgets["about_message"].pack()


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
