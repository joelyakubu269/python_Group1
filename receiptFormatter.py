def receipt_formatter(name,quantity,price):
    if quantity == 0 or quantity <0 :
        return "Invalid Quantity"
    if price < 0 :
        return "Invalid price"
    subtotal = quantity * price
    tax = 7.5/100 * subtotal
    total = subtotal + tax
    return f"""Customer: {name}
    Subtotal: {subtotal: .2f}
    Tax: {tax: .2f}
    Total: {total: .2f}"""
print(receipt_formatter("Joel",100,20))
