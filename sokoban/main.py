#!/usr/bin/env python
# coding=utf-8
import pygame
import time
from pygame.locals import *
from sys import exit
#Read Image Unit
pygame.init()
Game_Screen = pygame.display.set_mode((1024,1024),0,28)
Image_Box_Inplace = pygame.image.load("source/Box_Inplace.jpg").convert()
Image_Box_Outplace = pygame.image.load("source/Box_Outplace.JPG").convert()
Image_Player = pygame.image.load("source/man.jpg").convert()
Image_Goal = pygame.image.load("source/Goal.jpg").convert()
Image_Wall = pygame.image.load("source/wall.jpg").convert()
Image_Box_Inplace = pygame.transform.scale(Image_Box_Inplace,(64,64))
Image_Box_Outplace = pygame.transform.scale(Image_Box_Outplace,(64,64))
Image_Player = pygame.transform.scale(Image_Player,(64,64))
Image_Wall= pygame.transform.scale(Image_Wall,(64,64))
Image_Goal = pygame.transform.scale(Image_Goal,(64,64))
#Read1 Image Unit Done

#The Map
#0--------------------> x
#|
#|
#|
#|
#|
#|
#v
#y
#Don't Forget the address

#Global Vara
Game_Map_Source = []
Game_Step = 0
Player_Pos=[0,0]
Game_Level = 1
Game_Map = []
Map_Wide = 0
Map_Deepth = 0
Game_Path = []
Dir = ((-1,0),(1,0),(0,-1),(0,1))

#Global Var Done

#Read Map Unit
def Map_Reader(Mission):
    global Game_Map
    global Map_Deepth
    global Map_Wide
    File_Name ="map/"+ str(Mission) +'.dat'
    file = open(File_Name,'r')
    Map_Deepth,Map_Wide = map(int,file.readline().split())
    for i in range(Map_Deepth):
        Game_Map.append(file.readline()[:Map_Wide])
    file.close()
#Read Map Unit Done

#Map P = Player W = Wall B = Box G=Goal A=achieve N = Way or NULL
#Draw Map Unit
def Display_refresh(Game_Screen):
    global Game_Level
    global Game_Step
    global Game_Map
    global Map_Deepth
    global Map_Wide
    global Player_Pos
    Game_Screen.fill((255,255,255))
    for i in range(Map_Deepth):
        for j in range(Map_Wide):
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
    pygame.display.set_caption("Mission %s   Step %s" % (str(Game_Level),str(Game_Step)))
    pygame.display.update()
#Draw Map Unit Done

#Check Unit
def Check_Win():
    num = 0
    global Game_Map
    global Map_Wide
    global Map_Deepth
    for i in range(Map_Deepth):
        for j in range(Map_Wide):
            if Game_Map[i][j]=='B':
                return False
    return True
#Check Win Unit 

#Defult Unit
def Defult():
    global Game_Map
    global Game_Level
    global Map_Wide
    global Map_Deepth
    global Game_Path
    global Game_Map_Source
    global Player_Pos
    Game_Path = []
    Game_Map = []
    Map_Reader(Game_Level)
    Game_Map_Source = Game_Map[:]
    pygame.display.set_caption("Mission %s   Step %s" % (str(Game_Level),str(Game_Step)))
    return pygame.display.set_mode((Map_Wide*64,Map_Deepth*64),0,32)
#Defult Unit Done

#Map Change Unit
def Change_Map(x,y,object):
    global Game_Map
    Game_Map[x] = Game_Map[x][:y]+object+Game_Map[x][y+1:]
#Map Change Done

#Move Unit
def Move(dir):
    global Game_Screen
    global Game_Map
    global Player_Pos
    global Game_Step
    global Game_Path
    global Game_Map_Source
    global Map_Wide
    global Map_Deepth
    Player_Stand = Game_Map[Player_Pos[0]][Player_Pos[1]]
    Temp_x = Player_Pos[0] + Dir[dir][0]
    Temp_y = Player_Pos[1] + Dir[dir][1]
    print Temp_x,Temp_y
    print Game_Map[Temp_x][Temp_y]
    #If there is a Box
    if Game_Map[Temp_x][Temp_y]=="B":
        print "there is a box"
        if Game_Map[Temp_x+Dir[dir][0]][Temp_y+Dir[dir][1]] in ('N','G'):
            #Move Box 
            if Game_Map[Temp_x+Dir[dir][0]][Temp_y+Dir[dir][1]]=='G':
                Change_Map(Temp_x+Dir[dir][0],Temp_y+Dir[dir][1],'A')
            else:
                Change_Map(Temp_x+Dir[dir][0],Temp_y+Dir[dir][1],'B')
            #Change Box to Play
            Change_Map(Temp_x,Temp_x,'P')
            #Change Player to what he use to stand;
            if Game_Map_Source[Player_Pos[0]][Player_Pos[1]]=='G':
                Change_Map(Player_Pos[0],Player_Pos[1],"G")
            else:
                Change_Map(Player_Pos[0],Player_Pos[1],"N")
            #Update Player_Pos
            Player_Pos[0] = Temp_x
            Player_Pos[1] = Temp_y
    #if there is nothing
    if Game_Map[Temp_x][Temp_y] in ("N","G"):
        print "do it"
        Change_Map(Temp_x,Temp_y,'P')
        if Game_Map_Source[Player_Pos[0]][Player_Pos[1]]=='G':
            Change_Map(Player_Pos[0],Player_Pos[1],"G")
        else:
            Change_Map(Player_Pos[0],Player_Pos[1],"N")
        Player_Pos[0] = Temp_x
        Player_Pos[1] = Temp_y
    Display_refresh(Game_Screen)
    #else do nothing

if __name__=="__main__":
    Game_Screen = Defult()
    Display_refresh(Game_Screen)
    print Player_Pos
    print Game_Map
    while True:
        for event in pygame.event.get():
            if event.type  ==KEYDOWN:
                if event.key == K_UP:
                    Move(0)
                elif event.key == K_DOWN:
                    Move(1)
                elif event.key == K_LEFT:
                    Move(2)
                elif event.key == K_RIGHT:
                    Move(3)
            elif event.type == QUIT:
                exit()
