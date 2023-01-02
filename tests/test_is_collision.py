"""Tests if function raises collision"""
from battle_ship.config import Config
from battle_ship.set_game import Player_Action
from battle_ship.player import Player

def test_is_collision():
    player1 = Player.create()
    action = Player_Action()
    action._Player_Action__place_ship(player1, 'U', (0, 0), (1,3))
    truth_table = action._Player_Action__is_collision(player1.get_own_board(), (0, 0), (1,3))
    assert truth_table == False
