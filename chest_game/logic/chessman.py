from abc import ABC, abstractmethod
from chest_game.logic.coordinates import Coordinates

class Chessman(ABC):
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.number_of_moves = 0
    
    @abstractmethod
    def weight(self): pass

    @abstractmethod
    def get_starting_points_list(): pass

    @abstractmethod
    def check_move(): pass
    
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