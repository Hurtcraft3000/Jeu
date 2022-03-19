import pygame
from variable import *


def draw_background(screen,scroll):


    for x in range(3):
        screen.blit(sky,((x*SCREEN_WIDTH)-scroll*0.5,0))
        screen.blit(cloud_cover,((x*SCREEN_WIDTH)-scroll*0.6,300))
        screen.blit(colline,((x*SCREEN_WIDTH)-scroll*0.7,400))
        screen.blit(buisson,((x*SCREEN_WIDTH)-scroll*0.8,450))


def grille(screen,hauteur,largeur,scroll):


    BLACK=(0,0,0)

    for x in range(COLONNE+1):
        pygame.draw.line(screen,BLACK,((x*Tile_size-scroll),0),((x*Tile_size-scroll),hauteur-Tile_size))
    for x in range(LIGNES):
        pygame.draw.line(screen,BLACK, (0-Tile_size,(x*Tile_size)) , (largeur,(x*Tile_size) ))
