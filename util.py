import pygame
import random
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
col_n = 10  # número de columnas
row_n = 10  # número de filas

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

import random

def get_highest(array):
    # Find the maximum number in the array
    max_value = max(array)
    
    # Find all the indices where the maximum number occurs
    max_indices = [i for i, num in enumerate(array) if num == max_value]
    
    # If there are more than one maximum numbers, choose one randomly
    if len(max_indices) > 1:
        chosen_index = random.choice(max_indices)
        return chosen_index
    else:
        return max_indices[0]



class Objeto:
    def __init__(self, screen):
        self.screen = screen

class Ser_vivo(Objeto):
    def __init__(self, screen, pos, size, color, grid_size):
        super().__init__(screen)
        self.pos = {'x': pos[0], 'y': pos[1]}
        self.size = size
        self.color = color
        self.q_map = [[[0 for _ in range(4)] for _ in range(grid_size[0])] for _ in range(grid_size[1])]
    
    def info(self):
        print(f'posicion actual {self.pos} vecinos: ', self.q_map[self.pos['y']][self.pos['x']])
        print('q_map\n')
        for row in self.q_map:
            print(row)

    def draw(self):
        pygame.draw.rect(
            self.screen,
            self.color,
            (self.pos['x']*self.size[0],self.pos['y']*self.size[1],self.size[0], self.size[1]),
            0
        )

    def move(self, dir):
        print('moviendo en direccion: ', dir)

        if(dir == 0):
            if self.pos['y'] > 0:
                self.pos['y'] = self.pos['y'] - 1
        if(dir == 1):
            if self.pos['x'] < col_n-1:
                self.pos['x'] = self.pos['x'] + 1
        if(dir == 2):
            if self.pos['y'] < col_n-1:
                self.pos['y'] = self.pos['y'] + 1
        if(dir == 3):
            if self.pos['x'] > 0:
                self.pos['x'] = self.pos['x'] - 1

    def q_learn(self, dir, value):
        self.q_map[self.pos['y']][self.pos['x']][dir] += value

class Mapa(Objeto):
    def __init__(self, screen, grid_size, cell_size):
        super().__init__(screen)
        self.map = [[-1 for _ in range(grid_size[0])] for _ in range(grid_size[1])]
        self.cell_size = cell_size

    def draw_grid(self):
        self.screen.fill(BLACK)
        cx = self.cell_size[0]
        cy = self.cell_size[1]
        for y, row in enumerate(self.map):
            for x, value in enumerate(row):
                color = BLACK if value == -1 else (RED if value == 1 else GREEN)
                pygame.draw.rect(self.screen, WHITE, (x * cx, y * cy, cx, cy), 1)
                pygame.draw.rect(self.screen, WHITE, (x * cx, y * cy, cx, cy), 1)

    def get_neighbors(self, current_pos):
        neighbors = []
        # arriba
        if current_pos['y'] > 0:
            neighbors.append(self.map[current_pos['y']-1][current_pos['x']])
        else:
            neighbors.append(-100)

        # derecha
        if current_pos['x'] < col_n-1:
            neighbors.append(self.map[current_pos['y']][current_pos['x']+1])
        else:
            neighbors.append(-100)
        
        # abajo
        if current_pos['y'] < col_n-1:
            neighbors.append(self.map[current_pos['y']+1][current_pos['x']])
        else:
            neighbors.append(-100)
            
        # izquierda
        if current_pos['x'] > 0:
            neighbors.append(self.map[current_pos['y']][current_pos['x']-1])
        else:
            neighbors.append(-100)

        return neighbors
