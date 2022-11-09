class Product:
    def __init__(self, name, quantity, tags={}):
        self.name = name
        self.quantity = quantity
        self.tags = tags

    def __str__(self):
        tags_as_strings = {str(t) for t in self.tags}
        return (
            f"Product: name={self.name}, quantity={self.quantity}, "
            f"tags={''.join(tags_as_strings)}"
        )

    def create_in_database(self, db):
        print(f"Created a {str(self)} in db {db}")

    def remove_from_database(self, db):
        print(f"Removed a {str(self)} from db {db}")
