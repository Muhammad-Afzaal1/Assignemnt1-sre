STUDENT_DISCOUNT = 0.10
STAFF_DISCOUNT = 0.05

EXPRESS_FEE = 250
STANDARD_FEE = 100

DISCOUNT_RATES = {
    "student": STUDENT_DISCOUNT,
    "staff": STAFF_DISCOUNT,
}

DELIVERY_FEES = {
    "express": EXPRESS_FEE,
    "standard": STANDARD_FEE,
}


def validate_items(items):
    """Reject negative prices and quantities."""
    for item in items:
        if item["price"] < 0:
            raise ValueError(
                f"Negative price for {item['name']}"
            )

        if item["qty"] < 0:
            raise ValueError(
                f"Negative quantity for {item['name']}"
            )


def calculate_subtotal(items):
    """Calculate subtotal before discounts and delivery."""
    subtotal = 0

    for item in items:
        subtotal += item["price"] * item["qty"]

    return subtotal


def calculate_discount(subtotal, customer_type):
    """Calculate the applicable customer discount."""
    rate = DISCOUNT_RATES.get(customer_type, 0)
    return subtotal * rate


def calculate_delivery_fee(delivery):
    """Return the delivery fee."""
    return DELIVERY_FEES.get(delivery, 0)


def order_total(items, customer_type, delivery):
    """Calculate and return the final order total."""
    validate_items(items)

    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal, customer_type)
    delivery_fee = calculate_delivery_fee(delivery)

    return round(subtotal - discount + delivery_fee, 2)


def print_receipt(items, customer_type, delivery):
    """Generate and return the order receipt."""
    amount = order_total(items, customer_type, delivery)

    lines = ["ORDER RECEIPT"]

    for item in items:
        line_total = item["price"] * item["qty"]
        lines.append(
            f"{item['qty']} x {item['name']} = {line_total}"
        )

    lines.append(f"Customer: {customer_type}")
    lines.append(f"Delivery: {delivery}")
    lines.append(f"Total: {amount}")

    return "\n".join(lines)


if __name__ == "__main__":
    sample = [
        {
            "name": "Notebook",
            "category": "book",
            "price": 300,
            "qty": 2,
        },
        {
            "name": "USB Drive",
            "category": "electronics",
            "price": 800,
            "qty": 1,
        },
    ]

    print(print_receipt(sample, "student", "standard"))