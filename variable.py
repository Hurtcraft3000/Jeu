import pygame
from tile import *
pygame.init()

SCREEN_WIDTH=1000
SCREEN_HEIGHT=int(SCREEN_WIDTH*0.7)
LOWER_MARGIN=0
SIDE_MARGIN=250
screen=pygame.display.set_mode((SCREEN_WIDTH+SIDE_MARGIN,SCREEN_HEIGHT+LOWER_MARGIN))
pygame.display.set_caption("lvl editor")
tiles_image=get_tile_image()[0]
tiles_image_scale=get_tile_image()[1]

scroll_left=False
scroll_right=False
scroll=0
scroll_speed=1

current_tile=0

niveau=1

button_liste=[]
button_colonne=0
button_ligne=0
button_count=0

COLONNE=65
LIGNES=14
Tile_size=50

save_button_x=SCREEN_WIDTH+50
save_button_y=SCREEN_HEIGHT-240

load_button_x=SCREEN_WIDTH+140
load_button_y=SCREEN_HEIGHT-240

font_color=(20,20,20)

sauvegarde_message=False
loading_error_message=False
affichage_message_cd=4000



def load(LIGNES,COLONNE):
    map_data=[]
    for i in range(LIGNES):
        l=[-1]*COLONNE
        map_data.append(l)



    for row in range(LIGNES):
        for i in range(4):
            if row>LIGNES-7:
                map_data[row][i]=8
        for i in range(COLONNE-5,COLONNE):
            if row > LIGNES - 7:
                map_data[row][i] = 8
    for tile in range(COLONNE):
        map_data[-1][tile]=0
    return map_data

map_data=load(LIGNES,COLONNE)

sky=pygame.image.load("map/background ete/5 - Sky_color.png").convert_alpha()
sky=pygame.transform.scale(sky,(SCREEN_WIDTH,SCREEN_HEIGHT))

cloud_cover=pygame.image.load("map/background ete/4 - Cloud_cover_2.png")
cloud_cover=pygame.transform.scale(cloud_cover,(SCREEN_WIDTH,300))

colline=pygame.image.load("map/background ete/2 - Hills.png")
colline=pygame.transform.scale(colline,(SCREEN_WIDTH,300))

buisson=pygame.image.load("map/background ete/1 - Foreground_scenery.png")
buisson=pygame.transform.scale(buisson,(SCREEN_WIDTH,300))
