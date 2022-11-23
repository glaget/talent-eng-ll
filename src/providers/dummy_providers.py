class DummyDatabase:
    """
    This is a dummy Database provider.
    """

    def __init__(self, path) -> None:
        self.path = path
        self.tables = None
        self.connected = False

    def connect(self):
        if self.connected:
            print("Database connection already established")
            return
        self.tables = {"products": [], "users": []}
        self.connected = True
        print("Database connection established")

    def disconnect(self):
        if not self.connected:
            print("Database connection already dropped")
            return
        self.tables = None
        self.connected = False
        print("Database connection dropped")
