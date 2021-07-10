from tkinter import *
from tkinter import ttk

widget_font = 'Helvetica'
widget_text_size = 14
widget_background = 'white'
widget_foreground = 'blue'


class GUI:

    def __init__(self, Title="Python GUI Assessment"):
        self.window = Tk()
        self.window.title(Title)

    def add_frame(self, motherwidget):
        return Frame(motherwidget)

    @staticmethod
    def add_label(motherwidget, text):
        return Label(motherwidget, text=text)

    @staticmethod
    def add_entry(motherwidget, text_var):
        return Entry(motherwidget, textvariable=text_var)

    @staticmethod
    def add_message(motherwidget, text, aspect):
        return Message(motherwidget,text=text, aspect=aspect)

    def add_spinbox(self, motherwidget, start, end, text_var):
        return Spinbox(motherwidget, from_=start, to=end, textvariable=text_var)

    def add_combobox(self, motherwidget, values, text_var):
        combobox_widget = ttk.Combobox(motherwidget, textvariable=text_var)
        combobox_widget['values'] = values
        return combobox_widget

    def button(self, motherwidget, text, command):
        return Button(motherwidget, text=text, command=command, font=(widget_font, widget_text_size),bg=widget_background, fg=widget_foreground)

    def user_input(self, motherwidget, text, text_var):
        # Create Frame to place label and entry widget
        user_input_frame = self.add_frame(motherwidget)
        # Create Label widget
        user_input_label = self.add_label(user_input_frame, text)
        user_input_label.configure(font=(widget_font, widget_text_size),bg=widget_background, fg=widget_foreground)
        user_input_label.grid(row=0, column=0)
        # Create Entry widget
        user_input_entry = self.add_entry(user_input_frame, text_var)
        user_input_entry.grid(row=0, column=1)
        return user_input_frame

    def quantity(self, motherwidget, text, text_var, command):
        # Create Frame to place label and spinbox widget
        quantity_frame = self.add_frame(motherwidget)
        # Create Label widget
        quantity_label = self.add_label(quantity_frame, text)
        quantity_label.configure(font=(widget_font, widget_text_size), bg=widget_background, fg=widget_foreground)
        quantity_label.grid(row=0, column=0)
        # Create Spinbox widget
        quantity_spinbox = self.add_spinbox(quantity_frame, 0, 100000, text_var)
        quantity_spinbox.grid(row=0, column=1)
        quantity_spinbox.bind("<Return>", command)
        return quantity_frame

    def drop_down(self, motherwidget, text, text_var, items):
        # Create Frame to place label and combobox widget
        dd_frame = self.add_frame(motherwidget)
        # Create Label widget
        dd_label = self.add_label(dd_frame, text)
        dd_label.configure(font=(widget_font, widget_text_size), bg=widget_background, fg=widget_foreground)
        dd_label.grid(row=0, column=0)
        # Create Combobox widget
        dd_box = self.add_combobox(dd_frame, items, text_var)
        dd_box.grid(row=0, column=1)
        dd_box.current(0)
        return dd_frame

    def launch_window(self):
        self.window.mainloop()
