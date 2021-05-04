import pygame
from .constants import WHITE, BLACK, SQUARE_SIZE, BLACK_PAWN, WHITE_PAWN

class Pawn:
    def __init__(self,row,col,color):
        self.row = row
        self.col = col
        self.color = color
        self.has_moved = False
        self.just_moved_two = False
        
        if self.color == WHITE:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.position()
    
    # x/y pos based on location in array
    def position(self):
        self.x = SQUARE_SIZE * self.col + 15
        self.y = SQUARE_SIZE * self.row + 15
    
    # load png asset for piece on screen, at x/y, for proper color
    def draw(self, win):
        if self.color == WHITE:
            win.blit(WHITE_PAWN, (self.x, self.y))
        else:
            win.blit(BLACK_PAWN, (self.x, self.y))
                
    def move_piece(self, row, col):
        self.row = row
        self.col = col
        self.position()