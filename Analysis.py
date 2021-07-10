def swap_func(a, b):
    msg = f"Before: a = {a} and b = {b}\n"
    a = a + b
    b = a - b
    a = a - b
    msg = msg + f"After:    a = {a} and b = {b}"
    return msg


def lookup_func(item_price, item, qty):
    total_price = item_price[item] * qty
    msg = f'Total Price = ${total_price:.2f}'
    return msg



