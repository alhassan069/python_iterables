cart = []


def add_item(item):
    cart.append(item)
    return f"Item {item} added"

def remove_item(item):
    cart.remove(item)
    return f"Item {item} removed"

def remove_last():
    cart.pop()
    return "Removed last item"

def display_items():
    return cart

def display_items_alphabetically():
    return sorted(cart)

def display_items_with_indices():
    return [item for item in cart]


add_item('apples')
add_item('bread')
add_item('milk')
add_item('eggs')
print(display_items())
remove_item('bread')
print(display_items())
remove_last()
print(display_items())
print(display_items_alphabetically())

print(display_items_with_indices())
