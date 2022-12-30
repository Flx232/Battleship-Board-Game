from battle_ship.config import Config
from battle_ship.player import Player
from battle_ship.operations import Operations
from battle_ship.exceptions import OutOfBounds
import numpy as np


class Player_Action:
    def ship_placement(self, player, ship, begin_loc: tuple, pos):
        try:
            game_piece = player.ships[ship]
            if game_piece not in player.ship_list:
                return 'This piece has already been placed'
        except KeyError:
            print('Invalid Ship')
            raise
        enum_pos = Operations.get_enum_pos(pos)
        end_loc = (0,0)
        try:
            if enum_pos == Config.Position.LEFT:
                begin_loc = Operations.addition(begin_loc, (1, 1))
                end_loc = begin_loc
                begin_loc = Operations.subtraction(end_loc, (1, game_piece.get_specifier()))

            elif enum_pos == Config.Position.RIGHT:
                end_loc = Operations.addition(begin_loc, (1, game_piece.get_specifier()))
                
            elif enum_pos == Config.Position.UP:
                begin_loc = Operations.addition(begin_loc, (1, 1))
                end_loc = begin_loc
                begin_loc = Operations.subtraction(end_loc, (game_piece.get_specifier(), 1))
                
            else:
                end_loc = Operations.addition(begin_loc, (1, game_piece.get_specifier()))
        except OutOfBounds:
            print(f'End_loc is out of bounds! end_loc: {end_loc}')
            return False
        
        if self.__is_collision(player.get_own_board(), begin_loc, end_loc):
            player = self.__place_ship(player, ship, begin_loc, end_loc)
            print(player.get_own_board())
            return True
        return False

    def __is_collision(self, board, begin_loc: tuple, end_loc:tuple):
        bx, by = begin_loc
        rx, ry = end_loc
        for row in range(bx, rx, 1):
            for col in range(by, ry, 1):
                if board[row][col] != 0:
                    print(f'There is a collision! Point of collision: {(row,col)}')
                    return False
        return True

    def __place_ship(self, player, ship, begin_loc: tuple, end_loc: tuple):
        game_piece = player.remove_ship(ship)
        bx, by = begin_loc
        rx, ry = end_loc
        board = player.get_own_board()
        board[bx:rx, by:ry] = game_piece.get_indicator()
        player.update_own_board(board) 
        return player
    
    def remove_ship(self, player, ship: str):
        board = player.get_own_board()
        player.add_ship(ship)
        game_piece = player.get_ships()[-1]
        coords = np.where(board == game_piece.get_indicator())
        bx, by = coords[0][0], coords[1][0]
        rx, ry = coords[0][-1]+1, coords[1][-1]+1
        board[bx:rx, by:ry] = 0
        player.update_own_board(board)
        print(player.get_own_board())
        return player

    def is_hit(self, player, target: tuple):
        return Operations.get_cell(player.get_own_board(), target) != 0

