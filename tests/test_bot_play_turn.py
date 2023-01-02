"""Tests turn base bot algorithm"""
from battle_ship.start_game.sim.sim_pre_game import Sim_Start_Game
from battle_ship.start_game.sim.sim_play import Bot_Player_Info
from battle_ship.player import Player
import numpy as np
import time


def test_pick_loc_strat():
    """Calls caller function in Bot_Player_Info"""
    seed = time.time()
    start = Sim_Start_Game()
    player1 = Bot_Player_Info.create()
    start.pre_game(player1, seed)
    player2 = Bot_Player_Info.create()
    start.pre_game(player2, seed)

    temp = 0
    turn = 1
    print('\n')
    while len(player1.get_ship_sunk_list()) != 5:
        print(f'turn: {turn}')
        player1.pick_loc_strat(player2, seed)
        if temp < len(player1.get_ship_sunk_list()):
            temp = len(player1.get_ship_sunk_list())
        print(player1.get_shoot_board())
        print(player1.get_ship_sunk_list(), '\n')
        seed += 1
        turn += 1
    print("Number of Misses: ", np.count_nonzero(player1.get_shoot_board() == 2))
