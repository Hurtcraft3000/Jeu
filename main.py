import pygame
from background import *
from tile import *
from bouton import *

import csv
from variable import *
pygame.init()






for i in range(len(tiles_image)):
    tile_button=Bouton(SCREEN_WIDTH+(50*button_colonne)+5,(50*button_ligne)+10,tiles_image[i])
    button_liste.append(tile_button)
    button_colonne+=1
    if button_colonne==3:
        button_ligne+=1
        button_colonne=0




run=True




save_img=pygame.image.load("bouton_menu/save_btn.png").convert_alpha()
save_img=pygame.transform.scale(save_img,(100,50))
load_image=pygame.image.load("bouton_menu/load_btn.png").convert_alpha()
load_image= pygame.transform.scale(load_image,(100,50))

save_button=Bouton(save_button_x-40,save_button_y+50,save_img)
load_button=Bouton(load_button_x,load_button_y+50,load_image)



font_pixel=pygame.font.Font("font/font_pixel.TTF",24)

def draw_text(text,font,text_color,x,y):
    img=font.render(text,True,text_color)
    screen.blit(img,(x,y))

def confirmation():
    #demande a l'user si il veut vrmt save
    pass


while run==True:

    draw_background(screen, scroll)

    grille(screen, SCREEN_HEIGHT, SCREEN_WIDTH, scroll)
    draw_world(screen, map_data, tiles_image_scale, scroll)
    pygame.draw.rect(screen, (50, 50, 50), (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))

    draw_text(f"lvl:{niveau}",font_pixel,font_color,0,0)
    #draw_text("fleche du haut ou du bas pour changer de lvl",font_pixel,font_color,130,SCREEN_HEIGHT-40)
    #draw_text("SAVE",font_pixel,font_color,save_button_x,save_button_y+110)
    #draw_text("LOAD",font_pixel,font_color,load_button_x,load_button_y+110)


    if sauvegarde_message==True:
        draw_text("sauvegarde", font_pixel, font_color, save_button_x-25, save_button_y + 100)
        draw_text("effectuer", font_pixel, font_color, save_button_x - 25, save_button_y + 130)
        if pygame.time.get_ticks()-temp_affichage_save>affichage_message_cd:
            sauvegarde_message=False


    if save_button.draw(screen)==True:
        sauvegarde_message=True
        temp_affichage_save=pygame.time.get_ticks()

        with open(f"lvl{niveau}_data.csv","w",newline="") as csvfile:
            writer=csv.writer(csvfile,delimiter=",")
            for ligne in map_data:
                writer.writerow(ligne)

    if load_button.draw(screen)==True:

        scroll=0
        try:
            with open(f"lvl{niveau}_data.csv",newline="") as csvfile:
                reader=csv.reader(csvfile,delimiter=",")
                for x,ligne in enumerate(reader):
                    for y,tile in enumerate(ligne):
                        map_data[x][y]=int(tile)

        except:
            loading_error_message=True
            temp_affichage_load = pygame.time.get_ticks()

            with open("lvl0_data.csv", newline="") as csvfile:
                reader = csv.reader(csvfile, delimiter=",")
                for x, ligne in enumerate(reader):
                    for y, tile in enumerate(ligne):
                        map_data[x][y] = int(tile)

    if loading_error_message == True:
        pygame.draw.rect(screen, (0, 0, 0), (350, 50, 350, 50))
        draw_text("niveau inexistant", font_pixel, (200,200,200), 375, 50)

        if pygame.time.get_ticks() - temp_affichage_load > affichage_message_cd:

            loading_error_message = False



    for button_count,button in enumerate(button_liste):
        if button.draw(screen)==True:
            current_tile=button_count

        button.draw(screen)


    pygame.draw.rect(screen,(255,0,0),button_liste[current_tile],3)




    if scroll_left==True and scroll>0:
        scroll=scroll-10*scroll_speed
    if scroll_right==True and scroll<(COLONNE*Tile_size)-SCREEN_WIDTH:
        scroll=scroll+10*scroll_speed

    #ajouter tile
    pos=pygame.mouse.get_pos()
    x=(pos[0]+scroll)//Tile_size
    y=pos[1]//Tile_size

    if pos[0]<SCREEN_WIDTH and pos[1]<SCREEN_HEIGHT:
        if pygame.mouse.get_pressed()[0]==1:
            if map_data[y][x]!=current_tile:
                map_data[y][x]=current_tile
        if pygame.mouse.get_pressed()[2]==1:
            map_data[y][x]=-1



    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                scroll_left=True
            if event.key==pygame.K_RIGHT:
                scroll_right=True
            if event.key==pygame.K_LSHIFT:
                scroll_speed=5
            if event.key==pygame.K_UP and niveau>=2:
                niveau-=1
            if event.key==pygame.K_DOWN:
                niveau+=1


        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                scroll_left=False
            if event.key==pygame.K_RIGHT:
                scroll_right=False
            if event.key==pygame.K_LSHIFT:
                scroll_speed=1
            

    pygame.display.flip()
    
pygame.quit()


