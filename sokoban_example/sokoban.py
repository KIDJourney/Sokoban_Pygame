import pygame, sys, os
from pygame.locals import *

from collections import deque

def to_box(level, index):
    if level[index] == '-' or level[index] == '@':
        level[index] = '$'
    else:
        level[index] = '*'

def to_man(level, i):
    if level[i] == '-' or level[i] == '$':
        level[i]='@'
    else:
        level[i]='+'

def to_floor(level, i):
    if level[i] == '@' or level[i] == '$':
        level[i]='-'
    else:
        level[i]='.'

def to_offset(d, width):
    d4 = [-1, -width, 1, width]
    m4 = ['l','u','r','d']
    return d4[m4.index(d.lower())]

def b_manto(level,width,b,m,t):
    maze = list(level)
    maze[b] = '#'
    if m == t:
        return 1
    queue = deque([])
    queue.append(m)
    d4 = [-1, -width, 1, width]
    m4 = ['l','u','r','d']
    while len(queue) > 0:
        pos = queue.popleft()
        for i in range(4):
            newpos = pos + d4[i]
            if maze[newpos] in ['-','.']:
                if newpos == t:
                    return 1
                maze[newpos] = i
                queue.append(newpos)
    return 0

def b_manto_2(level,width,b,m,t):
    maze = list(level)
    maze[b] = '#'
    maze[m] = '@'
    if m == t:
        return []
    queue = deque([])
    queue.append(m)
    d4 = [-1, -width, 1, width]
    m4 = ['l','u','r','d']
    while len(queue) > 0:
        pos = queue.popleft()
        for i in range(4):
            newpos = pos + d4[i]
            if maze[newpos] in ['-','.']:
                maze[newpos] = i
                queue.append(newpos)
                if newpos == t:
                    path = []
                    while maze[t] != '@':
                        path.append( m4[maze[t]])
                        t = t - d4[maze[t]]
                    return path
                
    return []



    
	
class Sokoban:
    def __init__(self):
        self.level = list('----#####--------------#---#--------------#$--#------------###--$##-----------#--$-$-#---------###-#-##-#---#######---#-##-#####--..##-$--$----------..######-###-#@##--..#----#-----#########----#######--------')
        self.w = 19
        self.h = 11
        self.man = 163
        self.hint = list(self.level)
        self.solution = []
        self.push = 0
        self.todo = []
        self.auto = 0
        self.sbox = 0
        self.queue = []
    def draw(self, screen, skin):
        w = skin.get_width() / 4
        offset = (w-4)/2
        for i in range(0,self.w):
            for j in range(0,self.h):
                if self.level[j*self.w + i] == '#':
                    screen.blit(skin, (i*w, j*w), (0,2*w,w,w))
                elif self.level[j*self.w + i] == '-':
                    screen.blit(skin, (i*w, j*w), (0,0,w,w))
                elif self.level[j*self.w + i] == '@':
                    screen.blit(skin, (i*w, j*w), (w,0,w,w))
                elif self.level[j*self.w + i] == '$':
                    screen.blit(skin, (i*w, j*w), (2*w,0,w,w))
                elif self.level[j*self.w + i] == '.':
                    screen.blit(skin, (i*w, j*w), (0,w,w,w))
                elif self.level[j*self.w + i] == '+':
                    screen.blit(skin, (i*w, j*w), (w,w,w,w))
                elif self.level[j*self.w + i] == '*':
                    screen.blit(skin, (i*w, j*w), (2*w,w,w,w))
                if self.sbox != 0 and self.hint[j*self.w+i]=='1':
                    screen.blit(skin,  (i*w+offset, j*w+offset), (3*w, 3*w, 4, 4))
    def move(self, d):
        self._move(d)
        self.todo = []
    def _move(self, d):
        self.sbox = 0
        h = to_offset(d, self.w)
        h2 = 2 * h
        if self.level[self.man + h] == '-' or self.level[self.man + h] == '.':
        # move
            to_man(self.level, self.man+h)
            to_floor(self.level, self.man)
            self.man += h
            self.solution += d
        elif self.level[self.man + h] == '*' or self.level[self.man + h] == '$':
            if self.level[self.man + h2] == '-' or self.level[self.man + h2] == '.':
            # push
                to_box(self.level, self.man + h2)
                to_man(self.level, self.man + h)
                to_floor(self.level, self.man)
                self.man += h
                self.solution += d.upper()
                self.push += 1
    def undo(self):
        if self.solution.__len__()>0:
            self.todo.append(self.solution[-1])
            self.solution.pop()
            
            h = to_offset(self.todo[-1],self.w) * -1
            if self.todo[-1].islower():
            #undo a move
                to_man(self.level, self.man + h)
                to_floor(self.level, self.man)
                self.man += h
            else:
            # undo a push
                to_floor(self.level, self.man - h)
                to_box(self.level, self.man)
                to_man(self.level, self.man + h)
                self.man += h
                self.push -= 1
    def redo(self):
        if self.todo.__len__()>0:
            self._move(self.todo[-1].lower())
            self.todo.pop()
    def manto(self, x, y):
        maze = list(self.level)
        maze[self.man] = '@'
        queue = deque([])
        queue.append(self.man)
        d4 = [-1, -self.w, 1, self.w]
        m4 = ['l','u','r','d']
        while len(queue) > 0:
            pos = queue.popleft()
            for i in range(4):
                newpos = pos + d4[i]
                if maze[newpos] in ['-','.']:
                    maze[newpos] = i
                    queue.append(newpos)
        #print str(maze)
        t = y * self.w + x
        if maze[t] in range(4):
            self.todo = []
            while maze[t] != '@':
                self.todo.append( m4[maze[t]])
                t = t - d4[maze[t]]
        #print self.todo
        self.auto = 1
    def automove(self):
        if self.auto == 1 and self.todo.__len__()>0:
            self._move(self.todo[-1].lower())
            self.todo.pop()
        else:
            self.auto = 0
    def boxhint(self,x,y):
        d4 = [-1, -self.w, 1, self.w]
        m4 = ['l','u','r','d']
        b = y * self.w + x
        maze = list(self.level)
        to_floor(maze,b)
        to_floor(maze, self.man)
        mark = maze * 4
        size = self.w * self.h
        self.queue = []
        head = 0
        for i in range(4):
            if b_manto(maze, self.w, b, self.man, b+d4[i]):
                if len(self.queue) == 0:
                    self.queue.append((b,i,-1))
                mark[ i*size + b ]='1'
        #print self.queue
        while head < len(self.queue):
            pos = self.queue[head]
            head += 1
            #print pos
            for i in range(4):
                if mark[ pos[0] + i*size ] == '1' and maze[ pos[0] - d4[i] ] in ['-','.']:
                    #print i
                    if mark[ pos[0]-d4[i] + i*size ] != '1' :
                        self.queue.append((pos[0]-d4[i],i,head - 1))
                        for j in range(4):
                            if b_manto(maze, self.w, pos[0]-d4[i], pos[0], pos[0]-d4[i]+d4[j]):
                                mark[ j*size + pos[0]-d4[i] ] = '1'
        for i in range(size):
            self.hint[i] = '0'
            for j in range(4):
                if mark[j*size+i] == '1':
                    self.hint[i] = '1'
        #print self.hint
    def boxto(self,x,y):
        d4 = [-1, -self.w, 1, self.w]
        m4 = ['l','u','r','d']
        om4 = ['r','d','l','u']
        b = y * self.w + x
        maze = list(self.level)
        to_floor(maze, self.sbox)
        to_floor(maze, self.man) # make a copy of working maze by removing the selected box and the man
        for i in range(len(self.queue)):
            if self.queue[i][0] == b:
                self.todo = []
                j = i
                while self.queue[j][2] != -1:
                    self.todo.append( om4[self.queue[j][1]].upper() )
                    k = self.queue[j][2]
                    if self.queue[k][2] != -1:
                        self.todo += b_manto_2(maze, self.w, self.queue[k][0], self.queue[k][0]+d4[self.queue[k][1]], self.queue[k][0]+d4[self.queue[j][1]])
                    else:
                        self.todo += b_manto_2(maze, self.w, self.queue[k][0], self.man, self.queue[k][0]+d4[self.queue[j][1]])
                    j = k
                #print self.todo
                self.auto = 1
                return    
        print 'not found!'


    def mouse(self,x,y):
        if x >= self.w or y >= self.h:
            return
        m = y * self.w + x
        if self.level[m] in ['-','.']:
            if self.sbox == 0:
                self.manto(x,y)
            else:
                self.boxto(x,y)
        elif self.level[m] in ['$','*']:
            if self.sbox == m:
                self.sbox = 0
            else:
                self.sbox = m
                self.boxhint(x,y)
        elif self.level[m] in ['-','.','@','+']:
            self.boxto(x,y)
        
            

