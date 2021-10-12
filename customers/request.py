CUSTOMERS = [
    {
        "id": 1,
        "name": "Lisa Mill"
    },
    {
        "id": 2,
        "name": "Reese Parker"
    },
    {
    "id": 3,
    "name": "Matthew Lock"
    },
    {
        "id": 4,
        "name": "Kara Lott"
    },
    {
        "id": 5,
        "name": "Grant Beaton"
    }
]

def get_all_customers():
    return CUSTOMERS


def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    
    return requested_customer


def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id +1
    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer


