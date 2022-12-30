from battle_ship.player import Player
from battle_ship.config import Config
from battle_ship.set_game import Player_Action
import pytest


def test_ship_placement():
    player1 = Player.create()
    action = Player_Action()
    action.ship_placement(player1, 'U', (0,0), 'RIGHT')
    new_board = Config.board
    new_board[0, :3] = player1.ships['U'].get_indicator()
    comparison = player1.get_own_board() == new_board
    assert comparison.all() == True
    print(player1.get_ships())
    print(player1.get_own_board())
    with pytest.raises(KeyError):
        assert action.ship_placement(player1, 'B', (2, 2), 'SIDE') == 'Invalid'
    with pytest.raises(KeyError):
        assert action.ship_placement(player1, 'Z', (2, 2), 'RIGHT') == 'Invalid'
