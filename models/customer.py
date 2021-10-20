class Customer():

    def __init__(self, id, name, address, email = "", password = ""):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password



new_customer = Customer(5, "Grant Beaton","173 Chesire Rd" ,"grant@beaton.com", "grant")