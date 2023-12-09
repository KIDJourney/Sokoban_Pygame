#!/usr/bin/env python
# coding=utf-8
import pygame
import time
from pygame.locals import *
from sys import exit

DEBUG = True

pygame.init()
Game_Screen = pygame.display.set_mode((768,768),0,32)
Image_Help = pygame.image.load("img/help.png").convert()
Image_Welcome = pygame.image.load("img/welcome2.png").convert()
Image_Box_Inplace = pygame.image.load("img/Box_Inplace.jpg").convert()
Image_Box_Outplace = pygame.image.load("img/Box_Outplace.JPG").convert()
Game_Success = pygame.image.load("img/Success.jpg").convert()
Image_Player = pygame.image.load("img/man2.png").convert()
Image_Goal = pygame.image.load("img/Goal2.png").convert()
Image_Wall = pygame.image.load("img/wall.jpg").convert()
Image_Help = pygame.transform.scale(Image_Help,(768,768))
Image_Welcome = pygame.transform.scale(Image_Welcome,(768,768))
Image_Box_Inplace = pygame.transform.scale(Image_Box_Inplace,(64,64))
Image_Box_Outplace = pygame.transform.scale(Image_Box_Outplace,(64,64))
Image_Player = pygame.transform.scale(Image_Player,(64,64))
Image_Wall= pygame.transform.scale(Image_Wall,(64,64))
Image_Goal = pygame.transform.scale(Image_Goal,(64,64))

#Map Coordinates
#0--------------------> x
#|
#|
#|
#|
#|
#|
#v
#y

def print_map(alist):
    for i in alist:
        print( i.replace("N", "."))

Game_font = pygame.font.SysFont("arial",32)
Game_Map_Source = []
Game_Step = 0
Player_Pos=[0,0]
Game_Level = 1
Game_Map = []
Map_Width = 0
Map_Depth = 0
Game_Path = []
Dir = ((-1,0),(1,0),(0,-1),(0,1))

def read_map(Mission):
    global Game_Map
    global Map_Depth
    global Map_Width
    File_Name ="map/"+ str(Mission) +'.dat'
    with open(File_Name,'r') as file:
        Map_Depth,Map_Width = map(int,file.readline().split())
        for i in range(Map_Depth):
            Game_Map.append(file.readline()[:Map_Width])

def undo():
    global Game_Screen
    global Game_Map
    global Game_Path
    if Game_Path:
        Game_Map = Game_Path.pop()
        refresh_display(Game_Screen)
    elif DEBUG:
        print( "You can't undo")

def start_over():
    global Game_Map_Source
    global Game_Map
    global Game_Screen
    Game_Map = Game_Map_Source[:]
    refresh_display(Game_Screen)

#Map P = Player W = Wall B = Box G=Goal A=achieve N = Way or NULL

def refresh_display(Game_Screen):
    global Game_Level
    global Game_Step
    global Game_Map
    global Map_Depth
    global Map_Width
    global Player_Pos
    Game_Screen.fill((255,255,255))
    for i in range(Map_Depth):
        for j in range(Map_Width):
            pos = [j*64,i*64]
            if Game_Map[i][j]=='P':
                Game_Screen.blit(Image_Player,pos)
                Player_Pos[0]=i
                Player_Pos[1]=j
            elif  Game_Map[i][j]=='W':
                Game_Screen.blit(Image_Wall,pos)
            elif  Game_Map[i][j]=='B':
                Game_Screen.blit(Image_Box_Outplace,pos)
            elif  Game_Map[i][j]=='A':
                Game_Screen.blit(Image_Box_Inplace,pos)
            elif  Game_Map[i][j]=='G':
                Game_Screen.blit(Image_Goal,pos)
    pygame.display.set_caption("Mission "+str(Game_Level))
    #Game_Screen.blit(Game_font.render("space to redo",True,(0,0,0)),(0,Map_Depth*64-32)) 
    pygame.display.update()

def check_win():
    num = 0
    global Game_Map
    global Map_Width
    global Map_Depth
    for i in range(Map_Depth):
        for j in range(Map_Width):
            if Game_Map[i][j]=='B':
                return False
    return True

