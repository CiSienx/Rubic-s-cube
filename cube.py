from vpython import *
import numpy as np
import random
from solve_rubiccs_cube import *

class Rubic_Cube():
    def __init__(self):
        self.running = True
        self.tiles = []
        self.dA = np.pi/40
        #center
        sphere(pos=vector(0,0,0),size=vector(3,3,3),color=vector(0,0,0))
        tile_pos = [[vector(-1, 1, 1.5),vector(0, 1, 1.5),vector(1, 1, 1.5),           #front
                     vector(-1, 0, 1.5),vector(0, 0, 1.5),vector(1, 0, 1.5),
                     vector(-1, -1, 1.5),vector(0, -1, 1.5),vector(1, -1, 1.5), ],
                    [vector(1.5, 1, -1), vector(1.5, 1, 0), vector(1.5, 1, 1),         # right
                     vector(1.5, 0, -1), vector(1.5, 0, 0), vector(1.5, 0, 1),
                     vector(1.5, -1, -1), vector(1.5, -1, 0), vector(1.5, -1, 1), ],
                    [vector(-1, 1, -1.5), vector(0, 1, -1.5), vector(1, 1, -1.5),       # back
                     vector(-1, 0, -1.5), vector(0, 0, -1.5), vector(1, 0, -1.5),
                     vector(-1, -1, -1.5), vector(0, -1, -1.5), vector(1, -1, -1.5), ],
                    [vector(-1.5, 1, -1), vector(-1.5, 1, 0), vector(-1.5, 1, 1),          # left
                     vector(-1.5, 0, -1), vector(-1.5, 0, 0), vector(-1.5, 0, 1),
                     vector(-1.5, -1, -1), vector(-1.5, -1, 0), vector(-1.5, -1, 1), ],
                    [vector(-1, 1.5, -1), vector(0, 1.5, -1), vector(1, 1.5, -1),          # top
                     vector(-1, 1.5, 0), vector(0, 1.5, 0), vector(1, 1.5, 0),
                     vector(-1, 1.5, 1), vector(0, 1.5, 1), vector(1, 1.5, 1), ],
                    [vector(-1, -1.5, -1), vector(0, -1.5, -1), vector(1, -1.5, -1),          # bottom
                     vector(-1, -1.5, 0), vector(0, -1.5, 0), vector(1, -1.5, 0),
                     vector(-1, -1.5, 1), vector(0, -1.5, 1), vector(1, -1.5, 1), ],
                    ]
        colors = [vector(1,0,0),vector(1,1,0),vector(1,0.5,0),vector(1,1,1),vector(0,0,1),vector(0,1,0)]
        angle = [(0,vector(0,0,0)),(np.pi/2,vector(0,1,0)),(0,vector(0,0,0)),(np.pi/2,vector(0,1,0)),(np.pi/2,vector(1,0,0)),(np.pi/2,vector(1,0,0))]
        #sides
        for rank,side in enumerate(tile_pos):
            for vec in side:
                tile = box(pos=vec,size=vector(0.98,0.98,0.1),color=colors[rank])
                tile.rotate(angle = angle[rank][0],axis=angle[rank][1])
                self.tiles.append(tile)
        #positions
        self.positions = {'front':[],'right':[],'back':[],'left':[],'top':[],'bottom':[]}
        #variables
        self.rotate = [None,0,0]
        self.moves = []
    def reset_positions(self):
        self.positions = {'front': [], 'right': [], 'back': [], 'left': [], 'top': [], 'bottom': []}
        for tile in self.tiles:
            if tile.pos.z > 0.4:
                self.positions['front'].append(tile)
            if tile.pos.x > 0.4:
                self.positions['right'].append(tile)
            if tile.pos.z < -0.4:
                self.positions['back'].append(tile)
            if tile.pos.x < -0.4:
                self.positions['left'].append(tile)
            if tile.pos.y > 0.4:
                self.positions['top'].append(tile)
            if tile.pos.y < -0.4:
                self.positions['bottom'].append(tile)
        for key in self.positions.keys():
            self.positions[key] = set(self.positions[key])
    def animations(self):
        if self.rotate[0] == 'front_counter' :
            pieces = self.positions['front']
            for tile in pieces:
                tile.rotate(angle=(self.dA),axis = vector(0,0,1),origin=vector(0,0,0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'right_counter' :
            pieces = self.positions['right']
            for tile in pieces:
                tile.rotate(angle=(self.dA),axis = vector(1,0,0),origin=vector(0,0,0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'back_counter' :
            pieces = self.positions['back']
            for tile in pieces:
                tile.rotate(angle=(self.dA),axis = vector(0,0,-1),origin=vector(0,0,0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'left_counter' :
            pieces = self.positions['left']
            for tile in pieces:
                tile.rotate(angle=(self.dA),axis = vector(-1,0,0),origin=vector(0,0,0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'top_counter' :
            pieces = self.positions['top']
            for tile in pieces:
                tile.rotate(angle=(self.dA),axis = vector(0,1,0),origin=vector(0,0,0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'bottom_counter' :
            pieces = self.positions['bottom']
            for tile in pieces:
                tile.rotate(angle=(self.dA),axis = vector(0,-1,0),origin=vector(0,0,0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'front_clock' :
            pieces = self.positions['front']
            for tile in pieces:
                tile.rotate(angle=(-self.dA),axis = vector(0,0,1),origin=vector(0,0,0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'right_clock' :
            pieces = self.positions['right']
            for tile in pieces:
                tile.rotate(angle=(-self.dA),axis = vector(1,0,0),origin=vector(0,0,0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'back_clock' :
            pieces = self.positions['back']
            for tile in pieces:
                tile.rotate(angle=(-self.dA),axis = vector(0,0,-1),origin=vector(0,0,0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'left_clock' :
            pieces = self.positions['left']
            for tile in pieces:
                tile.rotate(angle=(-self.dA),axis = vector(-1,0,0),origin=vector(0,0,0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'top_clock' :
            pieces = self.positions['top']
            for tile in pieces:
                tile.rotate(angle=(-self.dA),axis = vector(0,1,0),origin=vector(0,0,0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'bottom_clock' :
            pieces = self.positions['bottom']
            for tile in pieces:
                tile.rotate(angle=(-self.dA),axis = vector(0,-1,0),origin=vector(0,0,0))
            self.rotate[1] += self.dA
        if self.rotate[1] + self.dA/2 > self.rotate[2] and \
            self.rotate[1] - self.dA/2 < self.rotate[2]:
            self.rotate = [None,0,0]
            self.reset_positions()
    def rotate_front_counter(self):
        if self.rotate[0] == None:
            self.rotate = ['front_counter',0,np.pi/2]
    def rotate_right_counter(self):
        if self.rotate[0] == None:
            self.rotate = ['right_counter',0,np.pi/2]
    def rotate_back_counter(self):
        if self.rotate[0] == None:
            self.rotate = ['back_counter',0,np.pi/2]
    def rotate_left_counter(self):
        if self.rotate[0] == None:
            self.rotate = ['left_counter',0,np.pi/2]
    def rotate_top_counter(self):
        if self.rotate[0] == None:
            self.rotate = ['top_counter',0,np.pi/2]
    def rotate_bottom_counter(self):
        if self.rotate[0] == None:
            self.rotate = ['bottom_counter',0,np.pi/2]
    def rotate_front_clock(self):
        if self.rotate[0] == None:
            self.rotate = ['front_clock',0,np.pi/2]
    def rotate_right_clock(self):
        if self.rotate[0] == None:
            self.rotate = ['right_clock',0,np.pi/2]
    def rotate_back_clock(self):
        if self.rotate[0] == None:
            self.rotate = ['back_clock',0,np.pi/2]
    def rotate_left_clock(self):
        if self.rotate[0] == None:
            self.rotate = ['left_clock',0,np.pi/2]
    def rotate_top_clock(self):
        if self.rotate[0] == None:
            self.rotate = ['top_clock',0,np.pi/2]
    def rotate_bottom_clock(self):
        if self.rotate[0] == None:
            self.rotate = ['bottom_clock',0,np.pi/2]
    def move(self):
        possible_moves = ["F", "R", "B", "L", "U", "D", "F'", "R'", "B'", "L'", "U'", "D'"]
        if self.rotate[0] == None and len(self.moves) > 0:
            if self.moves[0] == possible_moves[0]:
                self.rotate_front_clock()
            elif self.moves[0] == possible_moves[1]:
                self.rotate_right_clock()
            elif self.moves[0] == possible_moves[2]:
                self.rotate_back_clock()
            elif self.moves[0] == possible_moves[3]:
                self.rotate_left_clock()
            elif self.moves[0] == possible_moves[4]:
                self.rotate_top_clock()
            elif self.moves[0] == possible_moves[5]:
                self.rotate_bottom_clock()
            elif self.moves[0] == possible_moves[6]:
                self.rotate_front_counter()
            elif self.moves[0] == possible_moves[7]:
                self.rotate_right_counter()
            elif self.moves[0] == possible_moves[8]:
                self.rotate_back_counter()
            elif self.moves[0] == possible_moves[9]:
                self.rotate_left_counter()
            elif self.moves[0] == possible_moves[10]:
                self.rotate_top_counter()
            elif self.moves[0] == possible_moves[11]:
                self.rotate_bottom_counter()
            self.moves.pop(0)
    def scramble(self):
        possible_moves = ["F","R","B","L","U","D","F'","R'","B'","L'","U'","D'"]
        for i in range(25):
            self.moves.append(random.choice(possible_moves))
    def solution(self):
        solve(self.tiles)
    def solve(self):
        values = solve(self.tiles)
        values = list(values.split(" "))
        for value in values:
            lis_value = list(value)
            if lis_value[-1] == '2':
                lis_value.pop(-1)
                value = ''.join(lis_value)
                self.moves.append(value)
                self.moves.append(value)
            else:
                self.moves.append(value)
    def control(self):
        button(bind=self.rotate_front_clock, text='F')
        button(bind=self.rotate_front_counter,text="F'")
        button(bind=self.rotate_right_clock, text='R')
        button(bind=self.rotate_right_counter, text="R'")
        button(bind=self.rotate_back_clock, text='B')
        button(bind=self.rotate_back_counter, text="B'")
        button(bind=self.rotate_left_clock, text='L')
        button(bind=self.rotate_left_counter, text="L'")
        button(bind=self.rotate_top_clock, text='U')
        button(bind=self.rotate_top_counter, text="U'")
        button(bind=self.rotate_bottom_clock, text='D')
        button(bind=self.rotate_bottom_counter, text="D'")
        button(bind=self.scramble, text='random_move')
        button(bind=self.solution, text='solution')
        button(bind=self.solve, text='solve it!')
    def update(self):
        rate(60)
        self.animations()
        self.move()
    def start(self):
        self.reset_positions()
        self.control()
        while self.running:
            self.update()