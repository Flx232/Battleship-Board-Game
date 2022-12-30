from battle_ship.player import Player
from battle_ship.set_game import Player_Action

def test_is_hit():
    player1 = Player.create()
    action = Player_Action()
    action.ship_placement(player1, 'U', (0,0), 'RIGHT')
    assert action.is_hit(player1, (0,1)) == True
