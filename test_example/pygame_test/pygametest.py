#!/usr/bin/env python
# coding=utf-8
import pygame
pygame.init()
screen = pygame.display.set_mode((760,600),0,32)
while (1):
    for i in pygame.event.get():
        print i
