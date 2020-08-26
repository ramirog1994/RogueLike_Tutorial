import pygame
# from random import choice, randint
from my_basic_functions import *

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_a,
    K_b,
)
pygame.init()

# Window Parameters
GRID_SIZE = 48
NUMBER_OF_SQUARES = 17
GUI_SIZE = 2
TEXT_RECORD_SIZE = 4
WIDTH = GRID_SIZE * (NUMBER_OF_SQUARES + TEXT_RECORD_SIZE)  # screen width
LENGHT = GRID_SIZE * (NUMBER_OF_SQUARES + GUI_SIZE)
screen = pygame.display.set_mode([WIDTH, LENGHT])
boardgame = pygame.Surface((NUMBER_OF_SQUARES*GRID_SIZE, NUMBER_OF_SQUARES*GRID_SIZE))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def size_sprites(file_location, grid_size=GRID_SIZE):
    end_product = pygame.image.load(file_location)
    end_product = pygame.transform.scale(end_product, (grid_size, grid_size))
    return end_product


def make_ground(base_map, base_dict, grid_size, number_of_squares):
    for i in range(number_of_squares):
        for x in range(number_of_squares):
            boardgame.blit(base_dict[base_map[x][i]], (x*grid_size, i*grid_size))


def draw_char(lista_char, grid_size):
    for i in lista_char:
        boardgame.blit(i.surface, pos_to_coordinates(i.pos_x, i.pos_y, grid_size))


def draw_GUI(list_GUI, grid_size=GRID_SIZE):
    for i in list_GUI:
        screen.blit(i, (list_GUI.index(i)*grid_size*2, NUMBER_OF_SQUARES*grid_size))
        pygame.draw.line(
            screen,
            WHITE,
            (list_GUI.index(i)*grid_size*2,
             NUMBER_OF_SQUARES*grid_size),
            (list_GUI.index(i)*grid_size*2,
             NUMBER_OF_SQUARES*(6+grid_size))
        )


def update_avatar(base_surface, surface_to_add):
    return base_surface.blit(surface_to_add, (0, 0))


# creatures
snake = size_sprites('assets/grey_snake.png')
elf = size_sprites('assets/deep_elf_high_priest.png')
fire = size_sprites('assets/i-rod_destruction_fire.png')
ogre = size_sprites('assets/ogre.png')
# floor tiles
stone_floor = size_sprites('assets/stone_floor.png')
water_floor = size_sprites('assets/water_floor.png')
grass_floor = size_sprites('assets/grass_floor.png')
# obejcts
rock = size_sprites('assets/rock.png')
rock2 = size_sprites('assets/rock.png', 96)
arrow = size_sprites('assets/arrow2.png', 96)
flame = size_sprites('assets/flame.png', 96)
snake2 = size_sprites('assets/grey_snake.png', 96)
# status
fire_status = pygame.image.load('assets/i-rod_destruction_fire.png')
water_status = pygame.image.load('assets/i-water.png')

# dictionary that relates map with sprites
floor_dict = {"s": stone_floor, "w": water_floor, "g": grass_floor}
level_map = create_map(NUMBER_OF_SQUARES, floor_dict)
char_base_map = [[9, 1]]


class Ogre:
    def __init__(self):
        self.surface = size_sprites('assets/ogre.png')
        self.initial_pos = pos_validator(char_base_map, NUMBER_OF_SQUARES)
        self.pos_x = self.initial_pos[0]
        self.pos_y = self.initial_pos[1]
        self.hp = 15
        self.wet = False
        self.old_surface = ogre

    def move_randomly(self):
        self.pos_x += randint(-1, 1)
        self.pos_y += randint(-1, 1)

    def get_hurt(self, damage):
        self.hp -= damage


class Rock:
    def __init__(self, pos_x, pos_y):
        self.surface = rock
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.wet = False


class Player:
    def __init__(self):
        self.surface = elf
        self.pos_x = 9
        self.pos_y = 1
        self.rock_level = 1

    def move_up(self):
        if self.pos_y != 0:
            self.pos_y -= 1

    def move_down(self):
        if self.pos_y != NUMBER_OF_SQUARES - 1:  # number_of_squares - 1 = BOARDGAME
            self.pos_y += 1

    def move_right(self):
        if self.pos_x != NUMBER_OF_SQUARES - 1:  # number_of_squares - 1 = BOARDGAMES
            self.pos_x += 1

    def move_left(self):
        if self.pos_x != 0:
            self.pos_x -= 1

    def summon_rock(self):
        for i in get_radius_area([self.pos_x, self.pos_y], self.rock_level):
            list_char.append(Rock(i[0], i[1]))


elfo1 = Player()

ogro1 = Ogre()
ogro2 = Ogre()
list_char = [Rock()]
# list_char = [Ogre() for i in range(4)]
list_char2 = [elfo1]
list_GUI = [rock2, snake2, arrow]


running = True
while running:
    make_ground(level_map, floor_dict, GRID_SIZE, NUMBER_OF_SQUARES)
    draw_GUI(list_GUI)
    draw_char(list_char, GRID_SIZE)
    draw_char(list_char2, GRID_SIZE)
    screen.blit(boardgame, (0, 0))
    # water_tile_checker(list_char, [[0,0], [1, 1], [5, 5]])
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                elfo1.move_up()
            elif event.key == K_DOWN:
                elfo1.move_down()
            elif event.key == K_LEFT:
                elfo1.move_left()
            elif event.key == K_RIGHT:
                elfo1.move_right()
            elif event.key == K_DOWN:
                elfo1.move_down()
            elif event.key == K_a:
                elfo1.summon_rock()
            elif event.key == K_b:
                push_action(list_char, [elfo1.pos_x, elfo1.pos_y])
            elif event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    pygame.display.flip()

pygame.quit()
