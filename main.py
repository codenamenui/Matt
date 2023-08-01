import pygame
import json
from functions import *
from classes import *

pygame.init()

# Defining Clock and UPS for Max Updates of the Program per Second
UPS = 60
clock = pygame.time.Clock()
S_WIDTH = 920
S_HEIGHT = 720
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
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

# Images
homeI = pygame.transform.scale(pygame.image.load("home.svg"), (50, 50))
plusI = pygame.transform.scale(pygame.image.load("plus.svg"), (40, 50))

# Buttons
homeB = Button(homeI, (50, 50), get_font(0))

baseline = 325
menuB = { "overview" : Button(pygame.Rect(0, 0, 200, 50), (S_WIDTH//2, baseline + 75 * 0), get_font(30), "overview", "black", "white", "purple"),
                "profiles" : Button(pygame.Rect(0, 0, 200, 50), (S_WIDTH//2, baseline + 75 * 1), get_font(30), "profiles", "black", "white", "purple"),
                "options" : Button(pygame.Rect(0, 0, 200, 50), (S_WIDTH//2, baseline + 75 * 2), get_font(30), "options", "black", "white", "purple"),
                "exit" : Button(pygame.Rect(0, 0, 200, 50), (S_WIDTH//2, baseline + 75 * 3), get_font(30), "exit", "black", "white", "purple"),
                # "" : Button()
                }

# overviewB = { "" : Button(),
#                 "" : Button(),
#                 "" : Button(),
#                 "" : Button(),
#                 "" : Button()
#                 }

profilesB = { "add" : Button(plusI, (S_WIDTH - 100, 50), get_font(0)),
                # "" : Button(),
                # "" : Button(),
                # "" : Button(),
                # "" : Button()
                }

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

# Settings
conversion = True
tutorial = True
flavor = False
darkMode = False

frame = "menu"
while True:

    while frame == "menu":

        mouse = pygame.mouse.get_pos()

        screen.fill("white")
        title = get_font(65).render("Welcome to DIME!", True, "black")
        lastuser = get_font(40).render("lastuser!", True, "black")
        screen.blit(title, title.get_rect(center=(S_WIDTH//2, 120)))
        screen.blit(lastuser, lastuser.get_rect(center=(S_WIDTH//2, 200)))

        for button in menuB.values():
            button.changeColor(mouse)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if menuB['exit'].check(mouse):
                    pygame.quit()
                elif menuB['overview'].check(mouse):
                    frame = "overview"
                elif menuB['profiles'].check(mouse):
                    frame = "profiles"
                elif menuB['options'].check(mouse):
                    frame = "options"

        clock.tick(UPS)
        pygame.display.update()

    while frame == "overview":
        
        screen.fill("white")
        mouse = pygame.mouse.get_pos()

        homeB.changeColor(mouse)
        homeB.update(screen)
        overviewTxt = get_font(40).render("Overview of Profile 1", True, "black")
        screen.blit(overviewTxt, overviewTxt.get_rect(center=(360, 50)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if homeB.check(mouse):
                    frame = "menu"

        clock.tick(UPS)
        pygame.display.update()

    while frame == "profiles":
        
        screen.fill("white")
        mouse = pygame.mouse.get_pos()

        homeB.changeColor(mouse)
        homeB.update(screen)
        overviewTxt = get_font(40).render("Registered Profiles", True, "black")
        screen.blit(overviewTxt, overviewTxt.get_rect(center=(360, 50)))

        for button in profilesB.values():
            button.changeColor(mouse)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if homeB.check(mouse):
                    frame = "menu"
                elif profilesB['add'].check(mouse):
                    running = True
                    while running:

                        mouse = pygame.mouse.get_pos()
                        bigRect = pygame.Rect(0, 0, 400, 500)
                        bigRect.center = (S_WIDTH//2, S_HEIGHT//2)
                        smallRect = pygame.Rect(0, 0, 400, 500)
                        smallRect.center = (S_WIDTH//2 - 3, S_HEIGHT//2 - 3)
                        pygame.draw.rect(screen, "black", bigRect, width=3)
                        pygame.draw.rect(screen, "black", bigRect, width=3)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_1:
                                    running = False

                        clock.tick(UPS)
                        pygame.display.update()

        clock.tick(UPS)
        pygame.display.update()

    while frame == "options":
        
        screen.fill("white")
        mouse = pygame.mouse.get_pos()

        homeB.changeColor(mouse)
        homeB.update(screen)
        overviewTxt = get_font(40).render("Overview of Profile 1", True, "black")
        screen.blit(overviewTxt, overviewTxt.get_rect(center=(360, 50)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if homeB.check(mouse):
                    frame = "menu"

        clock.tick(UPS)
        pygame.display.update()
