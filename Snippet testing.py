import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_a,
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
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

gui = pygame.Surface((TEXT_RECORD_SIZE*GRID_SIZE, GRID_SIZE*NUMBER_OF_SQUARES))
gui.fill(WHITE)

base_texto = pygame.font.SysFont("consolas", 20)
texto = base_texto.render("Has subido", True, BLACK)

class Report:
    def __init__(self):
        self.font = "consolas"
        self.size = 20
        self.base = pygame.font.SysFont(self.font, self.size)
        self.text = "Has subido"
        self.end_producto = self.base.render(self.text, True, BLACK)

    def get_surface(self):
        return self.end_producto

    def modify_text(self, new_text):
        self.text = new_text
        self.end_producto = self.base.render(self.text, True, BLACK)

current_report = Report()
running = True
while running:
    screen.blit(gui, (GRID_SIZE*NUMBER_OF_SQUARES, 0))
    gui.blit(current_report.end_producto, (0, 0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                current_report.modify_text("Has apretado arriba")
                gui.blit(current_report.end_producto, (0, 0))
                pygame.display.flip()
        elif event.type == QUIT:
            running = False
    pygame.display.flip()

pygame.quit()


####
    def update_avatar(self):
        if self.wet is True:
            update_avatar(self.surface, water_status)
#        if self.wet is False and self.surface != self.old_surface:
#            self.surface = self.old_surface