import pygame
import sys
pygame.init()
# rgb: red, green, blue
RED =(255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(BG_COLOR)

# pygame.draw.line(screen, RED, (10, 10),(300, 300),10)

def draw_lines():
    # 1 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), 15)
# 2 horizontal
pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), 15)
# 1 vertial
pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), 15)
# 2 vertial
pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), 15)

draw_lines()

# mainloop
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pygame.display.update()
