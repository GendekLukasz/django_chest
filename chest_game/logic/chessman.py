from abc import ABC, abstractmethod
from chest_game.logic.coordinates import Coordinates

class Chessman(ABC):
    def __init__(self, name, colour, coordinates):
        self.name = name
        self.colour = colour
        self.number_of_moves = 0
        self.coordinates = Coordinates(coordinates)
    
    @abstractmethod
    def weight(self): pass

    @abstractmethod
    def get_starting_points_list(): pass

    @abstractmethod
    def check_move(): pass
    
    @abstractmethod
    def check_move_collision(): pass

    def get_name(self):
        return self.name

    def get_colour(self):
        return self.colour
    
    def add_move(self):
        self.number_of_moves += 1

    def get_number_of_moves(self):
        return self.number_of_moves

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def get_coordinates_for_coolision_check(self, move):
        return {
            'from_x' : move.get_from_coor().get_x() if move.get_from_coor().get_x() <= move.get_to_coor().get_x() else move.get_to_coor().get_x(),
            'from_y' : move.get_from_coor().get_y() if move.get_from_coor().get_y() <= move.get_to_coor().get_y() else move.get_to_coor().get_y(),
            'to_x' : move.get_to_coor().get_x() if move.get_from_coor().get_x() <= move.get_to_coor().get_x() else move.get_from_coor().get_x(),
            'to_y' : move.get_to_coor().get_y() if move.get_from_coor().get_y() <= move.get_to_coor().get_y() else move.get_from_coor().get_y(),
        }