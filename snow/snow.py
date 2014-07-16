#!/usr/bin/env python
# coding=utf-8
import pygame
from pygame.locals import *
import random
import sys
pygame.init()

class snow():
    def __init__(self,tpos,tspeed):
        self.speed = tspeed
        self.pos = tpos
    def move(self):
        self.pos[1]+=self.speed
    def check(self):
        if self.pos[1]>size[1]:
            self.pos[1] = random.randrange(-50,-10)
            self.pos[0] = random.randrange(0,size[0])
    def getpos(self):
        return self.pos

black = (0,0,0)
white = (255,255,255)

size  = (1024,768)
screen = pygame.display.set_mode(size,0,32)
star_list =[]

for i in range(50):
    x = random.randrange(0,size[0])
    y = random.randrange(0,size[0])
    star_list.append(snow([x,y],random.randrange(0,10)))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    
    screen.fill(black)
    for i in range(len(star_list)):
        pygame.draw.circle(screen,white,star_list[i].getpos(),2)
        star_list[i].move()
        star_list[i].check()

    pygame.display.flip()
    clock.tick(20)


