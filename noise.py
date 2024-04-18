import pygame
from util import *

CELL_SIZE = [WIDTH // row_n, HEIGHT // col_n]
print(CELL_SIZE[0])
print(CELL_SIZE[1])

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dir = 0
    # inicializar mapa y objetos

    mapa = Mapa(
        screen=screen,
        grid_size=[10, 10],
        cell_size=CELL_SIZE
    )
    robot = Ser_vivo(
        screen=screen,
        pos=[0,0],
        size=CELL_SIZE,
        color=(255, 0, 255),
        grid_size=[10, 10]
    )

    robot.info()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Obtiene las teclas presionadas
        keys = pygame.key.get_pressed()

        # Verifica si no se está presionando ninguna tecla
        no_key_pressed = all(key == 0 for key in keys)

        if not no_key_pressed:
            # Solo permite un movimiento por ciclo de juego
            moved = False

            if keys[pygame.K_w] and not moved:
                dir = 0
                robot.move(dir)
                moved = True
            if keys[pygame.K_d] and not moved:
                dir = 1
                robot.move(dir)
                moved = True
            if keys[pygame.K_s] and not moved:
                dir = 2
                robot.move(dir)
                moved = True
            if keys[pygame.K_a] and not moved:
                dir = 3
                robot.move(dir)
                moved = True

            if keys[pygame.K_F10]:
                return 0
            if keys[pygame.K_ESCAPE]:
                return 1

            neigbors = mapa.get_neighbors(robot.pos)
            robot.q_learn(dir, neigbors[dir])

        # draw
        mapa.draw_grid()
        robot.draw()
        pygame.display.flip()
        clock.tick(10)


if __name__ == '__main__':
    state = 0

    while state == 0:
        state = main()