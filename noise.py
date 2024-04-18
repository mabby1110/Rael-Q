import pygame
import util

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Tamaño de la ventana
WIDTH = 800
HEIGHT = 800

# Tamaño del grid y celdas
n = 10  # número de columnas
m = 10  # número de filas
CELL_SIZE = [WIDTH // n, HEIGHT // m]
print(CELL_SIZE[0])
print(CELL_SIZE[1])
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    # inicializar mapa y objetos

    mapa = util.mapa(
        screen=screen,
        grid_size=[10, 10],
        cell_size=CELL_SIZE
    )
    robot = util.ser_vivo(
        screen=screen,
        pos=[0,0],
        size=CELL_SIZE,
        color=(255, 0, 255)
    )

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update logic
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            robot.move(0)
        if keys[pygame.K_d]:
            robot.move(1)
        if keys[pygame.K_s]:
            robot.move(2)
        if keys[pygame.K_a]:
            robot.move(3)
        if keys[pygame.K_F10]:
            return 0
        if keys[pygame.K_ESCAPE]:
            return 1
            
        # draw
        mapa.draw_grid()
        robot.draw()

        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    state = 0

    while state == 0:
        state = main()