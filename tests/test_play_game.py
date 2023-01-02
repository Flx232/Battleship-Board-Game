"""Tests Playing class"""
from battle_ship.start_game import Player_Start_Game, Playing
from battle_ship.start_game.sim.sim_pre_game import Sim_Start_Game
from battle_ship.start_game.sim.sim_play import Bot_Player_Info


def print_sinks(temp, player):
    """Prints the shoot board and ship list when ship gets sunk"""
    if temp < len(player.get_ship_sunk_list()):
        temp = len(player.get_ship_sunk_list())
        print(player1.get_shoot_board())
        print(player1.get_ship_list(), '\n')
    return temp

def test_play_game():
    player1 = Playing.create()
    player_start = Player_Start_Game()
    player_start.pre_game(player1)

    bot_start = Sim_Start_Game()
    bot = Bot_Player_Info.create()
    bot_start.pre_game(bot)
    
    seed = 3
    player_temp, bot_temp = 0, 0
    print('\n')
    while len(player1.get_ship_sunk_list()) != 5 or len(player2.get_ship_sunk_list()) != 5:
        print('Player1\'s Turn!')
        player1.play_game(player2)
        player_temp = print_sinks(player_temp, player1)
        
        print('Bot\'s Turn!')
        player2.pick_loc_strat(bot, seed)
        bot_temp = print_sinks(bot_temp, bot)
        seed += 1

