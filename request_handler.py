import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from animals import get_all_animals, get_single_animal, create_animal, delete_animal
from animals.request import get_animals_by_location, get_animals_by_status, update_animal
from customers import create_customer, delete_customer, get_all_customers, get_single_customer, update_customer
from customers.request import get_customers_by_email
from employees.request import create_employee, delete_employee, get_all_employees, get_employees_by_location, get_single_employee, update_employee
from locations.request import create_location, delete_location, get_all_locations, get_single_location, update_location



# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.
class HandleRequests(BaseHTTPRequestHandler):
    # Here's a class function
    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        

    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]

        if "?" in resource:

            param = resource.split("?")[1]
            resource =  resource.split("?")[0]
            pair = param.split("=")
            key = pair[0]
            value = pair[1]

            return (resource, key, value)

        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass
            except ValueError:
                pass

        return (resource, id)

    # This is a Docstring it should be at the beginning of all classes and functions
    # It gives a description of the class or function
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        """Handles GET requests to the server
        """
        self._set_headers(200)
        response = {} 

        parsed = self.parse_url(self.path)

        if len(parsed) == 2:
            ( resource, id ) = parsed

            if resource == "animals":
                if id is not None:
                    response = f"{get_single_animal(id)}"
                else:
                    response = f"{get_all_animals()}"
            elif resource == "customers":
                if id is not None:
                    response = f"{get_single_customer(id)}"
                else:
                    response = f"{get_all_customers()}"
            elif resource == "employees":
                if id is not None:
                    response = f"{get_single_employee(id)}"
                else:
                    response = f"{get_all_employees()}"
            elif resource == "locations":
                if id is not None:
                    response = f"{get_single_location(id)}"
                else:
                    response = f"{get_all_locations()}"
            
        elif len(parsed) == 3:
            ( resource, key, value ) = parsed

            if key == "email" and resource == "customers":
                response = get_customers_by_email(value)
            
            if key == "location_id" and resource == "animals":
                response = get_animals_by_location(value)

            if key == "location_id" and resource == "employees":
                response = get_employees_by_location(value)

            if key == "status" and resource == "animals":
                response = get_animals_by_status(value)


        self.wfile.write(response.encode())



    def do_DELETE(self):
    # Set a 204 response code
        self._set_headers(204)

    # Parse the URL
        (resource, id) = self.parse_url(self.path)

    # Delete a single animal from the list
        if resource == "animals":
            delete_animal(id)
        
        if resource == "locations":
            delete_location(id)

        if resource == "employees":
            delete_employee(id)

        if resource == "customers":
            delete_customer(id)
            
    # Encode the new animal and send in response
        self.wfile.write("".encode())


    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new animal
        new_animal = None

        # Add a new animal to the list. Don't worry about
        # the orange squiggle, you'll define the create_animal
        # function next.
        if resource == "animals":
            new_animal = create_animal(post_body)

        new_location = None

        if resource == "locations":
            new_location = create_location(post_body)

        new_employee = None

        if resource == "employees":
            new_employee = create_employee(post_body)

        new_customer = None
        if resource == "customers":
            new_customer = create_customer(post_body)

        # Encode the new animal and send in response
        self.wfile.write(f"{new_animal}".encode())
        self.wfile.write(f"{new_location}".encode())
        self.wfile.write(f"{new_employee}".encode())
        self.wfile.write(f"{new_customer}".encode())


    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

    # Parse the URL
        (resource, id) = self.parse_url(self.path)

        success = False

        if resource == "animals":
            success = update_animal(id, post_body)
    # rest of the elif's

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())


        





# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
