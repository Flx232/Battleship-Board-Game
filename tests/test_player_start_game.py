"""Tests User input base pre-game setup Functions"""
from battle_ship.start_game import Player_Start_Game
from battle_ship.player import Player

def test_pre_game():
    player1 = Player.create()
    start = Player_Start_Game()
    start.pre_game(player1)
    print(player1.get_own_board())
