#!/usr/bin/env python
# coding=utf-8
import pygame
import Load_Unit
from pygame.locals import *
#Globle Var
#W==Wall
#B==BOX
#P==Player
#G=goal
#N=NULL
#Game_Screen = pygame.surface.surfa




def MapRefresh():
    pass
if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((Load_Unit.Map_Wide,Load_Unit.Map_Deepth),0,28)

    Load_Unit.ReadMap()
    Load_Unit.ImageLoad()
    
