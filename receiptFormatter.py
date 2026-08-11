def receipt_formatter(name,quantity,price):
    if quantity == 0 or quantity <0 :
        return "Invalid Quantity"
    if price < 0 :
        return "Invalid price"
    subtotal = quantity * price
    tax = 7.5/100 * subtotal
    total = subtotal + tax
    return f"customer - {name} ,subtotal .{subtotal}, Tax {tax}, total {total}"
print(receipt_formatter("joel",100,20))
