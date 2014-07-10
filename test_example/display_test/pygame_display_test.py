#!/usr/bin/env python
# coding=utf-8
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480),0,28)
color = (255,255,255)
while True:
    for  i in range(0,640,64):
        pygame.draw.rect(screen,color,(i,64,64,64))
        if (color==(0,0,0)):
            color = (255,255,255)
        else:
            color = (0,0,0)
    pygame.display.update()
