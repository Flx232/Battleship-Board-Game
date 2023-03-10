"""Players are bots, Use algorithm to find ships"""
from battle_ship.set_game import Player_Action
from battle_ship.start_game.marker import Marker
from battle_ship.start_game.rand_gen import Rand_Vals
from battle_ship.operations import Operations
from battle_ship.config import Config
from battle_ship.game_pieces import Pieces
from battle_ship.player import Player
from battle_ship.exceptions import OutOfBounds


class Color_Cell:

    def __mark_cell(self, target_loc, counter, atk_player, def_player):
        """Marks cell that has been hit"""
        action = Player_Action()
        ship_ident = None
        if action.is_hit(def_player, target_loc):
            ship_ident = Operations.get_cell(def_player.get_own_board(), target_loc)
            Marker.shoot_board_mark(atk_player, target_loc, 1)
            Marker.own_board_mark(def_player, target_loc, 1)
        else:
            Marker.shoot_board_mark(atk_player, target_loc, 2)
            Marker.own_board_mark(def_player, target_loc, 2)
        return ship_ident

class Sim_Play_Rand:

    def pick_loc_rand(self, atk_player, def_player, seed):
        """Randomly picks a location every turn"""
        counter = seed
        target_loc = ()
        comparison = def_player.get_own_board() == atk_player.get_shoot_board()
        while not comparison.all():
            target_loc = Rand_Vals.get_rand_loc(counter, atk_player)
            color = Color_Cell()
            color._Color_Cell__mark_cell(target_loc, counter, atk_player, def_player)
            comparison = def_player.get_own_board() == atk_player.get_shoot_board()
            counter += 1

class Sim_Play_Strat:
    ship_sunk_list = []
    ship_part_dict = {}
    target_loc, point_of_contact = (), ()
    ship_ident = None
    ship_found = False
    is_horizontal, is_vertical = False, False

    def __checker(self, seed, enum_pos, dir_list_counter):
        """Moves to adjacent cells of current cell (if in bounds)"""
        if enum_pos == Config.Position.LEFT:
            self.target_loc = Operations.subtraction(self.point_of_contact, (0, 1))
            dir_list_counter = Config.pos_list.index('LEFT')
            self.is_horizontal, self.is_vertical = True, False
        elif enum_pos == Config.Position.RIGHT:
            self.target_loc = Operations.addition(self.point_of_contact, (0, 1))
            dir_list_counter = Config.pos_list.index('RIGHT')
            self.is_horizontal, self.is_vertical = True, False
        elif enum_pos == Config.Position.UP:
            self.target_loc = Operations.subtraction(self.point_of_contact, (1, 0))
            dir_list_counter = Config.pos_list.index('UP')
            self.is_horizontal, self.is_vertical = False, True
        elif enum_pos == Config.Position.DOWN:
            self.target_loc = Operations.addition(self.point_of_contact, (1, 0))
            dir_list_counter = Config.pos_list.index('DOWN')
            self.is_horizontal, self.is_vertical = False, True
        else: 
            self.target_loc = Rand_Vals.get_rand_loc(seed, atk_player)
        return dir_list_counter
    
    def __ship_sunk(self, atk_player):
        """Confirms ship sunked"""
        ship_names = {'U':'Submarine', 'C':'Carrier', 'D':'Destroyer', 'B':'Battleship', 'S':'Cruiser'}
        for key, val in self.ship_part_dict.items():
            game_piece = Pieces.create(key, val)
            ident_to_delete = key
        for key in Config.ships:
            if game_piece.equals(Config.ships[key]):
                self.ship_sunk_list.append(key)
                ship_name = ship_names[self.ship_sunk_list[-1]]
                print(f'You sunk my {ship_name}!')
                del self.ship_part_dict[ident_to_delete]
                print(atk_player.get_shoot_board())

    def pick_loc_strat(self, atk_player, def_player, seed):
        """bot that picks random locations until it hits ship"""
        dir_list_counter, cap = 0, 1
        comparison = def_player.get_own_board() == atk_player.get_shoot_board()
        action = Player_Action()
        while not comparison.all():
            if dir_list_counter > cap:
                self.ship_found = False
                game_piece = Pieces.create(0,0)
                ident_to_delete = 0
                self.__ship_sunk(atk_player)
                dir_list_counter, cap = 0, 1
            if self.ship_found:
                if self.is_vertical:
                    dir_list_counter, cap = 2, 3
                if dir_list_counter >= len(Config.pos_list):
                    enum_pos = None
                else:
                    enum_pos = Operations.get_enum_pos(Config.pos_list[dir_list_counter])
                
                try:
                    dir_list_counter = self.__checker(seed, enum_pos, dir_list_counter)
                except OutOfBounds:
                    dir_list_counter += 1
                    comparison = def_player.get_own_board() == atk_player.get_shoot_board()
                    continue

                if Operations.get_cell(atk_player.get_shoot_board(), self.target_loc) == 1:
                    self.point_of_contact = self.target_loc
                    comparison = def_player.get_own_board() == atk_player.get_shoot_board()
                    continue
                elif Operations.get_cell(atk_player.get_shoot_board(), self.target_loc) == 2:
                    self.target_loc = self.point_of_contact
                    dir_list_counter += 1
                else:
                    temp = self.point_of_contact
            else:
                self.target_loc = Rand_Vals.get_rand_loc(seed, atk_player)
            cell_ident = Operations.get_cell(atk_player.get_shoot_board(), self.target_loc)  
            if cell_ident == 1 or cell_ident == 2:
                continue
            color = Color_Cell()
            ship_ident = color._Color_Cell__mark_cell(self.target_loc, seed, atk_player, def_player)
            if ship_ident:
                self.point_of_contact = self.target_loc
                self.ship_found = True
                if ship_ident in self.ship_part_dict:
                    self.ship_part_dict[ship_ident] += 1
                else:
                    self.ship_part_dict[ship_ident] = 1
            else:
                if self.ship_found:
                    dir_list_counter += 1
            comparison = def_player.get_own_board() == atk_player.get_shoot_board()
            seed += 1
        if self.ship_part_dict: 
            self.__ship_sunk(atk_player)

