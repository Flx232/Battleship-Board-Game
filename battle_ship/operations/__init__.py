from battle_ship.config import Config
from battle_ship.exceptions import OutOfBounds


class Operations:
    @staticmethod
    def addition(val1: tuple, val2: tuple):
        resultx = val1[0] + val2[0]
        resulty = val1[1] + val2[1]
        if resultx > Config.size-1 or resulty > Config.size-1:
            raise OutOfBounds
        return (resultx, resulty)

    @staticmethod
    def subtraction(val1: tuple, val2: tuple):
        resultx = val1[0] - val2[0]
        resulty = val1[1] - val2[1]
        if resultx < 0 or resulty < 0:
            raise OutOfBounds
        return (resultx, resulty)

    @staticmethod
    def get_cell(board, loc: tuple):
        x, y = loc
        return int(board[x][y])

    @staticmethod
    def get_enum_pos(pos): 
        all_pos = {'LEFT':Config.Position.LEFT, 'RIGHT':Config.Position.RIGHT,\
                'UP':Config.Position.UP, 'DOWN':Config.Position.DOWN} 
        try:
            enum_pos = all_pos[pos]
        except KeyError:
            print('Invalid Orientation')
            raise
        return enum_pos

