import pygame
from .constants import WHITE, BLACK, SQUARE_SIZE, BLACK_KNIGHT, WHITE_KNIGHT

class Knight:
    def __init__(self,row,col,color):
        self.row = row
        self.col = col
        self.color = color
        
        self.x = 0
        self.y = 0
        self.position()
    
    def position(self):
        self.x = SQUARE_SIZE * self.col + 10
        self.y = SQUARE_SIZE * self.row + 10
        
    def draw(self, win):
        if self.color == WHITE:
            win.blit(WHITE_KNIGHT, (self.x, self.y))
        else:
            win.blit(BLACK_KNIGHT, (self.x, self.y))