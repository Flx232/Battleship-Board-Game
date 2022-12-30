class Pieces:

    @classmethod
    def create(cls, indicator, specifier):
        return cls(indicator, specifier)

    def __init__(self, indicator, specifier):
        self._indicator = indicator
        self._specifier = specifier

    def __repr__(self):
        return f'{self.get_indicator()},{self.get_specifier()}'

    def get_indicator(self):
        return self._indicator

    def get_specifier(self):
        return self._specifier

    def equals(self, pieces):
        if self.get_indicator() == pieces.get_indicator() and\
                self.get_specifier() == pieces.get_specifier():
                    return True
        return False

