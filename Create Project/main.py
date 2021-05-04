import pygame
from chess.constants import WIDTH, HEIGHT
from chess.board import Board

FPS = 30

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            #For exiting the game
            if event.type == pygame.QUIT:
                run = False

            #For clicking on screen
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        
        board.draw(WIN)
        pygame.display.update()

    pygame.quit()

main()