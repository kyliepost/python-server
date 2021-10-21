# import employees
import sqlite3
import json
from models import Employee
from models import Location


EMPLOYEES = [
    {
        "name": "Jenna Solis",
        "id": 1,
        "address": "7464 Lookout Dr",
        "location_id": 2
    },
    {
        "name": "Lucas Smith",
        "id": 2,
        "address": "2635 Hill Rd",
        "location_id": 1
    },
    {
        "name": "William Bax",
        "id": 3,
        "address": "366 Mixer Way",
        "location_id": 1
    },
    {
        "name": "Sara Lee",
        "id": 4,
        "address": "3688 Rio Dr",
        "location_id": 2
    }
]

def get_all_employees():
    with sqlite3.connect("./kennel.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            *
        FROM employee a
        """)

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])

            employees.append(employee.__dict__)

    return json.dumps(employees)


def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
        *            
        FROM employee a
        WHERE a.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        employee = Employee(data['id'], data['name'], data['address'], data['location_id'])

        return json.dumps(employee.__dict__)

def create_employee(employee):

    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)
    return employee

def delete_employee(id):

    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index
        
        if employee_index >= 0:
            EMPLOYEES.pop(employee_index)


def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break


def get_employees_by_location(location_id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT *
        FROM employee
        WHERE location_id = ?
        """, (location_id, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
            employees.append(employee.__dict__)
    
    return json.dumps(employees)