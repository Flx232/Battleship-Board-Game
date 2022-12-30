from battle_ship.start_game import Player_Start_Game
from battle_ship.player import Player
from battle_ship.start_game.sim.sim_play import Bot_Player_Info
from battle_ship.start_game.sim.sim_pre_game import Sim_Start_Game


def main():
    player1 = Player.create()
    start_player = Player_Start_Game()
    start_player.pre_game(player1)
    player2 = Bot_Player_Info.create()
    seed = 2
    temp = 0
    print('\n')

if __name__ == "__main__":
    main()
