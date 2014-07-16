#!/usr/bin/env python
# coding=utf-8
import pygame
from pygame.locals import *
from random import randrange
from sys import exit
pygame.init()
screen_size = (1024,768)
screen = pygame.display.set_mode(screen_size,0,32)
screen_rect  = pygame.rect.Rect((0,0),screen_size)
class point():
    def __init__(self,tpos,tspeed):
        self.pos = tpos
        self.speed = tspeed
        self.color = (randrange(0,255),randrange(0,255),randrange(0,255))
    def move(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
        self.color = (randrange(0,255),randrange(0,255),randrange(0,255))
    def getpos(self):
        return self.pos
    def getcolor(self):
        return self.color
    def check(self):
        return screen_rect.collidepoint(self.pos)

star_list = []
clock = pygame.time.Clock()

backgroud = (0,0,0)
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            eixt()
    screen.fill(backgroud)

    for i in range(randrange(1,10)):
        if len(star_list) > 50:
            break
        pos = [screen_size[0]/2,screen_size[1]/2]
        speed =[randrange(-10,10),randrange(-10,10)]
        while speed[0]==0 and speed[1]==0:
            speed[0]=randrange(-10,10)
            speed[0]=randrange(-10,10)
        star_list.append(point(pos,speed))
        
    for i in range(len(star_list)):
        if i < len(star_list):
            pygame.draw.circle(screen,star_list[i].getcolor(),star_list[i].getpos(),50)
            star_list[i].move()
            if not star_list[i].check():
                del star_list[i]
                i-=1
    pygame.display.flip()
    clock.tick(20)
    


