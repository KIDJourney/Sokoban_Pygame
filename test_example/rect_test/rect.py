#!/usr/bin/env python
# coding=utf-8
import pygame
pygame.init()
myrect = pygame.rect.Rect(0,0,1024,768)
print myrect.collidepoint(768,1024)
