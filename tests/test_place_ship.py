"""Tests place_ship private function"""
from battle_ship.config import Config
from battle_ship.set_game import Player_Action
from battle_ship.player import Player
import numpy as np


def test_place_ship():
    player1 = Player.create()
    action = Player_Action()
    action._Player_Action__place_ship(player1, 'U', (0,0), (1,3))
    new_board = np.zeros((Config.size, Config.size))
    new_board[0, :3] = Config.ships['U'].get_indicator()
    comparison = player1.get_own_board() == new_board
    assert comparison.all() == True
    print(player1.get_ships())

