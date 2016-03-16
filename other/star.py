from functools import reduce
import time
import pygame
import random
import math


def show_star(screen, star):
    points = []
    for i in range(len(star.Bpoints)):
        points.append(star.Bpoints[i])
        points.append(star.Spoints[i])


    def draw_line(point1, point2):
        pygame.draw.line(screen, star.color , point1, point2, 1)
        return point2


    reduce(draw_line, points, points[-1])


def sin(degree):
    return math.sin(math.radians(degree))


def cos(degree):
    return math.cos(math.radians(degree))


class Star:
    def __init__(self, screen_size):
        self.k = min(0.7,(max(0.3,random.random())))
        self.pos = [
            random.randint(screen_size[0] * 0.1, screen_size[0] * 0.9), random.randint(screen_size[1] * 0.1, screen_size[1] * 0.9)]
        
        self.color = (0 , 0 , 0)

        self.angel = 0
        self.r = random.randint(screen_size[0] * 0.05, screen_size[0] * 0.1)
        self.speed = [
            random.randint(-self.r, self.r), random.randint(-self.r, self.r)]
        self.aspeed = random.choice([-random.random() , random.random()])

        self.screen_size = screen_size
        self.Bpoints = []
        self.Spoints = []

        self.flush_points()

    def flush_points(self):
        self.Bpoints = []
        self.Spoints = []

        for i in range(5):
            point_pos = (
                self.r * cos(72 * i + self.angel), self.r * sin(72 * i + self.angel))
            point_pos = (
                point_pos[0] + self.pos[0], point_pos[1] + self.pos[1])
            self.Bpoints.append(point_pos)

        for index, value in enumerate(self.Bpoints):
            mid_point = ((self.Bpoints[index][0] + self.Bpoints[(index + 1) % len(self.Bpoints)][
                         0]) / 2, (self.Bpoints[index][1] + self.Bpoints[(index + 1) % len(self.Bpoints)][1]) / 2)

            goal_point = (mid_point[0] + (self.pos[0] - mid_point[0]) *
                          self.k, mid_point[1] + (self.pos[1] - mid_point[1]) * self.k)

            self.Spoints.append(goal_point)

    def move(self,t):
        self.pos[0], self.pos[1] = self.pos[0] + \
            self.speed[0] * t, self.pos[1] + self.speed[1] * t
        self.angel += self.aspeed

        self.flush_points()

        self.color = tuple(map(lambda x : max(0 , (min(255 , x + random.randint(-5,5)))) , self.color))

    def is_out(self):
        if max(0 - self.pos[0] , self.pos[0] - self.screen_size[0]) >= self.r:
            return True
        if max(0 - self.pos[1] , self.pos[1] - self.screen_size[1]) >= self.r:
            return True

        return False

if __name__ == "__main__":
    screen_size = ((1080 , 1080))

    time_clock = 0.01

    max_stars = 100
    pygame.init()
    screen = pygame.display.set_mode(screen_size, 0, 32)
    stars = [Star(screen_size) for i in range(max_stars)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill((0, 0, 0))

        for star in stars:
            star.move(time_clock)

        for star in stars:
            show_star(screen, star)

        stars = [star for star in stars if not star.is_out()]

        stars += [Star(screen_size) for i in range(max_stars - len(stars))]

        pygame.display.update()

        time.sleep(time_clock)
