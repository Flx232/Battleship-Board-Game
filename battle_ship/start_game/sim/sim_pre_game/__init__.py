from battle_ship.start_game.rand_gen import Rand_Vals
from battle_ship.set_game import Player_Action
from battle_ship.config import Config


class Sim_Start_Game:

    def __get_pos(self, x):
        """Gets a random position"""
        index = Rand_Vals.get_random_index(x)
        return Config.pos_list[index]

    def pre_game(self, player, seed):
        """Complete random setup"""
        action = Player_Action()
        """List of ships to let algo know when to stop (when all ships used)"""
        ships = ['U', 'B', 'C', 'D', 'S']
        counter = seed
        while ships:
            ship = ships.pop()
            pos = self.__get_pos(counter)
            begin_loc = Rand_Vals.get_random_loc(counter)
            can_place = action.ship_placement(player, ship, begin_loc, pos)
            while not can_place:
                counter += 1
                pos = self.__get_pos(counter)
                begin_loc = Rand_Vals.get_random_loc(counter)
                can_place = action.ship_placement(player, ship, begin_loc, pos)
            counter += 1
        return player

