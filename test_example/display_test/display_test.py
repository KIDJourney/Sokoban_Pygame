#!/usr/bin/env python
# coding=utf-8
import pygame
import time
pygame.init()
size = [120,120]
screen = pygame.display.set_mode(size,0,32)
while True:
    size = (size[0]+1,size[1]+1)
    screen = pygame.display.set_mode((size),0,32)
    pygame.display.update()
    if size[0]>2000:
        break
