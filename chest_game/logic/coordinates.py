class Coordinates():

    axis_x = {
        'a' : 0,
        'b' : 1,
        'c' : 2,
        'd' : 3,
        'e' : 4,
        'f' : 5,
        'g' : 6,
        'h' : 7}

    axis_y = {
        '1' : 7,
        '2' : 6,
        '3' : 5,
        '4' : 4,
        '5' : 3,
        '6' : 2,
        '7' : 1,
        '8' : 0}

    def __init__(self, field_name):
        self.field_name = field_name
        self.coordinates = self.field_name_to_coordinates(field_name)

    def field_name_to_coordinates(self, field_name):
        if len(field_name) == 2:
            y = Coordinates.axis_y[field_name[1]]
            x = Coordinates.axis_x[field_name[0]]
            return [x,y]
        else:
            return None

    def get_field_name(self):
        field_name = ''
        for x in self.axis_x:
            if self.coordinates[0] == self.axis_x[x]:
                field_name += x
        for y in self.axis_y:
            if self.coordinates[1] == self.axis_y[y]:
                field_name += y
        return field_name

    def change_coordinates(self, coor_to_add):
        new_x = self.get_x() + coor_to_add[0]
        new_y = self.get_y() + coor_to_add[1]
        if (0 <= new_x < 8) and (0 <= new_y < 8):
            self.coordinates[0] = new_x
            self.coordinates[1] = new_y
            return True
        else:
            return False

    def get_coordinates(self):
        return self.coordinates

    def get_x(self):
        return self.coordinates[0]

    def get_y(self):
        return self.coordinates[1]

    def get_absolute_value(self, coordinates):
        return [coordinates.get_x() - self.get_x(),coordinates.get_y() - self.get_y()]

    def compare_coordinates(self, coordinates):
        return self.get_x() == coordinates.get_x() and self.get_y() == coordinates.get_y()