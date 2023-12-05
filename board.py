import pygame
from cell import Cell
import sudoku_generator

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen 
        self.board = sudoku_generator.generate_sudoku(width, difficulty)
        self.cells = [[Cell(self.board[i][j], i, j, self.screen) 
                      for j in range(self.width)] for i in range(self.width)]
        self.current_cell = None
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
                if(self.cells[i][j].value == 0):
                    self.cells[i][j].draw_sketched_value()
        pygame.display.update()

    def select(self, row, col):
        pygame.draw.line(self.screen, (255, 0, 0), (col*50, row*50), (col*50+50, row*50), 4)
        pygame.draw.line(self.screen, (255, 0, 0), (col*50, row*50+50), (col*50+50, row*50+50), 4)
        pygame.draw.line(self.screen, (255, 0, 0), (col*50, row*50), (col*50, row*50+50), 4)
        pygame.draw.line(self.screen, (255, 0, 0), (col*50+50, row*50), (col*50+50, row*50+50), 4)
        pygame.display.update()
        self.current_cell = (col-1,row-1)

    def click(self, x, y):
        if (x > 50 and x < 500) and (y > 50 and y < 500):
            return (x,y)
        return None

    def clear(self):
        for i in range(self.width):
            for j in range(self.height):
                self.cells[i][j].sketched_value = None
        self.cells = [[Cell(self.board[i][j], i, j, self.screen) 
                      for j in range(self.width)] for i in range(self.width)]

    def sketch(self, value):
        if self.cells[self.current_cell[0]][self.current_cell[1]].value == 0:
            pygame.draw.rect(self.screen, (255,255,255),(self.current_cell[0]*50+54,self.current_cell[1]*50+54,42,42))
            cell = self.cells[self.current_cell[0]][self.current_cell[1]]
            cell.set_sketched_value(value)
            cell.draw_sketched_value()

    def place_number(self):
        cell = self.cells[self.current_cell[0]][self.current_cell[1]]
        if cell.value == 0 and cell.sketched_value != None:
            pygame.draw.rect(self.screen, (255,255,255),(self.current_cell[0]*50+54,self.current_cell[1]*50+54,42,42))
            cell.value = cell.sketched_value
            cell.draw()
        for i in range(self.width):
            for j in range(self.height):
                print(self.cells[j][i].value, end=' ')
            print('', end='\n')
        print()

    def reset_to_original(self):
        for i in range(self.width):
            for j in range(self.height):
                self.cells[i][j].set_cell_value(self.board[i][j])

    #
    def is_full(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.cells[i][j].value == 0:
                    return False
        return True

    def update_board(self):
        for i in range(self.width):
            for j in range(self.height):
                self.board[i][j] = self.cells[i][j].value
    
    def find_empty(self):
        pass

    def check_board(self):
        win = True
        for i in range(self.width):
            list = []
            for j in range(self.height):
                if self.cells[i][j].value not in list:
                    list.append(self.cells[i][j].value)
                else:
                    win = False

        for i in range(self.width):
            list = []
            for j in range(1, self.height):
                if self.cells[i][j].value not in list:
                    list.append(self.cells[i][j].value)
                else:
                    win = False
        
        for x in range(0, 7, 3):
            for y in range(0, 7, 3):
                list = []
                for i in range(x, x+3):
                    for j in range(y, y+3):
                        if self.cells[i][j].value not in list:
                            list.append(self.cells[i][j].value)
                        else:
                            win = False
        if win:
            print("You WON")
            return True
        else:
            print("You Lost")
        return False