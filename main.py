import pygame
import math

pygame.init()
pygame.font.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TD")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

tile_size = 50

#Draw Grid Function
def draw_grid():

    for line in range(0, (screen_width - 100) // tile_size + 1):
        x = 100 + line * tile_size
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, screen_height))

    for line in range(0, screen_height // tile_size + 1):
        y = line * tile_size
        pygame.draw.line(screen, (0, 0, 0), (100, y), (screen_width, y))

world_data = [
    [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

class World():
    def __init__(self, data):
        self.tile_list = []

        for row in range(len(data)):
            for col in range(len(data[row])):
                color = None
                if data[row][col] == 0:
                    color = (0, 0, 255)
                elif data[row][col] == 1:
                    color = (255, 0, 0)
                elif data[row][col] == 2:
                    color = (255, 255, 255)
                elif data[row][col] == 3:
                    color = (0, 255, 0)
                if color:
                    tile_surface = pygame.Surface((tile_size, tile_size))
                    tile_surface.fill(color)
                    tile_rect = tile_surface.get_rect()
                    tile_rect.topleft = (100 + col * tile_size, row * tile_size)
                    self.tile_list.append((tile_surface, tile_rect))

    def draw(self):
        for tile_surface, tile_rect in self.tile_list:
            screen.blit(tile_surface, tile_rect)

world = World(world_data)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (220, 220, 220), (0, 0, 100, screen_height))

    world.draw()
    draw_grid()

    pygame.display.flip()

pygame.quit()