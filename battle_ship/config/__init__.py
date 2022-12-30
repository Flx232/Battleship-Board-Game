from enum import Enum
import numpy as np


class Config: 
    size = 10
    board = np.zeros((size, size))
    class Position(Enum):
        LEFT = 1
        RIGHT = 2
        UP = 3
        DOWN = 4
