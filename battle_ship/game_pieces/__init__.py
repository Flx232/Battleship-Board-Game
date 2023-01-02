"""Pieces class that stores information of each piece in the Game"""
class Pieces:

    @classmethod
    def create(cls, indicator, specifier):
        """Factory Method"""
        return cls(indicator, specifier)

    def __init__(self, indicator, specifier):
        """Constructor"""
        self._indicator = indicator
        self._specifier = specifier

    def __repr__(self):
        """returns description of piece"""
        return f'{self.get_indicator()},{self.get_specifier()}'

    def get_indicator(self):
        """Gets the indication of piece"""
        return self._indicator

    def get_specifier(self):
        """Gets the characteristic of piece"""
        return self._specifier

    def equals(self, pieces):
        """Checks if two pieces are the same"""
        if self.get_indicator() == pieces.get_indicator() and\
                self.get_specifier() == pieces.get_specifier():
                    return True
        return False

