import pygame
from cell import Cell
import sudoku_generator

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen 
        self.difficulty = difficulty
        self.board = sudoku_generator.generate_sudoku(width, difficulty)
        self.cells = [[Cell(self.board[i][j], i, j, self.screen) 
                      for j in range(self.width)] for i in range(self.width)]
    #Draws outline of sudoku grid
    def draw(self):
        for i in range(0, 10):
            if i % 3 == 0:
                pygame.draw.line(self.screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
                pygame.draw.line(self.screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

            pygame.draw.line(self.screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
            pygame.draw.line(self.screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
        for i in range(self.width):
            for j in range(self.height):
                self.cells[i][j].draw()
        pygame.display.update()


    def select(self, row, col):
        pass

    def click(self, x, y):
        pass

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass
    
    def find_empty(self):
        pass

    def check_board(self):
        pass
    