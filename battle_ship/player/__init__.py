from battle_ship.config import Config
from battle_ship.game_pieces import Pieces
import numpy as np


class Player:
    U, B, C = Pieces.create(5, 3), Pieces.create(6, 3), Pieces.create(7, 5)
    D, S = Pieces.create(8, 4), Pieces.create(9, 2)
    ships = {'U':U, 'B':B, 'C':C, 'D':D, 'S':S}

    @classmethod
    def create(cls):
        return cls()

    def __init__(self):
        self.own_board = np.zeros((Config.size, Config.size))
        self.shoot_board = np.zeros((Config.size, Config.size))
        self.ship_list = [self.U, self.B, self.C, self.D, self.S]

    def update_own_board(self, board):
        self.own_board = board
        return self.own_board

    def update_shoot_board(self, board):
        self.shoot_board = board
        return self.shoot_board

    def get_own_board(self):
        return self.own_board

    def get_shoot_board(self):
        return self.shoot_board
    
    def get_ships(self):
        return self.ship_list

    def remove_ship(self, ship: str):
        try:
            game_piece = self.ships[ship]
            try:
                self.ship_list.remove(game_piece)
                return game_piece
            except ValueError:
                return "This piece has already been removed"
        except KeyError:
            return "Invalid Ship"

    def add_ship(self, ship: str):
        try:
            game_piece = self.ships[ship]
            if game_piece in self.ship_list:
                return "This piece has already been added"
            else:
                self.ship_list.append(game_piece)
        except KeyError:
            return "Invalid Ship"

