import random


class Rand_Vals:
    @staticmethod
    def get_random_loc(x):
        random.seed(x)
        return(random.randint(0, 9), random.randint(0, 9))

    @staticmethod
    def get_random_index(x):
        random.seed(x)
        return(random.randint(0,3))