def main():

    # start pygame
    pygame.init()
    screen = pygame.display.set_mode((400,300))


    # load skin
    skinfilename = os.path.join('borgar.png')
    try:
        skin = pygame.image.load(skinfilename)
    except pygame.error, msg:
        print 'cannot load skin'
        raise SystemExit, msg
    skin = skin.convert()

    #print skin.get_at((0,0))
    #screen.fill((255,255,255))
    screen.fill(skin.get_at((0,0)))
    pygame.display.set_caption('sokoban.py')

    # create Sokoban object
    skb = Sokoban()
    skb.draw(screen,skin)

    #
    clock = pygame.time.Clock()
    pygame.key.set_repeat(200,50)

    # main game loop
    while True:
        clock.tick(60)

        if skb.auto == 0:
            for event in pygame.event.get():
                if event.type == QUIT:
                    #print skb.solution
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        skb.move('l')
                        skb.draw(screen,skin)
                    elif event.key == K_UP:
                        skb.move('u')
                        skb.draw(screen,skin)
                    elif event.key == K_RIGHT:
                        skb.move('r')
                        skb.draw(screen,skin)
                    elif event.key == K_DOWN:
                        skb.move('d')
                        skb.draw(screen,skin)
                    elif event.key == K_BACKSPACE:
                        skb.undo()
                        skb.draw(screen,skin)
                    elif event.key == K_SPACE:
                        skb.redo()
                        skb.draw(screen,skin)
                elif event.type == MOUSEBUTTONUP and event.button == 1:
                    mousex, mousey = event.pos
                    mousex /= (skin.get_width() / 4)
                    mousey /= (skin.get_width() / 4)
                    skb.mouse(mousex, mousey)
                    skb.draw(screen, skin)
        else:
            skb.automove()
            skb.draw(screen, skin)

        pygame.display.update()
        pygame.display.set_caption(skb.solution.__len__().__str__() + '/' + skb.push.__str__() + ' - sokoban.py')


if __name__ == '__main__':
    main()
