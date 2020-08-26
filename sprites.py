from pygame import image
# from pygame import sprite ### possible parent class


class Ogre:
    def __init__(self):
        self.surface = image.load("ogre.png")
        self.pos_x, self.pos_y = 10, 10


class Player:
    def __init__(self):
        self.surface = image.load("deep_elf_high_priest.png")
        self.pos_x, self.pos_y = 42, 42
