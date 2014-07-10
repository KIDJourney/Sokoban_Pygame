#!/usr/bin/env python
# coding=utf-8
import Load_Unit
import pygame
#W==Wall B==BOX P==Player G=goal N=NULL
def Draw_Map(self,screen):
    for i in range(Load_Unit.Map_Deepth):
        for j in range(Load_Unit.Map_Wide):
            if Load_Unit.Game_Map[i][j]=='W':
                screen.blit(Load_Unit.Image_Wall)
