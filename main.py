import pygame, sys
import json
from functions import *
from classes import *
from sys import exit

pygame.init()

# Defining Clock and UPS for Max Updates of the Program per Second
UPS = 60
clock = pygame.time.Clock()
S_WIDTH = 920
S_HEIGHT = 720
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption('DIME: A DLSU-Based Finance Tracker')

# Color
textColor = "black"
bgColor = "white"

# Account
accounts = {
            "1" : User("1", 23232, 3232),
            "2" : User("2", 23232, 3232),
            "3" : User("3", 23232, 3232),
            "4" : User("4", 23232, 3232),
            "5" : User("5", 23232, 3232),
            "6" : User("6", 23232, 3232),
            "7" : User("7", 23232, 3232),
            }
# with open("accounts.json", "a+") as file:
#     file.seek(0)
#     try:
#         data = json.load(file)
#     except json.JSONDecodeError:
#         pass
#     else:
#         return data

if all([not user.chosen for user in accounts.values()]) and len(accounts) != 0:
    keys = list(accounts.keys())
    accounts[keys[0]].chosen = True

# Images
homeI = pygame.transform.scale(pygame.image.load("home.svg"), (50, 50))
plusI = pygame.transform.scale(pygame.image.load("plus.svg"), (40, 40))
minusI = pygame.transform.scale(pygame.image.load("minus.svg"), (40, 40))
trashI = pygame.transform.scale(pygame.image.load("trash.svg"), (50, 50))

# Buttons
homeB = Button(homeI, (50, 50), get_font(0))

