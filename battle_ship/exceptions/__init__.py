class OutOfBounds(Exception):
    def __init__(self, message = 'This Value is Out of Bounds '):
        self.message = message
        super().__init__(self.message)

