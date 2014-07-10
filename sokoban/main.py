#!/usr/bin/env python
# coding=utf-8
import pygame
from pygame.locals import *
#Read Image Unit
pygame.init()
screen = pygame.display.set_mode((1024,1024),0,28)
Image_Box_Inplace = pygame.image.load("source/Box_Inplace.jpg").convert()
Image_Box_Outplace = pygame.image.load("source/Box_Outplace.JPG").convert()
Image_Player = pygame.image.load("source/man.png").convert_alpha()
Image_Wall = pygame.image.load("source/wall.jpg").convert()
Image_Box_Inplace = pygame.transform.scale(Image_Box_Inplace,(64,64))
Image_Box_Outplace = pygame.transform.scale(Image_Box_Outplace,(64,64))
Image_Player = pygame.transform.scale(Image_Player,(64,64))
Image_Wall= pygame.transform.scale(Image_Wall,(64,64))
#Read1 Image Unit Done
#Read Map Unit
Game_Map = [];
Map_Wide = 0
Map_Deepth = 0

def Map_Reader(Mission):
    File_Name ="map/"+ str(Mission+1) +'.dat'
    file = open(File_Name,'r')
    
for Mission in range(3):
    pygame.display.set_caption("Mission "+str(Mission))

