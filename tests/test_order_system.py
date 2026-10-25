import pytest

import legacy_order_system as legacy
import order_system as new

NOTEBOOK = {
    "name": "Notebook",
    "category": "book",
    "price": 300,
    "qty": 2,
}

USB = {
    "name": "USB Drive",
    "category": "electronics",
    "price": 800,
    "qty": 1,
}


# Test 1–5: Compare original and refactored totals
@pytest.mark.parametrize(
    "items, customer, delivery, expected",
    [
        ([NOTEBOOK], "regular", "none", 600.00),
        ([NOTEBOOK, USB], "student", "standard", 1360.00),
        ([USB], "staff", "express", 1010.00),
        ([NOTEBOOK], "regular", "standard", 700.00),
        ([NOTEBOOK], "regular", "express", 850.00),
    ],
)
def test_refactored_matches_legacy(
    items, customer, delivery, expected
):
    assert legacy.order_total(
        items, customer, delivery
    ) == expected

    assert new.order_total(
        items, customer, delivery
    ) == expected


# Test 6: Receipt remains unchanged
def test_receipt_text_unchanged():
    items = [NOTEBOOK, USB]

    assert new.print_receipt(
        items, "student", "standard"
    ) == legacy.print_receipt(
        items, "student", "standard"
    )


# Test 7: Negative price must raise ValueError
def test_negative_price_raises_value_error():
    item = {
        "name": "Pen",
        "category": "other",
        "price": -50,
        "qty": 1,
    }

    with pytest.raises(ValueError):
        new.order_total([item], "regular", "none")


# Test 8: Negative quantity must raise ValueError
def test_negative_quantity_raises_value_error():
    item = {
        "name": "Pen",
        "category": "other",
        "price": 50,
        "qty": -1,
    }

    with pytest.raises(ValueError):
        new.order_total([item], "regular", "none")