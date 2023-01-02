"""Custom Out Of Bounds Exception"""


class OutOfBounds(Exception):
    def __init__(self, message = 'This Value is Out of Bounds '):
        """custom exception for board game"""
        self.message = message
        super().__init__(self.message)

