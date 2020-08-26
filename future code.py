class Ogre:
    def __init__(self):
        self.surface = ogre
        self.initial_pos = funcion_posicion()
        self.pos_x = self.initial_pos[0]
        self.pos_y = self.initial_pos[1]



class Player:
    def __init__(self):
        self.surface = elf
        self.pos_x = 9
        self.pos_y = 1

    def move_up(self):
        if self.pos_y != 0:
            self.pos_y -= 1

    def move_down(self):
        if self.pos_y != number_of_squares:
            self.pos_y += 1

    def move_right(self):
        if self.pos_x != number_of_squares:
            self.pos_x += 1

    def move_left(self):
        if self.pos_x != 0:
            self.pos_x -= 1
