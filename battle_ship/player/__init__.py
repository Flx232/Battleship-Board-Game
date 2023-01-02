"""Player class, stores info about each player in game"""
from battle_ship.config import Config
from battle_ship.game_pieces import Pieces
import numpy as np


class Player:
    
    @classmethod
    def create(cls):
        """Factory method"""
        return cls()

    def __init__(self):
        """Constructor"""
        self.own_board = np.zeros((Config.size, Config.size))
        self.shoot_board = np.zeros((Config.size, Config.size))
        self.ship_list = [Config.U, Config.B, Config.C, Config.D, Config.S]

    def update_own_board(self, board):
        """updates player's own board"""
        self.own_board = board
        return self.own_board

    def update_shoot_board(self, board):
        """updates player's shooting board"""
        self.shoot_board = board
        return self.shoot_board

    def get_own_board(self):
        """gets player's own board"""
        return self.own_board

    def get_shoot_board(self):
        """gets player's shooting board"""
        return self.shoot_board
    
    def get_ships(self):
        """gets the list of ships"""
        return self.ship_list

    def remove_ship(self, ship: str):
        """removes ship from ship list"""
        try:
            """Check if valid ship"""
            game_piece = Config.ships[ship]
            try:
                """Check if ship not in list"""
                self.ship_list.remove(game_piece)
                return game_piece
            except ValueError:
                return "This piece has already been removed"
        except KeyError:
            return "Invalid Ship"

    def add_ship(self, ship: str):
        """adds ship into ship list"""
        try:
            """Check if valid ship"""
            game_piece = Config.ships[ship]
            if game_piece in self.ship_list:
                """Check if ship already in list"""
                return "This piece has already been added"
            else:
                self.ship_list.append(game_piece)
        except KeyError:
            return "Invalid Ship"

