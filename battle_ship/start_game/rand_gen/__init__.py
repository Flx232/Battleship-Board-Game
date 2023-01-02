"""Random class with static methods"""
import random


class Rand_Vals:
    @staticmethod
    def get_random_loc(x):
        """Gets a random coord"""
        random.seed(x)
        return(random.randint(0, 9), random.randint(0, 9))

    @staticmethod
    def get_random_index(x):
        """Gets a random index"""
        random.seed(x)
        return(random.randint(0,3))

    @staticmethod
    def get_rand_loc(counter, atk_player):
        """Continuously gets random value until the element in cell is 0"""
        target_loc = Rand_Vals.get_random_loc(counter)
        x, y = target_loc
        while atk_player.get_shoot_board()[x][y] != 0:
            counter += 1
            target_loc = Rand_Vals.get_random_loc(counter)
            x, y = target_loc
        return target_loc