baseline = 325
menuB = {"overview": Button(pygame.Rect(0, 0, 200, 50), (S_WIDTH//2, baseline + 75 * 0), get_font(30), "overview", textColor, bgColor, "purple"),
         "profiles": Button(pygame.Rect(0, 0, 200, 50), (S_WIDTH//2, baseline + 75 * 1), get_font(30), "profiles", textColor, bgColor, "purple"),
         "options": Button(pygame.Rect(0, 0, 200, 50), (S_WIDTH//2, baseline + 75 * 2), get_font(30), "options", textColor, bgColor, "purple"),
         "exit": Button(pygame.Rect(0, 0, 200, 50), (S_WIDTH//2, baseline + 75 * 3), get_font(30), "exit", textColor, bgColor, "purple")
         }

profilesB = {"add": Button(plusI, (S_WIDTH - 250, 40), get_font(0)),
             "minus": Button(minusI, (S_WIDTH - 100, 40), get_font(0)),
             }

baseline = 200
deleteButtons = [Button(trashI, (S_WIDTH - 100, baseline), get_font(0)),
                 Button(trashI, (S_WIDTH - 100, baseline + 175 * 1), get_font(0)),
                 Button(trashI, (S_WIDTH - 100, baseline + 175 * 2), get_font(0))
                ]

baseline = 200
selectButtons = [Button(pygame.Rect(0, 0, S_WIDTH, 200), (S_WIDTH//2, baseline), get_font(0)),
                 Button(pygame.Rect(0, 0, S_WIDTH, 200), (S_WIDTH//2, baseline + 200 * 1), get_font(0)),
                 Button(pygame.Rect(0, 0, S_WIDTH, 200), (S_WIDTH//2, baseline + 200* 2), get_font(0))
                ]

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
delete = False

frame = "menu"
index = 0
while True:

    for user in accounts.values():
        if user.chosen:
            lastuserTxt = user.username
            break

    while frame == "menu":

        mouse = pygame.mouse.get_pos()

        screen.fill(bgColor)
        title = get_font(65).render("Welcome to DIME!", True, textColor)
        lastuser = get_font(40).render(f"{lastuserTxt}!", True, textColor)
        screen.blit(title, title.get_rect(center=(S_WIDTH//2, 120)))
        screen.blit(lastuser, lastuser.get_rect(center=(S_WIDTH//2, 200)))

        for button in menuB.values():
            button.changeColor(mouse)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if menuB['exit'].check(mouse):
                    pygame.quit()
                    sys.exit()
                elif menuB['overview'].check(mouse):
                    frame = "overview"
                elif menuB['profiles'].check(mouse):
                    frame = "profiles"
                elif menuB['options'].check(mouse):
                    frame = "options"

        clock.tick(UPS)
        pygame.display.update()

    while frame == "overview":

        screen.fill(bgColor)
        mouse = pygame.mouse.get_pos()

        homeB.changeColor(mouse)
        homeB.update(screen)
        overviewTxt = get_font(40).render(
            "Overview of Profile 1", True, textColor)
        screen.blit(overviewTxt, overviewTxt.get_rect(midleft=(100, 55)))
        pygame.draw.line(screen, textColor, (25, 100),
                         (S_WIDTH - 25, 100), width=3)
        pygame.draw.circle(screen, textColor, (S_WIDTH//2 - 15, 110),  3)
        pygame.draw.circle(screen, textColor, (S_WIDTH//2, 110),  3)
        pygame.draw.circle(screen, textColor, (S_WIDTH//2 + 15, 110), 3)
        pygame.draw.line(screen, textColor, (25, 120),
                         (S_WIDTH - 25, 120), width=3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if homeB.check(mouse):
                    frame = "menu"

        clock.tick(UPS)
        pygame.display.update()

    while frame == "profiles":

        screen.fill(bgColor)
        mouse = pygame.mouse.get_pos()
        homeB.changeColor(mouse)
        homeB.update(screen)
        profileTxt = get_font(40).render("Registered Profiles", True, textColor)
        screen.blit(profileTxt, profileTxt.get_rect(midleft=(100, 55)))
        pygame.draw.line(screen, textColor, (25, 100), (S_WIDTH - 25, 100), width=3)
        pygame.draw.circle(screen, textColor, (S_WIDTH//2 - 15, 110), 3)
        pygame.draw.circle(screen, textColor, (S_WIDTH//2, 110), 3)
        pygame.draw.circle(screen, textColor, (S_WIDTH//2 + 15, 110), 3)
        pygame.draw.line(screen, textColor, (25, 120), (S_WIDTH - 25, 120), width=3)

        addTxt = get_font(15).render("Add Profile", True, textColor)
        minusTxt = get_font(15).render("Remove Profile", True, textColor)
        screen.blit(addTxt, addTxt.get_rect(center=(S_WIDTH - 250, 80)))
        screen.blit(minusTxt, minusTxt.get_rect(center=(S_WIDTH - 100, 80)))

        for i in range(1, 4):
            pygame.draw.line(screen, textColor, (25, 120 + 175 * i), (S_WIDTH - 25, 120 + 175 * i), width=3)
        
        try:
            current_profiles = list(enumerate(list(accounts.values())[index:index + 3]))
        except:
            current_profiles = list(enumerate(list(accounts.values())[index:index]))

        baseline = 150
        for i, prof in current_profiles:
            if prof.chosen:
                color = "green"
            else:
                color = textColor
            usernameTxt = get_font(40).render(str(prof.username), True, color)
            screen.blit(usernameTxt, usernameTxt.get_rect(topleft=(35, baseline + 175 * i)))
            if conversion:
                money = f'{prof.remaining} PHP'
            else:
                money = f'{(prof.remaining/55):.2f} USD'
            remainingTxt = get_font(30).render(f'Balance Remaining: {money}', True, textColor)
            screen.blit(remainingTxt, remainingTxt.get_rect(topleft=(35, baseline + 50 + 175 * i)))
            if conversion:
                money = f'{prof.spent} PHP'
            else:
                money = f'{(prof.spent/55):.2f} USD'
            spentTxt = get_font(30).render(f'Balance Spent:      {money}', True, textColor)
            screen.blit(spentTxt, spentTxt.get_rect(topleft=(35, baseline + 80 + 175 * i)))

        for button in profilesB.values():
            button.changeColor(mouse)
            button.update(screen)

        if delete:
            for button in deleteButtons:
                button.changeColor(mouse)
                button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 5:
                    if index < len(accounts) - 3:
                        index += 1
                elif event.button == 4:
                    if index > 0:
                        index -= 1
                elif event.button == 1:
                    keys = list(accounts.keys())
                    try:
                        if selectButtons[0].check(mouse):
                            accounts[lastuserTxt].chosen = False
                            lastuserTxt = accounts[keys[index]].username
                            accounts[keys[index]].chosen = True
                        elif selectButtons[1].check(mouse):
                            accounts[lastuserTxt].chosen = False
                            lastuserTxt = accounts[keys[index + 1]].username
                            accounts[keys[index + 1]].chosen = True
                        elif selectButtons[2].check(mouse):
                            accounts[lastuserTxt].chosen = False
                            lastuserTxt = accounts[keys[index + 2]].username
                            accounts[keys[index + 2]].chosen = True
                    except:
                        pass
                    if delete:
                        try:
                            if deleteButtons[0].check(mouse):
                                del accounts[keys[index]]
                            elif deleteButtons[1].check(mouse):
                                del accounts[keys[index + 1]]
                            elif deleteButtons[2].check(mouse):
                                del accounts[keys[index + 2]]
                        except:
                            pass

                    if homeB.check(mouse):
                        frame = "menu"
                    elif profilesB['add'].check(mouse):
                        inp = add("Name", "Balance (in PHP)", screen, S_WIDTH, clock, textColor, bgColor, darkMode)
                        screen.blit(pygame.transform.scale(pygame.image.load("cross.svg"), (30, 40)), (617, 171))
                        if inp == None:
                            pass
                        elif inp[0] in accounts:
                            prompt("Profile already exists!", screen, S_WIDTH, clock, textColor, bgColor)
                        else:
                            accounts[inp[0]] = User(inp[0], inp[1], 0)
                            prompt("Profile successfuly created!", screen, S_WIDTH, clock, textColor, bgColor)
                    elif profilesB['minus'].check(mouse):
                        delete = not delete

        clock.tick(UPS)
        pygame.display.update()

    while frame == "options":

        screen.fill(bgColor)
        mouse = pygame.mouse.get_pos()

        homeB.changeColor(mouse)
        homeB.update(screen)
        overviewTxt = get_font(40).render("Option", True, textColor)
        screen.blit(overviewTxt, overviewTxt.get_rect(midleft=(100, 55)))
        pygame.draw.line(screen, textColor, (25, 100),
                         (S_WIDTH - 25, 100), width=3)
        pygame.draw.circle(screen, textColor, (S_WIDTH//2 - 15, 110),  3)
        pygame.draw.circle(screen, textColor, (S_WIDTH//2, 110),  3)
        pygame.draw.circle(screen, textColor, (S_WIDTH//2 + 15, 110), 3)
        pygame.draw.line(screen, textColor, (25, 120),
                         (S_WIDTH - 25, 120), width=3)

        x = 25
        y = 150

        titleTxt = get_font(30).render("General", True, textColor)
        screen.blit(titleTxt, titleTxt.get_rect(midleft=(x, y)))

        if darkMode:
            check = pygame.transform.scale(
            pygame.image.load("check-white.svg"), (x-5, 15))
        else:
            check = pygame.transform.scale(
            pygame.image.load("check.svg"), (x-5, 15))

        # conversion
        checkbox_01_border = pygame.draw.rect(
            screen, textColor, pygame.Rect(x, y+30, 30, 30), width=2)

        check_01 = get_font(30).render(
            "Toggle Money Conversion to PHP", True, textColor)
        screen.blit(check_01, check_01.get_rect(midleft=(x+50, y+45)))

        if conversion:
            screen.blit(check, check.get_rect(midleft=(x+5, y+45)))

        # tutorial
        checkbox_02_border = pygame.draw.rect(
            screen, textColor, pygame.Rect(x, y+90, 30, 30), width=2)

        check_02 = get_font(30).render(
            "Toggle Tutorial for New Users", True, textColor)
        screen.blit(check_02, check_02.get_rect(midleft=(x+50, y+105)))

        if tutorial:
            screen.blit(check, check.get_rect(midleft=(x+5, y+105)))

        # flavor
        checkbox_03_border = pygame.draw.rect(
            screen, textColor, pygame.Rect(x, y+150, 30, 30), width=2)

        check_03 = get_font(30).render(
            "Toggle Flavor Text", True, textColor)
        screen.blit(check_03, check_03.get_rect(midleft=(x+50, y+165)))

        if flavor:
            screen.blit(check, check.get_rect(midleft=(x+5, y+165)))

        # darkMode
        checkbox_04_border = pygame.draw.rect(
            screen, textColor, pygame.Rect(x, y+210, 30, 30), width=2)

        check_04 = get_font(30).render(
            "Toggle Dark Mode", True, textColor)
        screen.blit(check_04, check_04.get_rect(midleft=(x+50, y+225)))

        if darkMode:
            screen.blit(check, check.get_rect(midleft=(x+5, y+225)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if homeB.check(mouse):
                    frame = "menu"
                elif checkbox_01_border.collidepoint(mouse):
                    conversion = not conversion
                elif checkbox_02_border.collidepoint(mouse):
                    tutorial = not tutorial
                elif checkbox_03_border.collidepoint(mouse):
                    flavor = not flavor
                elif checkbox_04_border.collidepoint(mouse):
                    darkMode = not darkMode
                    if darkMode:
                        bgColor = (30, 30, 30)
                        textColor = "white"
                        # del homeI, plusI, minusI, trashI
                        homeI = pygame.transform.scale(pygame.image.load("home-white.svg"), (50, 50))
                        plusI = pygame.transform.scale(pygame.image.load("plus-white.svg"), (40, 40))
                        minusI = pygame.transform.scale(pygame.image.load("minus-white.svg"), (40, 40))
                        trashI = pygame.transform.scale(pygame.image.load("trash-white.svg"), (50, 50))
                        homeB = Button(homeI, (50, 50), get_font(0))

                        baseline = 325
                        menuB = {"overview": Button(pygame.Rect(0, 0, 200, 50), (S_WIDTH//2, baseline + 75 * 0), get_font(30), "overview", textColor, bgColor, "purple"),
                                 "profiles": Button(pygame.Rect(0, 0, 200, 50), (S_WIDTH//2, baseline + 75 * 1), get_font(30), "profiles", textColor, bgColor, "purple"),
                                 "options": Button(pygame.Rect(0, 0, 200, 50), (S_WIDTH//2, baseline + 75 * 2), get_font(30), "options", textColor, bgColor, "purple"),
                                 "exit": Button(pygame.Rect(0, 0, 200, 50), (S_WIDTH//2, baseline + 75 * 3), get_font(30), "exit", textColor, bgColor, "purple")
                                 }

                        profilesB = {"add": Button(plusI, (S_WIDTH - 250, 40), get_font(0)),
                                     "minus": Button(minusI, (S_WIDTH - 100, 40), get_font(0)),
                                     }

                        baseline = 200
                        deleteButtons = [Button(trashI, (S_WIDTH - 100, baseline), get_font(0)),
                                         Button(trashI, (S_WIDTH - 100, baseline + 175 * 1), get_font(0)),
                                         Button(trashI, (S_WIDTH - 100, baseline + 175 * 2), get_font(0))
                                        ]
                    else:
                        bgColor = "white"
                        textColor = "black"
                        homeI = pygame.transform.scale(pygame.image.load("home.svg"), (50, 50))
                        plusI = pygame.transform.scale(pygame.image.load("plus.svg"), (40, 40))
                        minusI = pygame.transform.scale(pygame.image.load("minus.svg"), (40, 40))
                        trashI = pygame.transform.scale(pygame.image.load("trash.svg"), (50, 50))
                        homeB = Button(homeI, (50, 50), get_font(0))

                        baseline = 325
                        menuB = {"overview": Button(pygame.Rect(0, 0, 200, 50), (S_WIDTH//2, baseline + 75 * 0), get_font(30), "overview", textColor, bgColor, "purple"),
                                 "profiles": Button(pygame.Rect(0, 0, 200, 50), (S_WIDTH//2, baseline + 75 * 1), get_font(30), "profiles", textColor, bgColor, "purple"),
                                 "options": Button(pygame.Rect(0, 0, 200, 50), (S_WIDTH//2, baseline + 75 * 2), get_font(30), "options", textColor, bgColor, "purple"),
                                 "exit": Button(pygame.Rect(0, 0, 200, 50), (S_WIDTH//2, baseline + 75 * 3), get_font(30), "exit", textColor, bgColor, "purple")
                                 }

                        profilesB = {"add": Button(plusI, (S_WIDTH - 250, 40), get_font(0)),
                                     "minus": Button(minusI, (S_WIDTH - 100, 40), get_font(0)),
                                     }

                        baseline = 200
                        deleteButtons = [Button(trashI, (S_WIDTH - 100, baseline), get_font(0)),
                                         Button(trashI, (S_WIDTH - 100, baseline + 175 * 1), get_font(0)),
                                         Button(trashI, (S_WIDTH - 100, baseline + 175 * 2), get_font(0))
                                        ]

        clock.tick(UPS)
        pygame.display.update()
