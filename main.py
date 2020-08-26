from sprites import Ogre, Player
from new_engine import Engine


def blit_all(surface, sets):
    for i in sets:
        surface.blit(i.surface, (i.pos_x, i.pos_y))


a = Player()
b = Ogre()

set_elements = (a, b)
test_engine = Engine(set_elements)


def main():
    while test_engine.running is True:
        blit_all(test_engine.base_display, test_engine.entities)
        test_engine.event_handler()
        test_engine.update_screen()


main()
