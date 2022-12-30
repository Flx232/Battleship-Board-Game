from battle_ship.start_game.sim.sim_pre_game import Sim_Start_Game
from battle_ship.player import Player

def test_pre_game():
    player1 = Player.create()
    start = Sim_Start_Game()
    start.pre_game(player1)
    print()
    print(player1.get_own_board())
