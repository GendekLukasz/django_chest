from abc import ABC, abstractmethod

class Chessman(ABC):
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    
    @abstractmethod
    def weight(self): pass

    @abstractmethod
    def get_starting_points_list(): pass

    def position(self): 
        return { 
            'x' : self.x,
            'y' : self.y,
            }
            
    def get_name(self):
        return self.name

    def get_colour(self):
        return self.colour