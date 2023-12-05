import pygame, sys
from board import Board
from Button import Button

SCREEN_WIDTH = 550
SCREEN_HEIGHT = 600

PATH = "C:/Users/Aaron/OneDrive/Documents/UF/COP3502C/Sudoku-Project/images"

def draw_game_start(screen):
    #background
    bg = pygame.image.load(f"{PATH}/backgroundimage.jpg")
    screen.blit(bg, (0, 0))

    #draw title
    font = pygame.font.SysFont('arial_bold', 60)
    title = font.render('SUDOKU', True, (255, 255, 255))
    screen.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, SCREEN_WIDTH / 2 - title.get_height()))

    #draw difficulty button
    easy_img = pygame.image.load(f"{PATH}/easy.png").convert_alpha()
    medium_img = pygame.image.load(f"{PATH}/medium.png").convert_alpha()
    hard_img = pygame.image.load(f"{PATH}/hard.png").convert_alpha()
    easy_button = Button(75, 360, easy_img, 0.2)
    medium_button = Button(225, 360, medium_img, 0.2)
    hard_button = Button(375, 360, hard_img, 0.2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if easy_button.draw(screen):
                return(30)
            if medium_button.draw(screen):
                return(40)
            if hard_button.draw(screen):
                return(50)
        pygame.display.update()    

if __name__ == '__main__':
    game_over = False

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sudoku game")

    difficulty = draw_game_start(screen)

    screen.fill((251, 247, 245))
    board = Board(9, 9, screen, difficulty)
    board.draw()

    pygame.display.update()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