class Bot_Player_Info(Player):
    ship_sunk_list = []
    ship_part_dict = {}
    target_loc, point_of_contact = (), ()
    ship_ident = None
    ship_found = False
    possible_ship_length = [5, 4, 3, 3, 2]
    is_horizontal, is_vertical = False, False
    dir_list_counter, cap, hit_counter = 0, 1, 0
    
    @classmethod
    def create(cls):
        return cls()

    def __init__(self):
        super().__init__()

    def __checker(self, enum_pos, dir_list_counter):
        """Moves to adj cells of cell where ship was hit"""
        try:
            if enum_pos == Config.Position.LEFT:
                self.target_loc = Operations.subtraction(self.point_of_contact, (0, 1))
                dir_list_counter = Config.pos_list.index('LEFT')
                self.is_horizontal, self.is_vertical = True, False
            elif enum_pos == Config.Position.RIGHT:
                self.target_loc = Operations.addition(self.point_of_contact, (0, 1))
                dir_list_counter = Config.pos_list.index('RIGHT')
                self.is_horizontal, self.is_vertical = True, False
            elif enum_pos == Config.Position.UP:
                self.target_loc = Operations.subtraction(self.point_of_contact, (1, 0))
                dir_list_counter = Config.pos_list.index('UP')
                self.is_horizontal, self.is_vertical = False, True
            else:
                self.target_loc = Operations.addition(self.point_of_contact, (1, 0))
                dir_list_counter = Config.pos_list.index('DOWN')
                self.is_horizontal, self.is_vertical = False, True
            return True
        except OutOfBounds:
            self.dir_list_counter += 1
            return False
    
    def __ship_sunk(self):
        """Confirms ship hit"""
        ship_names = {'U':'Submarine', 'C':'Carrier', 'D':'Destroyer', 'B':'Battleship', 'S':'Cruiser'}
        for key, val in self.ship_part_dict.items():
            game_piece = Pieces.create(key, val)
            ident_to_delete = key
        for key in Config.ships:
            if game_piece.equals(Config.ships[key]):
                self.possible_ship_length.remove(game_piece.get_specifier())
                self.ship_sunk_list.append(key)
                ship_name = ship_names[self.ship_sunk_list[-1]]
                print(f'You sunk my {ship_name}!')
                del self.ship_part_dict[ident_to_delete]

    def get_ship_sunk_list(self):
        """Get ship sunk list"""
        return self.ship_sunk_list;

    def __is_sunk(self):
        """Checks if ship is sunk"""
        if self.dir_list_counter > self.cap:
            self.ship_found = False
            ident_to_delete = 0
            self.__ship_sunk()
            self.dir_list_counter, self.cap = 0, 1
            return True

    def pick_loc_strat(self, def_player, seed):
        """Turn base bot that randomly picks coords until it hits a ship,\
                then strategically finds other parts of ship until ship sunk, then finds other ships"""
        action = Player_Action()
        self.__is_sunk()
        if self.hit_counter == 17:
            while len(self.get_ship_sunk_list()) < 5:
                self.__ship_sunk()
            return self.get_shoot_board()
        
        if self.ship_found:
            if self.is_vertical:
                self.dir_list_counter, self.cap = 2, 3
            while True:
                if self.dir_list_counter >= len(Config.pos_list):
                    self.__is_sunk()
                    return self.get_shoot_board()
                enum_pos = Operations.get_enum_pos(Config.pos_list[self.dir_list_counter])
                if not self.__checker(enum_pos, self.dir_list_counter):
                    continue

                if Operations.get_cell(self.get_shoot_board(), self.target_loc) == 1:
                    print(self.dir_list_counter)
                    self.point_of_contact = self.target_loc
                elif Operations.get_cell(self.get_shoot_board(), self.target_loc) == 2:
                    self.target_loc = self.point_of_contact
                    self.dir_list_counter += 1
                else:
                    temp = self.point_of_contact
                    break
        else:
            self.target_loc = Rand_Vals.get_rand_loc(seed, self)
        cell_ident = Operations.get_cell(self.get_shoot_board(), self.target_loc)  
        while cell_ident == 1 or cell_ident == 2:
            seed += 1
            self.target_loc = Rand_Vals.get_rand_loc(seed, self)
            cell_ident = Operations.get_cell(self.get_shoot_board(), self.target_loc)
        color = Color_Cell()
        ship_ident = color._Color_Cell__mark_cell(self.target_loc, seed, self, def_player)
        if ship_ident:
            self.hit_counter += 1         
            self.point_of_contact = self.target_loc
            self.ship_found = True
            if ship_ident in self.ship_part_dict:
                self.ship_part_dict[ship_ident] += 1
                if self.ship_part_dict[ship_ident] == max(self.possible_ship_length):
                    self.dir_list_counter = self.cap + 1
                    self.__is_sunk()
                    return self.get_shoot_board()
            else:
                self.ship_part_dict[ship_ident] = 1
        else:
            if self.ship_found:
                self.dir_list_counter += 1
        self.__is_sunk()

        return self.get_shoot_board()
