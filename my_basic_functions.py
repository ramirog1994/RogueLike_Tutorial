from random import randint, choice


def create_map(number_squares, diccionario):
    lista_valores = list(diccionario.keys())
    mapa_final = []
    for i in range(number_squares):
        linea = ""
        for iterator in range(number_squares):
            linea = linea+choice(lista_valores)
        mapa_final.append(linea)
    return mapa_final


def pos_to_coordinates(pos_x, pos_y, grid_size):
    x_coord = pos_x*grid_size
    y_coord = pos_y*grid_size
    return x_coord, y_coord


def starting_position_generator(number_of_squares):
    return [randint(0, number_of_squares - 1), randint(0, number_of_squares - 1)]


def pos_validator(mapa, number_of_squares):
    number = starting_position_generator(number_of_squares)
    if number in mapa:
        number = pos_validator(mapa, number_of_squares)
    return number


def get_radius_area(pos, radius):  # function to create area for summoning rocks or fireballs
    radius_range = [i for i in range(-radius, radius+1)]
    result = []
    for i in radius_range:
        for x_iter in radius_range:
            result.append([pos[0]+i, pos[1]+x_iter])
    result.remove(pos)
    return result


def push_action(char_list, player_position):
    for i in char_list:
        if [i.pos_x, i.pos_y] in get_radius_area(player_position, 1):
            if i.pos_x > player_position[0]:
                i.pos_x += 1
            elif i.pos_x < player_position[0]:
                i.pos_x -= 1
            else:
                pass
            if i.pos_y > player_position[1]:
                i.pos_y += 1
            elif i.pos_y < player_position[1]:
                i.pos_y -= 1
            else:
                pass


def get_water_positions(full_map,number_of_squares):
    final_list =[]
    for i in full_map:
        for x in range(number_of_squares):
            if i[x] == "w":
                final_list.append([x, full_map.index(i)])
    return final_list


def water_tile_checker(list_entities, map):
    for i in list_entities:
        if [i.pos_x, i.pos_y] in map:
            i.wet = True
        elif [i.pos_x, i.pos_y] not in map and i.wet == True:
            i.wet = False
        i.update_avatar()
