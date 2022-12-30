from battle_ship.start_game.sim.sim_pre_game import Sim_Start_Game
from battle_ship.start_game.sim.sim_play import Sim_Play_Strat
from battle_ship.player import Player

def test_pick_loc_strat():
    start = Sim_Start_Game()
    player1 = Player.create()
    start.pre_game(player1)
    player2 = Player.create()
    start.pre_game(player2)

    print('\n')
    play = Sim_Play_Strat()
    play.pick_loc_strat(player1, player2, 2)
