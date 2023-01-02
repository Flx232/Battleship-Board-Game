"""Tests player class"""
from battle_ship.game_pieces import Pieces
from battle_ship.player import Player

def test_init_player():
    player1 = Player.create()
    assert isinstance(player1, Player), "Is not a Player Instance"
    print(player1.get_own_board())
    game_piece = player1.remove_ship('U') 
    assert isinstance(game_piece, Pieces), "Is not a Piece Instance"
    assert game_piece not in player1.get_ships()
    print(player1.get_ships())
    player1.add_ship('U')
    print(game_piece)
    assert game_piece in player1.get_ships()
    print(player1.get_ships())

