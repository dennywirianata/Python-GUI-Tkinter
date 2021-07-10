from Analysis import *
from gui_lib import *


# Functions
def swap_value(msg, a, b):
    try:
        a_val = int(a.get())
        b_val = int(b.get())
        text = swap_func(a_val, b_val)
        msg.configure(text=text, fg=widget_foreground)
    except ValueError:
        msg.configure(text="Input is not a valid number", fg='red')

def calculate_price(msg, item_price, item, qty):
    try:
        qty_val = int(qty.get())
        if qty_val < 0:
            msg.configure(text="Quantity cannot be less than 0.", fg='red')
        else:
            text = lookup_func(item_price, item, qty_val)
            msg.configure(text=text, fg=widget_foreground)
    except ValueError:
        msg.configure(text="Input is not a valid integer number", fg='red')


# Main Script
if __name__ == "__main__":

    # Create UI window
    UI = GUI()
    window = UI.window
    window.resizable(False, False)

    # Divide UI window to left and right side
    left_frame = UI.add_frame(window)
    left_frame.grid(row=0, column=0, sticky=NSEW)
    left_frame.configure(bg=widget_background)
    right_frame = UI.add_frame(window)
    right_frame.grid(row=0, column=1, sticky=NSEW)
    right_frame.configure(bg=widget_background)

    # Create user numeric input for a and b on left side
    a_var = StringVar(window)
    b_var = StringVar(window)
    input_a = UI.user_input(left_frame, 'Key in value for a: ', a_var)
    input_a.grid(row=0, column=0)
    input_a.configure(bg=widget_background)
    input_b = UI.user_input(left_frame, 'Key in value for b: ', b_var)
    input_b.grid(row=1, column=0)
    input_b.configure(bg=widget_background)

    # Configure Swap button and output message on the left side
    swap_frame = UI.add_frame(left_frame)
    swap_frame.grid(row=2, column=0, sticky=NSEW)
    swap_frame.configure(bg=widget_background)
    swap_msg = GUI.add_message(swap_frame, text='', aspect=700)
    swap_msg.configure(fg=widget_foreground, bg=widget_background, font=(widget_font, widget_text_size))
    swap_button = UI.button(swap_frame, 'Swap', lambda: swap_value(swap_msg, a_var, b_var))
    swap_button.grid(row=0, column=0, sticky=SW, padx=10,pady=10)
    swap_msg.grid(row=0, column=1, pady=1)
    swap_button.configure(bg=widget_background)

    # Create Fruits list Dropdown box on right side
    fruit_price = {
        'Apple': 1.30,
        'Orange': 1.00,
        'Pear': 0.80,
        'Grape': 2.20,
        'Kiwi': 1.70
    }
    fruit = StringVar(window)
    dropdown_fruits = UI.drop_down(right_frame, 'Select Fruit: ', fruit, tuple(fruit_price.keys()))
    dropdown_fruits.grid(row=0, column=0)
    dropdown_fruits.configure(bg=widget_background)

    # Configure Quantity entry and output price message on right side
    qty = StringVar(window)
    price_msg = GUI.add_message(right_frame, text='', aspect=700)
    price_msg.configure(fg=widget_foreground, bg=widget_background, font=(widget_font, widget_text_size))
    price_msg.grid(row=2, column=0, sticky=EW, padx=5, pady=5)
    quantity_input = UI.quantity(right_frame, 'Quantity', qty, lambda x: calculate_price(price_msg, fruit_price, fruit.get(), qty))
    quantity_input.grid(row=1, column=0)
    quantity_input.configure(bg=widget_background)

    # Launch UI Window
    UI.launch_window()
