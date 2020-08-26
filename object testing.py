from my_basic_functions import get_radius_area, push_action


class Orc:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.wet = False


lista_orcos = [Orc(10, 10), Orc(20, 20)]

water_tiles = [[15, 15], [10, 10]]

def water_checker():
    for i in lista_orcos:
        if [i.pos_x, i.pos_y] in water_tiles:
            i.wet = True
        elif i.wet == True and [i.pos_x, i.pos_y] not in water_tiles:
            i.wet = False
water_checker()
for i in lista_orcos:
    print(i.wet)

