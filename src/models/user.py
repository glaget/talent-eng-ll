class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

    def create_in_database(self):
        print("User created in database")
        return True

    def remove_from_database(self):
        print("User removed from database")
        return True
