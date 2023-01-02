from enum import Enum
import numpy as np
from battle_ship.game_pieces import Pieces


"""Constant Variables that can be used in any function"""
class Config: 
    U, B, C, D, S = Pieces.create(5, 3), Pieces.create(6, 3), Pieces.create(7, 5),\
            Pieces.create(8, 4), Pieces.create(9, 2)
    ships = {'U':U, 'B':B, 'C':C, 'D':D, 'S':S}
    size = 10
    ship_names = {'U':'Submarine', 'C':'Carrier', 'D':'Destroyer', 'B':'Battleship', 'S':'Cruiser'}
    pos_list = ('LEFT', 'RIGHT', 'DOWN', 'UP')
    class Position(Enum):
        LEFT = 1
        RIGHT = 2
        UP = 3
        DOWN = 4
