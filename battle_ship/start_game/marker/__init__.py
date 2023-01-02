"""Marker Class containing static methods"""


class Marker:
    
    @staticmethod
    def shoot_board_mark(atk_player, target_loc, marker):
        """Mark cell in shooting board"""
        x, y = target_loc
        shoot_board = atk_player.get_shoot_board()
        shoot_board[x][y] = marker
        atk_player.update_shoot_board(shoot_board)

    @staticmethod
    def own_board_mark(def_player, target_loc, marker):
        """Mark cell in own board"""
        x, y = target_loc
        own_board = def_player.get_own_board()
        own_board[x][y] = marker
        def_player.update_own_board(own_board)

