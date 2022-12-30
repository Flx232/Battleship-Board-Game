from battle_ship.start_game.rand_gen import Rand_Vals


class Rand_Loc:
    @staticmethod
    def get_rand_loc(counter, atk_player):
        target_loc = Rand_Vals.get_random_loc(counter)
        x, y = target_loc
        while atk_player.get_shoot_board()[x][y] != 0:
            counter += 1
            target_loc = Rand_Vals.get_random_loc(counter)
            x, y = target_loc
        return target_loc
