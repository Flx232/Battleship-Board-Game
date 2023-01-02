"""Tests function where bot strategically selects cells every turn"""
from battle_ship.start_game.sim.sim_pre_game import Sim_Start_Game
from battle_ship.start_game.sim.sim_play import Sim_Play_Strat
from battle_ship.player import Player
import numpy as np
import time


def test_pick_loc_strat():
    seed = time.time()
    start = Sim_Start_Game()
    player1 = Player.create()
    start.pre_game(player1, seed)
    player2 = Player.create()
    start.pre_game(player2, seed)

    print('\n')
    play = Sim_Play_Strat()
    play.pick_loc_strat(player1, player2, seed)
    print(player1.get_shoot_board())
    print("Number of misses: ", np.count_nonzero(player1.get_shoot_board() == 2))

