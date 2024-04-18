import pygame

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Todo:
    def __init__(self):
        pass

class objeto:
    def __init__(self, screen):
        self.screen = screen

class ser_vivo(objeto):
    def __init__(self, screen, pos, size, color):
        super().__init__(screen)
        self.pos = {'x': pos[0], 'y': pos[1]}
        self.size = size
        self.color = color
    
    def draw(self):
        pygame.draw.rect(
            self.screen,
            self.color,
            (self.pos['x']*self.size[0],self.pos['y']*self.size[1],self.size[0], self.size[1]),
            0
        )

    def move(self, dir):
        print(dir)
        if(dir == 0):
            self.pos['y'] = self.pos['y'] - 1
        if(dir == 1):
            self.pos['x'] = self.pos['x'] + 1
        if(dir == 2):
            self.pos['y'] = self.pos['y'] + 1
        if(dir == 3):
            self.pos['x'] = self.pos['x'] - 1

class mapa(objeto):
    def __init__(self, screen, grid_size, cell_size):
        super().__init__(screen)
        self.grid = [[-1 for _ in range(grid_size[0])] for _ in range(grid_size[1])]
        self.cell_size = cell_size

    def draw_grid(self):
        self.screen.fill(BLACK)
        cx = self.cell_size[0]
        cy = self.cell_size[1]
        for y, row in enumerate(self.grid):
            for x, value in enumerate(row):
                color = BLACK if value == -1 else (RED if value == 1 else GREEN)
                pygame.draw.rect(self.screen, WHITE, (x * cx, y * cy, cx, cy), 1)
                pygame.draw.rect(self.screen, WHITE, (x * cx, y * cy, cx, cy), 1)
