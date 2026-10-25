"""SREE practical starter: deliberately untidy legacy order calculator.
Do not use this file for real payments. All prices are in PKR.
"""

def order_total(items, customer_type, delivery):
    total = 0
    for item in items:
        if item['category'] == 'book':
            total = total + item['price'] * item['qty']
        elif item['category'] == 'electronics':
            total = total + item['price'] * item['qty']
        else:
            total = total + item['price'] * item['qty']
    if customer_type == 'student':
        total = total - (total * 0.1)
    elif customer_type == 'staff':
        total = total - (total * 0.05)
    if delivery == 'express':
        total = total + 250
    elif delivery == 'standard':
        total = total + 100
    return round(total, 2)


def print_receipt(items, customer_type, delivery):
    amount = order_total(items, customer_type, delivery)
    result = 'ORDER RECEIPT\n'
    for item in items:
        result += str(item['qty']) + ' x ' + item['name'] + ' = ' + str(item['price'] * item['qty']) + '\n'
    result += 'Customer: ' + customer_type + '\n'
    result += 'Delivery: ' + delivery + '\n'
    result += 'Total: ' + str(amount)
    return result


if __name__ == '__main__':
    sample = [
        {'name': 'Notebook', 'category': 'book', 'price': 300, 'qty': 2},
        {'name': 'USB Drive', 'category': 'electronics', 'price': 800, 'qty': 1},
    ]
    print(print_receipt(sample, 'student', 'standard'))
