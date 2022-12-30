from battle_ship.start_game.rand_gen import Rand_Vals
from battle_ship.set_game import Player_Action


class Sim_Start_Game:
    def __get_pos(self, x):
        pos = ('LEFT', 'RIGHT', 'DOWN', 'UP')
        index = Rand_Vals.get_random_index(x)
        return pos[index]

    def pre_game(self, player):
        action = Player_Action()
        ships = ['U', 'B', 'C', 'D', 'S']
        counter = 1
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

