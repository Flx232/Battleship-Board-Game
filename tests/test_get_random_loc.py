from battle_ship.start_game.rand_gen import Rand_Vals

def test_get_random_loc():
    assert isinstance(Rand_Vals.get_random_loc(1), tuple)
