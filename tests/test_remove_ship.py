from battle_ship.set_game import Player_Action
from battle_ship.config import Config
from battle_ship.player import Player


def test_remove_ship():
    player1 = Player.create()
    action = Player_Action()
    action.ship_placement(player1, 'U', (0,0), 'RIGHT')
    action.remove_ship(player1, 'U')
    comparison = Config.board == player1.get_own_board()
    assert comparison.all() == True
