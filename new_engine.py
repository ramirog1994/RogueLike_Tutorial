import pygame
import sprites
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from sprites import Player


class Engine:
    def __init__(self, entities: sprites, player):
        pygame.init()
        self.base_display = pygame.display.set_mode([500, 500])
        self.running = True
        self.entities = entities
        self.player = Player()

    def shut_down(self):
        self.running = False

    def event_handler(self):
        for event in pygame.event.get():
            action = event.type

            if action is None:
                continue

            action.perform()



    def update_screen(self):
        pygame.display.flip()
