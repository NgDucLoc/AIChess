import pygame, sys
from pygame.locals import *
from tkinter import *
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from playWithAIState import *
from playWithPersonState import *
def menuState():
    pygame.init()
    WHITE = (255, 255, 255)
    init_background = pygame.image.load("images/menu_state.jpg")
    screen = pygame.display.set_mode((567, 589))

    running = True
    state = "init"
    color = "WHITE"

    while running:
    
        screen.blit(init_background, (0, 0))
        if state == "init":
            titleSize = pygame.font.Font("images/gameFont.ttf", 25)
            titleText = titleSize.render('Nhan Enter de choi', True, WHITE)
            titleRect = titleText.get_rect(center=(300, 400))
            screen.blit(titleText, titleRect)
            titleText1 = titleSize.render('Chon che do', True, WHITE)
            titleRect1 = titleText1.get_rect(center=(300, 450))
            screen.blit(titleText1, titleRect1)
            titleText2 = titleSize.render('1. PvE', True, WHITE)
            titleRect2 = titleText2.get_rect(center=(300, 500))
            screen.blit(titleText2, titleRect2)
            titleText3 = titleSize.render('2. PvP', True, WHITE)
            titleRect3 = titleText3.get_rect(center=(300, 550))
            screen.blit(titleText3, titleRect3)
            pygame.display.update()

        for event in pygame.event.get():
            if event.type==pygame.QUIT: 
                pygame.quit()
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and state == "init":
                    playWithAI()
                if event.key == pygame.K_2 and state == "init":
                    playWithPerson()
                





















