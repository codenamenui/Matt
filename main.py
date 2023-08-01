import pygame
import json
from functions import *
from classes import *

pygame.init()

# Defining Clock and UPS for Max Updates of the Program per Second
UPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('DIME: A DLSU-Based Finance Tracker')

# Account
accounts = {}
# with open("accounts.json", "a+") as file:
#     file.seek(0)
#     try:
#         data = json.load(file)
#     except json.JSONDecodeError:
#         pass
#     else:
#         return data

# Buttons
menuB = { "overview" : Button(pygame.Rect(0, 0, 200, 50), (640, 275), get_font(30), "overview", "black", "white", "purple"),
                "profile" : Button(pygame.Rect(0, 0, 200, 50), (640, 350), get_font(30), "profiles", "black", "white", "purple"),
                "options" : Button(pygame.Rect(0, 0, 200, 50), (640, 425), get_font(30), "options", "black", "white", "purple"),
                "exit" : Button(pygame.Rect(0, 0, 200, 50), (640, 500), get_font(30), "exit", "black", "white", "purple"),
                # "" : Button()
                }

# overviewB = { "" : Button(),
#                 "" : Button(),
#                 "" : Button(),
#                 "" : Button(),
#                 "" : Button()
#                 }

# profileB = { "" : Button(),
#                 "" : Button(),
#                 "" : Button(),
#                 "" : Button(),
#                 "" : Button()
#                 }

# optionsB = { "" : Button(),
#                 "" : Button(),
#                 "" : Button(),
#                 "" : Button(),
#                 "" : Button()
#                 }

# menuButtons = { "" : Button(),
#                 "" : Button(),
#                 "" : Button(),
#                 "" : Button(),
#                 "" : Button()
#                 }

frame = "menu"
while True:

    while frame == "menu":

        mouse = pygame.mouse.get_pos()

        screen.fill("white")
        title = get_font(50).render("Welcome to DIME!", True, "black")
        screen.blit(title, title.get_rect(center=(640, 160)))

        for button in menuB.values():
            button.changeColor(mouse)
            button.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if menuB['exit'].check(mouse):
                    pygame.quit()

        clock.tick(UPS)
        pygame.display.update()

    while frame == "overview":
        
        screen.fill("white")
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        clock.tick(UPS)
        pygame.display.update()

    while frame == "profile":
        
        screen.fill("white")
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        clock.tick(UPS)
        pygame.display.update()

    while frame == "options":
        
        screen.fill("white")
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        clock.tick(UPS)
        pygame.display.update()
