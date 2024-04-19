import pygame
import copy
from util import *

CELL_SIZE = [WIDTH // row_n, HEIGHT // col_n]

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    play = 1
    dir = 0
    iterations = 0
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
    mapa.map[9][9] = 50
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Obtiene las teclas presionadas
        keys = pygame.key.get_pressed()

        # Verifica si no se está presionando ninguna tecla
        no_key_pressed = all(key == 0 for key in keys)

        if play == True:
            current_pos = copy.copy(robot.pos)

            # obtenemos mejor opcion del q_map para Q1
            n_q1 = robot.q_map[robot.pos['y']][robot.pos['x']]
            dir_q1 = choose_highest_random(n_q1)
            robot.move(dir_q1)
            reward_Q1 = mapa.map[robot.pos['y']][robot.pos['x']]


            # obtenemos mejor opcion del q_map para Q2
            n_q2 = robot.q_map[robot.pos['y']][robot.pos['x']]
            dir_q2 = choose_highest_random(n_q2)
            robot.move(dir_q2)
            reward_Q2 = mapa.map[robot.pos['y']][robot.pos['x']]

            # Q.learning
            robot.pos = current_pos
            q_obs = reward_Q1 + 0.9*reward_Q2
            td = q_obs - robot.q_map[robot.pos['y']][robot.pos['x']][dir_q1]
            robot.q_map[robot.pos['y']][robot.pos['x']][dir_q1] += td*0.2
            print(f"current_pos {robot.pos} to {dir_q1}")
            robot.move(dir_q1)

            # ver datos
            robot.info()
            print(f"\nnew_pos {robot.pos}\n\n")
            robot.state += 1

            if robot.pos == {'x':9, 'y':9}:
                if iterations >= 40:
                    play = -1
                    robot.info()
                else:
                    robot.info()
                    iterations += 1
                    robot.state = 0
                    robot.pos = {'x':0, 'y':0}
            
        if not no_key_pressed:
            if keys[pygame.K_F10]:
                return 0
            if keys[pygame.K_SPACE]:
                play *= -1
            if keys[pygame.K_ESCAPE]:
                return 1

        # draw
        mapa.draw_grid()
        robot.draw()
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    state = 0

    while state == 0:
        state = main()