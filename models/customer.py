from customers.request import CUSTOMERS


class Customer():
    def __init__(self, id, name):
        self.id = id
        self.name = name


new_customer = Customer(5, "Grant Beaton ")