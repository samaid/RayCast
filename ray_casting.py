import math

import pygame
from settings import *
from map import world_map

def ray_casting(sc, pos, angle):
    cur_angle = angle - HALP_FOV
    xo, yo = pos

    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            x = xo + depth*cos_a
            y = yo + depth*sin_a
            #pygame.draw.line(sc, DARK_GRAY, pos, (x, y), 2)

            if (x // TILE*TILE, y // TILE*TILE) in world_map:
                depth *= math.cos(angle - cur_angle)
                proj_height = PROJ_COEFF / depth
                c = 255 / (1 + depth*depth*0.0001)
                color = (c//2, c//2, c)
                pygame.draw.rect(sc, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                break
        cur_angle += DELTA_ANGLE
