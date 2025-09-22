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

grass_img = pygame.image.load("assets/grass.png")
sand_img = pygame.image.load("assets/sand.png")
spawn_img = pygame.image.load("assets/spawn.png")

#Draw Grid Function
def draw_grid():
    x_offset = 100
    for line in range(0, (screen_width - x_offset) // tile_size + 1):
        x = x_offset + line * tile_size
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, screen_height))

    for line in range(0, screen_height // tile_size + 1):
        y = line * tile_size
        pygame.draw.line(screen, (0, 0, 0), (x_offset, y), (screen_width, y))

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

class World:
    def __init__(self, data):
        self.tile_list = []

        for row in range(len(data)):
            for col in range(len(data[row])):
                x_offset = 100  # Sidebar width
                if data[row][col] == 0:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = x_offset + col * tile_size
                    img_rect.y = row * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if data[row][col] == 1:
                    img = pygame.transform.scale(sand_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = x_offset + col * tile_size
                    img_rect.y = row * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if data[row][col] == 2:
                    img = pygame.transform.scale(spawn_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = x_offset + col * tile_size
                    img_rect.y = row * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if data[row][col] == 3:
                    img = pygame.Surface((tile_size, tile_size))
                    img.fill((255, 0, 0))  # Red
                    img_rect = img.get_rect()
                    img_rect.x = x_offset + col * tile_size
                    img_rect.y = row * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)


    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

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