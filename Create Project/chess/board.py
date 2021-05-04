import pygame
from .constants import BLACK, ROWS, COLS, WHITE, SQUARE_SIZE, DARK_TAN, LIGHT_TAN
from .bishop import Bishop
from .king import King
from .knight import Knight
from .pawn import Pawn
from .queen import Queen
from .rook import Rook

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.place_pieces()

    def draw_checkerboard(self, win):
        win.fill(DARK_TAN)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, LIGHT_TAN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def place_pieces(self):
        self.board.append([])
        self.board[0].append(Rook(0, 0, BLACK))
        self.board[0].append(Knight(0, 1, BLACK))
        self.board[0].append(Bishop(0, 2, BLACK))
        self.board[0].append(Queen(0, 3, BLACK))
        self.board[0].append(King(0, 4, BLACK))
        self.board[0].append(Bishop(0, 5, BLACK))
        self.board[0].append(Knight(0, 6, BLACK))
        self.board[0].append(Rook(0, 7, BLACK))
        self.board.append([])
        for x in range(8):
            self.board[1].append(Pawn(1, x, BLACK))
        for y in range(4):
            self.board.append([])
            for x in range(8):
                self.board[y+2].append(0)
        self.board.append([])
        for x in range(8):
            self.board[6].append(Pawn(6, x, WHITE))
        self.board.append([])
        self.board[7].append(Rook(7, 0, WHITE))
        self.board[7].append(Knight(7, 1, WHITE))
        self.board[7].append(Bishop(7, 2, WHITE))
        self.board[7].append(Queen(7, 3, WHITE))
        self.board[7].append(King(7, 4, WHITE))
        self.board[7].append(Bishop(7, 5, WHITE))
        self.board[7].append(Knight(7, 6, WHITE))
        self.board[7].append(Rook(7, 7, WHITE))
    
    def draw(self, win):
        self.draw_checkerboard(win)
        for y in range(ROWS):
            for x in range(COLS):
                piece_loc = self.board[y][x]
                if piece_loc != 0:
                    piece_loc.draw(win)