def default():
    global Game_Map
    global Game_Level
    global Map_Width
    global Map_Depth
    global Game_Path
    global Game_Map_Source
    global Player_Pos
    Game_Path = []
    Game_Map = []
    read_map(Game_Level)
    Game_Map_Source = Game_Map[:]
    pygame.display.set_caption("Mission %s   Step %s" % (str(Game_Level),str(Game_Step)))
    pygame.display.update()
    return pygame.display.set_mode((Map_Width*64,Map_Depth*64),0,32)

def change_map(x,y,object):
    global Game_Map
    Game_Map[x] = Game_Map[x][:y]+object+Game_Map[x][y+1:]

def move(dir):
    global Game_Screen
    global Game_Map
    global Player_Pos
    global Game_Step
    global Game_Path
    global Game_Map_Source
    global Map_Width
    global Map_Depth
    Player_Stand = Game_Map[Player_Pos[0]][Player_Pos[1]]
    Temp_x = Player_Pos[0] + Dir[dir][0]
    Temp_y = Player_Pos[1] + Dir[dir][1]
    #If there is a Box
    if Game_Map[Temp_x][Temp_y] in ('A','B'):
        if DEBUG:
            print( "there is a box")
        if Game_Map[Temp_x+Dir[dir][0]][Temp_y+Dir[dir][1]] in ('N','G'):
            #Move Box 
            Game_Path.append(Game_Map[:])
            if Game_Map[Temp_x+Dir[dir][0]][Temp_y+Dir[dir][1]]=='G':
                change_map(Temp_x+Dir[dir][0],Temp_y+Dir[dir][1],'A')
            else:
                change_map(Temp_x+Dir[dir][0],Temp_y+Dir[dir][1],'B')

            #Change Box to Player
            change_map(Temp_x,Temp_y,'P')

            #Change the Player position to the original floor type
            if Game_Map_Source[Player_Pos[0]][Player_Pos[1]]=='G':
                change_map(Player_Pos[0],Player_Pos[1],"G")
            else:
                change_map(Player_Pos[0],Player_Pos[1],"N")

            Player_Pos[0] = Temp_x
            Player_Pos[1] = Temp_y

    #If there is nothing
    if Game_Map[Temp_x][Temp_y] in ("N","G"):
        if DEBUG:
            print( "there is nothing")
        change_map(Temp_x,Temp_y,'P')
        if Game_Map_Source[Player_Pos[0]][Player_Pos[1]]=='G':
            change_map(Player_Pos[0],Player_Pos[1],"G")
        else:
            change_map(Player_Pos[0],Player_Pos[1],"N")
        Player_Pos[0] = Temp_x
        Player_Pos[1] = Temp_y

    if DEBUG:
        print_map(Game_Map) 
    refresh_display(Game_Screen)

if __name__=="__main__":
    Game_Screen.blit(Image_Welcome,(0,0))
    pygame.display.update()
    flag = True
    while flag:
        Game_Screen.blit(Image_Welcome,(0,0))
        pygame.display.update()                    
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_1:
                    flag=False
                    break
                if event.key == K_2:
                    Game_Screen.blit(Image_Help,(0,0))
                    pygame.display.update()
                    time.sleep(3)
                if event.key == K_3:
                    pygame.display.quit()
                    exit()

    Game_Screen = default()
    refresh_display(Game_Screen)
    while True:
        for event in pygame.event.get():
            if event.type  ==KEYDOWN:
                if event.key == K_UP:
                    move(0)
                elif event.key == K_DOWN:
                    move(1)
                elif event.key == K_LEFT:
                    move(2)
                elif event.key == K_RIGHT:
                    move(3)
                elif event.key == K_r:
                    undo()
                elif event.key == K_SPACE:
                    start_over()
                elif event.key == K_ESCAPE:
                    pygame.display.quit()
                    exit()
            elif event.type == QUIT:
                pygame.display.quit()
                exit()
        if check_win():
            if DEBUG:
                print( "you win")
            time.sleep(1)
            if Game_Level < 3:
                Game_Level += 1
                default()
                refresh_display(Game_Screen)
            else:
                Game_Screen = pygame.display.set_mode((572,416),0,32)
                Game_Screen.blit(Game_Success,(0,0))
                pygame.display.update()
                time.sleep(5)
                pygame.display.quit()
                exit()
