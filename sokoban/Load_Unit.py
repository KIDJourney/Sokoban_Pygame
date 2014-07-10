#!/usr/bin/env python
# coding=utf-8
#Map Read From File Unit
import pygame
from pygame.locals import *
Game_Map = list()
Map_Wide = 0
Map_Deepth =0
Game_Level = 1
def ReadMap():
    Game_Level
    Game_Map = []
    FileName = "map/"+str(Game_Level)+".dat"
    file = open(FileName,'r')
    Map_Deepth,Map_Wide = map(int,file.readline().split())
    for i in range(Map_Deepth):
        Game_Map.append(file.readline()[:Map_Wide-1])
#Tested

#Image Load Unit
def ImageLoad():
    Image_Box_Inplace = pygame.image.load("source/Box_Inplace.jpg").convert()
    Image_Box_Outplace =pygame.image.load("source/Box_Outplace.JPG").convert()
    Image_Wall = pygame.image.load("source/wall.jpg").convert()
    Image_People = pygame.image.load("source/man.jpb").convert()
    
    Image_Box_Inplace = pygame.transform.scale(Image_Box_Inplace,(64,64))
    Image_Box_Outplace = pygame.transform.scale(Image_Box_Outplace,(64,64))
    Image_Wall = pygame.transform.scale(Image_Wall,(64,64))
    Image_People = pygame.transform.scale(Image_People,(64,64)) 

    return Image_Box_Inplace , Image_Box_Outplace , Image_Wall , Image_People

