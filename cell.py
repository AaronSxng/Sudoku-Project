import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = None


    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        number_font = pygame.font.SysFont('arial_bold', 50)
        if self.value != 0:
            number = number_font.render(str(self.value),0,(0, 0, 0))
            chip_x_rect = number.get_rect(
                center=(75+self.row*50, 77.5+self.col*50))
            self.screen.blit(number, chip_x_rect)

    def draw_sketched_value(self):
        number_font = pygame.font.SysFont('arial_bold', 40)
        if self.sketched_value != None and self.value == 0:
            number = number_font.render(str(self.sketched_value),0,(100, 100, 100))
            chip_x_rect = number.get_rect(
                center=(65+self.row*50, 67.5+self.col*50))
            self.screen.blit(number, chip_x_rect)