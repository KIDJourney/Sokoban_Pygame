#!/usr/bin/env python
# coding=utf-8
import pygame
from pygame.locals import *
#Globle Var
Game_Level = 1
Game_Map = list()
Map_Wide = 0
Map_Deepth = 0
def ReadMap():
    global Game_Map
    FileName = str(Game_Level)+".dat"
    file = open(FileName,'r')
    Map_Deepth,Map_Wide = map(int,file.readline().split())
    for i in range(Map_Deepth):
        Game_Map.append(file.readline()[:Map_Wide-1])
ReadMap()
if Game_Map[0][0]=='D':
    print "Yes"
