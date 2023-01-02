"""Test bot based pre-game setup functions"""
from battle_ship.start_game.sim.sim_pre_game import Sim_Start_Game
from battle_ship.player import Player
import time


def test_pre_game():
    seed = time.time()
    player1 = Player.create()
    start = Sim_Start_Game()
    start.pre_game(player1, seed)
    print()
    print(player1.get_own_board())
