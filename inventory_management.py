inventory = {
    "apples": {"price": 1.50, "quantity": 100},
    "bananas": {"price": 0.75, "quantity": 150},
    "oranges": {"price": 2.00, "quantity": 80}
}

# Add a New Product
# Add a new product to the inventory with its price and quantity.

# Update Product Price
# Update the price of an existing product (e.g., change the price of "bananas").

# Sell 25 Apples
# Simulate the sale of 25 apples by updating the quantity accordingly.

# Calculate Total Inventory Value
# Compute the total value of the inventory using the formula:
# total = sum(price × quantity for all products)

# Find Low Stock Products
# Identify and print all products whose quantity is below 100.



def add_product(name:str, price:float, quantity:int):
    inventory[name] = {"price": price, "quantity": quantity}


def update_price(name: str, price:float):
    inventory[name]["price"] = price

def sale(name:str, quantity_sold:int):
    inventory[name]["quantity"] -= quantity_sold

def total_inventory_value():
    total = 0

    for key, value in inventory.items():
        total = total + (inventory[key]["price"] * inventory[key]["quantity"])

    return total

def low_stock_products():
    for key, value in inventory.items():
        if  inventory[key]["quantity"] < 100:
            print(key)


add_product("Gooseberry", 1.25, 120)

print(inventory)

update_price("apples", 1.25)

print(inventory)

sale("apples",25)

print(inventory)

print(total_inventory_value())

low_stock_products()
