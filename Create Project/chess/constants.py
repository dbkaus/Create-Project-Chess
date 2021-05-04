import pygame

#board size
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

#rgb colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREY = (192, 192, 192)
DARK_TAN = (195, 155, 119)
LIGHT_TAN = (229, 211, 180)

WHITE_PAWN = pygame.transform.scale(pygame.image.load('assets/white_pawn.png'), (70, 70))
BLACK_PAWN = pygame.transform.scale(pygame.image.load('assets/black_pawn.png'), (70, 70))
WHITE_BISHOP = pygame.transform.scale(pygame.image.load('assets/white_bishop.png'), (70, 70))
BLACK_BISHOP = pygame.transform.scale(pygame.image.load('assets/black_bishop.png'), (70, 70))
WHITE_KNIGHT = pygame.transform.scale(pygame.image.load('assets/white_knight.png'), (70, 70))
BLACK_KNIGHT = pygame.transform.scale(pygame.image.load('assets/black_knight.png'), (70, 70))
WHITE_ROOK = pygame.transform.scale(pygame.image.load('assets/white_rook.png'), (70, 70))
BLACK_ROOK = pygame.transform.scale(pygame.image.load('assets/black_rook.png'), (70, 70))
WHITE_QUEEN = pygame.transform.scale(pygame.image.load('assets/white_queen.png'), (70, 70))
BLACK_QUEEN = pygame.transform.scale(pygame.image.load('assets/black_queen.png'), (70, 70))
WHITE_KING = pygame.transform.scale(pygame.image.load('assets/white_king.png'), (70, 70))
BLACK_KING = pygame.transform.scale(pygame.image.load('assets/black_king.png'), (70, 70))