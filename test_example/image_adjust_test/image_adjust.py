#!/usr/bin/env python
# coding=utf-8
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480),0,28)
screen.fill((0,0,0))
test_image = pygame.image.load("image/test.jpg").convert()
test_image = pygame.transform.scale(test_image,(64,64))
while True:
    screen.blit(test_image,(0,0))
    pygame.display.update()
