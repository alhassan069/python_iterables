
products = ["Laptop", "Mouse","Keyboard", "Monitor"]
prices = [999.99, 25.50, 75.00, 299.99]
quantities = [15, 20, 15, 8]

low_stock = []

product_catalogue = {}


for (product, price, quantity) in zip(products,prices,quantities):
    product_dict = {
        'price': price,
        'quantity' : quantity,
        'total' : price * quantity,
    }
    product_catalogue[product] = product_dict
    if quantity < 10:
        low_stock.append(product)

print('Product Catalogue', product_catalogue)
print('Low Stock', low_stock)
