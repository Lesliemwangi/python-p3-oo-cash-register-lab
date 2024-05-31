def reset_last_transaction(func):
    """Decorator to reset the last transaction amount after the method call."""

    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        self.last_transaction_amount = 0
        return result
    return wrapper


def validate_discount(func):
    """Decorator to check if the discount can be applied."""

    def wrapper(self, *args, **kwargs):
        if self.discount <= 0:
            print("There is no discount to apply.")
            return
        return func(self, *args, **kwargs)
    return wrapper


class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction_amount = price * quantity
        self.items.extend([title] * quantity)

    @validate_discount
    def apply_discount(self):
        self.total -= (self.total * self.discount) / 100
        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        self.last_transaction_amount = 0