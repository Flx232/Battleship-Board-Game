from battle_ship.start_game.rand_gen import Rand_Vals
from battle_ship.set_game import Player_Action
from battle_ship.start_game.sim.sim_play import Color_Cell
from battle_ship.start_game.marker import Marker
from battle_ship.game_pieces import Pieces
from battle_ship.player import Player


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

class Get_Coord:
    @staticmethod
    def coord(self):
        row = int(input('Enter the row: \n'))
        col = int(input('Enter the column: \n'))
        return (row, col)

class Player_Start_Game:
    ship_list = ['U', 'B', 'C', 'D', 'S']
    pos_list = ('LEFT', 'RIGHT', 'DOWN', 'UP')
    used_ship_list = []

    def __place_ship(self, player, action):      
        ships = ', '.join(str(x) for x in self.ship_list)
        ship = input(f'Pick a ship ({ships}): \n').upper()
        pos = input(f'Enter an orientation {self.pos_list}: \n').upper()
        loc = Get_Coord.coord()
        can_place = action.ship_placement(player, ship, loc, pos)
        while not can_place:
            pos = input(f'Enter an orientation {self.pos_list}: \n').upper()
            loc = Get_Coord.coord()
            can_place = action.ship_placement(player, ship, begin_loc, pos)
        self.ship_list.remove(ship)
        self.used_ship_list.append(ship)

    def __remove_ship(self, player, action):
        ships = ','.join(str(x) for x in self.used_ship_list)
        ship = input(f'Pick a ship ({ships}): \n').upper()
        can_remove = action.remove_ship(player, ship)
        while not can_remove:            
            ships = ','.join(str(x) for x in self.used_ship_list)
            ship = input(f'Pick a ship ({ships}): \n').upper()
            can_remove = action.remove_ship(player, ship)
        self.used_ship_list.remove(ship)
        self.ship_list.append(ship)

    def pre_game(self, player):
        action = Player_Action()
        while self.ship_list:
            decider = input('PLACE or REMOVE\n').upper()
            if decider == 'PLACE':
                self.__place_ship(player, action)
            elif decider == 'REMOVE':
                self.__remove_ship(player, action)
            else:
                print('Invalid Input!')
        return player

class Playing(Player):
    ship_sunk_list = []
    
    @classmethod
    def create(cls):
        return cls()

    def __init__(self):
        super().__init__()
        self.ship_part_dict = {}

    def get_ship_part_dict(self):
        return self.ship_part_dict

    def set_ship_part_dict(self, new_dict):
        self.ship_part_dict = new_dict

    def get_ship_sunk_list(self):
        return self.ship_sunk_list
    
    def __mark_cell(self, target_loc, def_player, action):
        ship_ident = None
        if action.is_hit(def_player, target_loc):
            ship_ident = Operations.get_cell(def_player.get_own_board(), target_loc)
            Marker.shoot_board_mark(self, target_loc, 1)
            Marker.own_board_mark(def_player, target_loc, 1)
        else:
            Marker.shoot_board_mark(self, target_loc, 2)
            Marker.own_board_mark(def_player, target_loc, 2)
        return ship_ident

    def __is_ship_sunk(self, ship_part_dict):
        ship_names = {'U':'Submarine', 'C':'Carrier', 'D':'Destroyer', 'B':'Battleship', 'S':'Cruiser'}
        game_piece_list = {}
        for key, val in ship_part_dict.items():
            game_piece = Pieces.create(key, val)
            game_piece_list[key] = game_piece
        for ship_key in Player.ships:
            for piece_key in game_pieces_list:
                if game_piece_list[piece_key].equals(Player.ships[ship_key]):
                    self.ship_sunk_list.append(ship_key)
                    ship_name = ship_names[self.ship_sunk_list[-1]]
                    ident_to_delete = piece_key
                    del ship_part_dict[ident_to_delete]
                    print(f'You sunk my {ship_name}!')
                    print(self.get_shoot_board())
        return ship_part_dict

    def play_game(self, def_player):
        action = Player_Action()
        temp_dict = self.__is_ship_sunk(self.get_ship_part_dict())
        loc = Get_Coord.coord()
        self.__mark_cell(loc, def_player, action)
        if ship_ident:
            self.point_of_contact = self.target_loc
            self.ship_found = True
            if ship_ident in self.ship_part_dict:
                temp_dict[ship_ident] += 1
            else:
                temp_dict[ship_ident] = 1
        self.set_ship_part_dict(temp_dict)
        return def_player
