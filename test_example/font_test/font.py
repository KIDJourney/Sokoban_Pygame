#!/usr/bin/env python
# coding=utf-8
import pygame
pygame.init()
screen = pygame.display.set_mode((1024,768),0,32)
font = pygame.font.SysFont("arial",16)
while True:
    screen.blit(font.render("hi",True,(255,0,0)),(0,0))
    pygame.display.update()
