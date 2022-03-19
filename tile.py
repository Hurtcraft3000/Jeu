import pygame
from os import listdir
from bouton import *
from variable import *

def get_tile_image():


    tile_name_list=listdir("map/tiles")
    tile_image=[]
    tile_image_scale=[]

    for i in range(len(tile_name_list)):
        image = pygame.image.load(f'map/tiles/{i}.png').convert_alpha()
        image_width = image.get_width()
        image_height = image.get_height()
        tile_image.append(image)
        if i==24:


            image = pygame.transform.scale(image, (150, 150))
            tile_image_scale.append(image)
        else:
            image = pygame.transform.scale(image, (image_width*3 , image_height*3 ))

            tile_image_scale.append(image)


    return tile_image,tile_image_scale

def draw_world(screen,data,img_list,scroll):
    tile_size=50
    for y , row in enumerate(data):
        for x , tile in enumerate(row):
            if tile>=0:
                screen.blit(img_list[tile],(x*tile_size-scroll,y*tile_size))
                                    #8-->block de base dans mon fichier





