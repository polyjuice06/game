# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
import sys
import time
import random
background_width = 1080
def back(background,x,y):
    global screen,background1
    screen.blit(background,(x,y))
def character(x,y):
    global screen,character1
    screen.blit(character1,(x,y))
def rungame():
    global screen,background1,clock,background2
    backgroundx_1, backgroundx_2 = 0, background_width
    x,y = 0 ,500
    y_change = 0
    background_change, jump_cooltime = 0, 28
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    background_change = -10.8
                elif event.key == pygame.K_d:
                    background_change = 10.8
                elif event.key == pygame.K_w and jump_cooltime >= 28:
                    y_change = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    background_change = 0
        x += background_change
        if x< 0:
            x = 0
        if x > background_width - 100:
            x = background_width - 100
        if y_change > 0 and jump_cooltime >= 15:
            jump_cooltime -= 1
        elif jump_cooltime < 15 and jump_cooltime > 0:
            jump_cooltime -= 1
            y_change = -5
        elif jump_cooltime <= 0:
            y_change = 0
            jump_cooltime = 28
        y -= y_change
        back(background1,backgroundx_1,0)
        character(x,y)
        pygame.display.update()
        clock.tick(60)
def initGame():
    global screen,background1,background2,clock,character1
    pygame.init()
    screen = pygame.display.set_mode((background_width, 640))
    background1 = pygame.image.load("./img/background.jpg")
    background2 = background1.copy()
    character1 = pygame.image.load("./img/wizard.png")
    clock = pygame.time.Clock()
    rungame()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initGame()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
