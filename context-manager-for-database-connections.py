"""
Custom context manager for managing database connections
"""


class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None

    def __enter__(self):
        # Setup resource
        print(f"Connecting to database: {self.connection_string}")
        self.connection = {"connection": "established"}  # Simulate connection
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        # Cleanup resource
        if self.connection:
            print("Closing database connection")
            self.connection = None
        if exc_type is not None:
            # Handle any errors that occurred
            print(f"An error occurred: {exc_value}")
            return False  # Propagate the exception


# Usage
with DatabaseConnection("postgresql://localhost:5432/db") as conn:
    # Do something with connection
    print("Performing database operations")
