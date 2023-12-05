import pygame, sys
from board import Board
from Button import Button

SCREEN_WIDTH = 550
SCREEN_HEIGHT = 600

PATH = r"C:\Users\jimin\개개비\SUDOKU\Sudoku-Project\images"

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

def draw_game_menu(screen, board):
    board.draw()
    reset_img = pygame.image.load(f"{PATH}/reset.png").convert_alpha()
    restart_img = pygame.image.load(f"{PATH}/restart.png").convert_alpha()
    exit_img = pygame.image.load(f"{PATH}/exit.png").convert_alpha()
    reset_button = Button(80, 510, reset_img, 0.15)
    restart_button = Button(235, 510, restart_img, 0.15)
    exit_button = Button(390, 510, exit_img, 0.15)
    lose_statement = True
    while True:
        if board.is_full() and lose_statement:
            print(board.check_board())
            lose_statement = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_row = int(event.pos[1])
                clicked_col = int(event.pos[0])
                if board.click(clicked_row, clicked_col) != None:
                    screen.fill((251, 247, 245))
                    board.draw()
                    reset_button = Button(80, 510, reset_img, 0.15)
                    restart_button = Button(235, 510, restart_img, 0.15)
                    exit_button = Button(390, 510, exit_img, 0.15)
                    board.select((clicked_row-50)//50+1, (clicked_col-50)//50+1)
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_1:
                        board.sketch(1)
                    case pygame.K_2:
                        board.sketch(2)
                    case pygame.K_3:
                        board.sketch(3)
                    case pygame.K_4:
                        board.sketch(4)
                    case pygame.K_5:
                        board.sketch(5)
                    case pygame.K_6:
                        board.sketch(6)
                    case pygame.K_7:
                        board.sketch(7)
                    case pygame.K_8:
                        board.sketch(8)
                    case pygame.K_9:
                        board.sketch(9)
                    case pygame.K_RETURN:
                        board.place_number()
                    
            if reset_button.draw(screen):
                return(1)
            if restart_button.draw(screen):
                return(2)
            if exit_button.draw(screen):
                return(3)
        pygame.display.update()

def draw_game_won():
     #background
    bg = pygame.image.load(f"{PATH}/backgroundimage.jpg")
    screen.blit(bg, (0, 0))

     #draw title
    font = pygame.font.SysFont('arial_bold', 60)
    title = font.render('Game Won!', True, (255, 255, 255))
    screen.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, SCREEN_WIDTH / 2 - title.get_height()))

    exit_img = pygame.image.load(f"{PATH}/exit.png").convert_alpha()
    exit_button = Button(255, 400, exit_img, 0.15)

    if exit_button.draw(screen):
        quit()

    
def draw_game_lose():
    #background
    bg = pygame.image.load(f"{PATH}/backgroundimage.jpg")
    screen.blit(bg, (0, 0))
    
    #draw title
    font = pygame.font.SysFont('arial_bold', 60)
    title = font.render('Game Over :()', True, (255, 255, 255))
    screen.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, SCREEN_WIDTH / 2 - title.get_height()))

    restart_img = pygame.image.load(f"{PATH}/restart.png").convert_alpha()
    restart_button = Button(255, 400, restart_img, 0.15)

    if restart_button.draw(screen):
        return(2)

if __name__ == '__main__':
    game_over = False

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sudoku game")

    option = 2

    loop = True
    while loop:
        match option:
            case 1:
                screen.fill((251, 247, 245))
                option = draw_game_menu(screen,board)
                board.clear()
                board.draw()
            case 2:
                difficulty = draw_game_start(screen)
                screen.fill((251, 247, 245))
                board = Board(9, 9, screen, difficulty)
                option = draw_game_menu(screen,board)
            case 3:
                loop = False
                sys.exit()

    pygame.display.update()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
