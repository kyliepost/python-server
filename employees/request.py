EMPLOYEES = [
    {
        "name": "Jenna Solis",
        "id": 1
    },
    {
        "name": "Lucas Smith",
        "id": 2
    },
    {
        "name": "William Bax",
        "id": 3
    },
    {
        "name": "Sara Lee",
        "id": 4
    }
]

def get_all_employees():
    return EMPLOYEES


def get_single_employee(id):

    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee