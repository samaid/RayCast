import pygame
from settings import *
from player import Player
from map import world_map
from ray_casting import ray_casting
import math

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player()

do_game = True
while do_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            do_game = False

    player.movement()

    sc.fill(BLACK)

    pygame.draw.rect(sc, BLUE, (0, 0, WIDTH, HALF_HEIGHT))
    pygame.draw.rect(sc, DARK_GRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    ray_casting(sc, player.pos, player.angle)

    #pygame.draw.circle(sc, GREEN, (int(player.x), int(player.y)), 12)
    #pygame.draw.line(sc, GREEN, (int(player.x), int(player.y)), (int(player.x + WIDTH * math.cos(player.angle)),
    #                                                             int(player.y + HEIGHT * math.sin(player.angle))))

    #for x, y in world_map:
    #    pygame.draw.rect(sc, DARK_GRAY, (x, y, TILE, TILE), 2)

    pygame.display.flip()
    clock.tick(FPS)
