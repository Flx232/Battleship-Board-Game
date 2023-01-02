"""Tests get_cell operation"""
from battle_ship.operations import Operations
from battle_ship.player import Player


def test_get_cell():
    player1 = Player.create()
    assert isinstance(Operations.get_cell(player1.get_own_board(), (0,0)), int)
