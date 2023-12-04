import pygame
import sys
from board import Board

pygame.init()
pygame.display.set_caption("Sudoku")

BG_COLOR = (255, 255, 245)
screen = pygame.display.set_mode((630, 700))

start_title_font = pygame.font.Font(None, 80)
title_font = pygame.font.Font(None, 80)
text_font = pygame.font.Font(None, 50)


# Basic Settings
def draw_menu():
    bg_image = pygame.image.load("backgroundimage.jpg")
    screen.blit(bg_image, (0, 0))

    # Render and position title
    title_surf = start_title_font.render("Welcome to Sudoku", True, (0, 0, 0))
    title_rect = title_surf.get_rect(center=(630 // 2, 150))
    screen.blit(title_surf, title_rect)

    mode_surf = text_font.render("Select Game Mode:", True, (0, 0, 0))
    mode_rect = mode_surf.get_rect(center=(630 // 2, 300))
    screen.blit(mode_surf, mode_rect)

    pygame.draw.rect(screen, (245, 152, 66), [110, 380, 90, 40])
    easy_text = 'easy'
    easy_surf = text_font.render(easy_text, False, (0, 0, 0))
    easy_rect = easy_surf.get_rect(center=(155, 400))
    screen.blit(easy_surf, easy_rect)

    pygame.draw.rect(screen, (245, 152, 66), [240, 380, 150, 40])
    medium_text = 'Medium'
    medium_surf = text_font.render(medium_text, False, (0, 0, 0))
    medium_rect = medium_surf.get_rect(center=(315, 400))
    screen.blit(medium_surf, medium_rect)

    pygame.draw.rect(screen, (245, 152, 66), [430, 380, 90, 40])
    hard_text = 'Hard'
    hard_surf = text_font.render(hard_text, False, (0, 0, 0))
    hard_rect = hard_surf.get_rect(center=(475, 400))
    screen.blit(hard_surf, hard_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Easy
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()

                if 110 <= mouse[0] <= 200 and 380 <= mouse[1] <= 420:
                    draw_board('easy')

                # medium
                elif 225 <= mouse[0] <= 375 and 380 <= mouse[1] <= 420:
                    draw_board('medium')

                # hard
                elif 430 <= mouse[0] <= 520 and 380 <= mouse[1] <= 420:
                    draw_board('hard')

            pygame.display.update()


def draw_board(difficulty):
    sudoku_board = Board(630, 700, screen, difficulty)
    screen.fill(BG_COLOR)
    sudoku_board.draw()
    pygame.display.update()

    while True:

        mouse = pygame.mouse.get_pos()

        # Reset button
        pygame.draw.rect(screen, (245, 152, 66), [105, 645, 100, 40])
        easy_text = 'Reset'
        easy_surf = text_font.render(easy_text, False, (0, 0, 0))
        easy_rect = easy_surf.get_rect(center=(155, 665))
        screen.blit(easy_surf, easy_rect)
        pygame.display.update()

        # Restart button
        pygame.draw.rect(screen, (245, 152, 66), [240, 645, 150, 40])
        medium_text = 'Restart'
        medium_surf = text_font.render(medium_text, False, (0, 0, 0))
        medium_rect = medium_surf.get_rect(center=(315, 665))
        screen.blit(medium_surf, medium_rect)
        pygame.display.update()

        # Exit
        pygame.draw.rect(screen, (245, 152, 66), [430, 645, 90, 40])
        hard_text = 'Exit'
        hard_surf = text_font.render(hard_text, False, (0, 0, 0))
        hard_rect = hard_surf.get_rect(center=(475, 665))
        screen.blit(hard_surf, hard_rect)
        pygame.display.update()

        # Checks full board
        if sudoku_board.is_full():

            if sudoku_board.check_board():
                draw_game_won()
            else:
                draw_game_over()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                # click and select function
                if 0 <= mouse[1] <= 630:
                    select_row, select_col = sudoku_board.click(mouse[0], mouse[1])
                    sudoku_board.select(select_row, select_col)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    sudoku_board.clear()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    sudoku_board.place_number(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    sudoku_board.sketch(1)
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    sudoku_board.sketch(2)
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    sudoku_board.sketch(3)
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    sudoku_board.sketch(4)
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    sudoku_board.sketch(5)
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    sudoku_board.sketch(6)
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    sudoku_board.sketch(7)
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    sudoku_board.sketch(8)
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    sudoku_board.sketch(9)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 105 <= mouse[0] <= 205 and 645 <= mouse[1] <= 685:
                    sudoku_board.reset_to_original()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 240 <= mouse[0] <= 390 and 645 <= mouse[1] <= 685:
                    draw_menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 430 <= mouse[0] <= 520 and 645 <= mouse[1] <= 685:
                    pygame.quit()
                    sys.exit()


def draw_game_won():
    # Set background image
    bg_image = pygame.image.load('backgroundimage.jpg')
    screen.blit(bg_image, (0, 0))

    # Draw game won
    winner_text = 'Game won!'
    winner_surf = title_font.render(winner_text, False, (0, 0, 0))
    winner_rect = winner_surf.get_rect(center=(315, 170))
    screen.blit(winner_surf, winner_rect)

    # Exit button
    pygame.draw.rect(screen, (245, 152, 66), [240, 380, 150, 40])
    exit_text = 'Exit'
    exit_surf = text_font.render(exit_text, False, (0, 0, 0))
    exit_rect = exit_surf.get_rect(center=(315, 400))
    screen.blit(exit_surf, exit_rect)
    pygame.display.update()

    while True:

        mouse_exit = pygame.mouse.get_pos()

        # Exit button
        pygame.draw.rect(screen, (245, 152, 66), [240, 380, 150, 40])
        exit_text = 'Exit'
        exit_surf = text_font.render(exit_text, False, (0, 0, 0))
        exit_rect = exit_surf.get_rect(center=(315, 400))
        screen.blit(exit_surf, exit_rect)

        pygame.display.update()

        for event_exit in pygame.event.get():

            if event_exit.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event_exit.type == pygame.MOUSEBUTTONDOWN:
                if 240 <= mouse_exit[0] <= 390 and 380 <= mouse_exit[1] <= 420:
                    pygame.quit()
                    sys.exit()


def draw_game_over():
    bg_image = pygame.image.load('backgroundimage.jpg')
    screen.blit(bg_image, (0, 0))

    # Draw game over
    loser_text = 'Game Over'
    loser_surf = title_font.render(loser_text, False, (0, 0, 0))
    loser_rect = loser_surf.get_rect(center=(315, 170))
    screen.blit(loser_surf, loser_rect)

    # Restart button
    pygame.draw.rect(screen, (245, 152, 66), [240, 380, 150, 40])
    restart_text = 'Restart'
    restart_surf = text_font.render(restart_text, False, (0, 0, 0))
    restart_rect = restart_surf.get_rect(center=(315, 400))
    screen.blit(restart_surf, restart_rect)

    pygame.display.update()

    # loop for hovering and button usage
    while True:

        mouse_restart = pygame.mouse.get_pos()

        pygame.draw.rect(screen, (245, 152, 66), [240, 380, 150, 40])
        restart_text = 'Restart'
        restart_surf = text_font.render(restart_text, False, (0, 0, 0))
        restart_rect = restart_surf.get_rect(center=(315, 400))
        screen.blit(restart_surf, restart_rect)
        pygame.display.update()

        for event_exit in pygame.event.get():

            if event_exit.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event_exit.type == pygame.MOUSEBUTTONDOWN:
                if 240 <= mouse_restart[0] <= 390 and 380 <= mouse_restart[1] <= 420:
                    draw_menu()


if __name__ == '__main__':
    draw_menu()
