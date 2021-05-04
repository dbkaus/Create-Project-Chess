import pygame
from chess.constants import WIDTH, HEIGHT, SQUARE_SIZE
from chess.board import Board

FPS = 30

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')

def return_row_col_of_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    active_click = 0

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            #For exiting the game
            if event.type == pygame.QUIT:
                run = False

            #For clicking on screen
            if event.type == pygame.MOUSEBUTTONDOWN:
                if active_click == 1:
                    pos = pygame.mouse.get_pos()
                    row, col = return_row_col_of_mouse(pos)
                    board.move_piece(piece, row, col)
                    active_click = 0
                else:
                    pos = pygame.mouse.get_pos()
                    row, col = return_row_col_of_mouse(pos)
                    piece = board.return_piece(row, col)
                    if piece != 0:
                        active_click = 1

                
        
        board.draw(WIN)
        pygame.display.update()

    pygame.quit()

main()