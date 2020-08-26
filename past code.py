# def make_grid(windows_size=WIDTH, grid=GRID_SIZE):
#     for i in range(1, number_of_squares):
#         pygame.draw.line(screen, BLACK, (i * grid, 0), (i * grid, windows_size))
#         pygame.draw.line(screen, BLACK, (0, i * grid), (windows_size, i * grid))
from test_module import sumatoria

print(sumatoria(7, 8))


# movimiento y eliminacion
if event.type == KEYDOWN:
    for i in list_char:
        if i.hp == 0:
            list_char.remove(i)
        i.get_hurt(1)
        i.move_randomly()
    pygame.display.flip()

