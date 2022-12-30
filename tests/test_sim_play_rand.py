from battle_ship.start_game.sim.sim_pre_game import Sim_Start_Game
from battle_ship.start_game.sim.sim_play import Sim_Play_Rand
from battle_ship.player import Player

def test_pick_loc_rand():
    start = Sim_Start_Game()
    player1 = Player.create()
    start.pre_game(player1)
    player2 = Player.create()
    start.pre_game(player2)
    
    play = Sim_Play_Rand()
    play.pick_loc_rand(player1, player2)
    print('\n', player2.get_own_board())

