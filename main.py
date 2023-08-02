import pygame, sys
import json
from functions import *
from classes import *
from sys import exit
import datetime

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

# Variable
locationlist = ["Yuchengco Hall", "St. La Salle Hall", "Bloemen Hall", 
                "EGI Taft Tower", "Agno Compound", "One Archer's Place",
                "GC"]
lastuserTxt = ""
# Format the date and time as 00/00/00
formatted_time = datetime.datetime.now().strftime("%m/%d/%y")
date = formatted_time

# Account
accounts = {
            "1" : User("1", 23232, 3232, True, {date : {locationlist[1] : 10000, locationlist[2] : 20000}}),
            # "2" : User("2", 23232, 3232),
            # "3" : User("3", 23232, 3232),
            # "4" : User("4", 23232, 3232),
            # "5" : User("5", 23232, 3232),
            # "6" : User("6", 23232, 3232),
            # "7" : User("7", 23232, 3232),
            }

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
plusI = pygame.transform.scale(pygame.image.load("plus.svg"), (40, 40))
minusI = pygame.transform.scale(pygame.image.load("minus.svg"), (40, 40))
trashI = pygame.transform.scale(pygame.image.load("trash.svg"), (50, 50))
location = pygame.transform.scale(pygame.image.load("location.png"), (S_WIDTH - 90, 300))
sendI = pygame.transform.scale(pygame.image.load("send.svg"), (30, 30))

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

locs = [Button(pygame.Rect(0, 0, 20, 20), (192, 211), get_font(0)),
        Button(pygame.Rect(0, 0, 20, 20), (271, 302), get_font(0)),
        Button(pygame.Rect(0, 0, 20, 20), (463, 209), get_font(0)),
        Button(pygame.Rect(0, 0, 20, 20), (523, 275), get_font(0)),
        Button(pygame.Rect(0, 0, 20, 20), (682, 232), get_font(0)),
        Button(pygame.Rect(0, 0, 20, 20), (740, 275), get_font(0)),
        Button(pygame.Rect(0, 0, 20, 20), (780, 232), get_font(0))]

baseline = 550
addlocsB = Button(pygame.Rect(0, 0, 100, 30), (408, baseline), get_font(20), "Location", base_color=textColor)
removelocsB = Button(pygame.Rect(0, 0, 100, 30), (408, baseline + 100), get_font(20), "Location", base_color=textColor)

sendAddB = Button(sendI, (630, baseline - 1), get_font(0))
sendRemoveB = Button(sendI, (630, baseline + 100 - 1), get_font(0))
 
# Settings
conversion = False
tutorial = True
flavor = False
darkMode = False
delete = False
pick = False

frame = "overview"
index = 0
while True:

    if all([not user.chosen for user in accounts.values()]) and len(accounts) != 0:
        keys = list(accounts.keys())
        accounts[keys[0]].chosen = True

    for user in accounts.values():
        if user.chosen:
            lastuserTxt = user.username
            break


    while frame == "menu":

        mouse = pygame.mouse.get_pos()

        screen.fill(bgColor)
        title = get_font(65).render("Welcome to DIME!", True, textColor)
        lastuser = get_font(40).render(f"{lastuserTxt}", True, textColor)
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
                elif menuB['overview'].check(mouse) and lastuserTxt != "":
                    frame = "overview"
                elif menuB['profiles'].check(mouse):
                    frame = "profiles"
                elif menuB['options'].check(mouse):
                    frame = "options"

        clock.tick(UPS)
        pygame.display.update()

    expense_index = 0
    addBool = False
    removeBool = False
    dateBool = False
    addExpenseTxt = ""
    removeExpenseTxt = ""
    dateTxt = ""
    current_loc = ""

    baseline = 550
    if conversion:
        addExpenseB = Button(pygame.Rect(0, 0, 120, 30), (540, baseline), get_font(20), " PHP", base_color=textColor, color=bgColor)
        removeExpenseB = Button(pygame.Rect(0, 0, 120, 30), (540, baseline + 100), get_font(20), " PHP", base_color=textColor, color=bgColor)
    else:
        addExpenseB = Button(pygame.Rect(0, 0, 120, 30), (540, baseline), get_font(20), " USD", base_color=textColor, color=bgColor)
        removeExpenseB = Button(pygame.Rect(0, 0, 120, 30), (540, baseline + 100), get_font(20), " USD", base_color=textColor, color=bgColor)

    baselineX = 355
    baselineY = 460
    dateB = Button(pygame.Rect(0, 0, 100, 30), (600, 473), get_font(25), formatted_time)

    while frame == "overview":

        screen.fill(bgColor)
        mouse = pygame.mouse.get_pos()

        homeB.changeColor(mouse)
        homeB.update(screen)
        overviewTxt = get_font(40).render(f"Overview of {lastuserTxt}", True, textColor)
        screen.blit(overviewTxt, overviewTxt.get_rect(midleft=(100, 55)))
        pygame.draw.line(screen, textColor, (25, 100), (S_WIDTH - 25, 100), width=3)
        pygame.draw.circle(screen, textColor, (S_WIDTH//2 - 15, 110),  3)
        pygame.draw.circle(screen, textColor, (S_WIDTH//2, 110),  3)
        pygame.draw.circle(screen, textColor, (S_WIDTH//2 + 15, 110), 3)
        pygame.draw.line(screen, textColor, (25, 120), (S_WIDTH - 25, 120), width=3)

        locationRect = pygame.Rect(0, 0, S_WIDTH - 80, 310)
        locationRect.center = (S_WIDTH//2, 285)
        pygame.draw.rect(screen, textColor, locationRect)
        screen.blit(location, location.get_rect(center=(S_WIDTH//2, 285)))

        try:
            current_locations = list(accounts[lastuserTxt].expenses.get(dateTxt, {}).items())[index:index + 7]
        except:
            current_locations = list(accounts[lastuserTxt].expenses.get(dateTxt, {}).items())[index:index]
        pygame.draw.rect(screen, textColor, [40, 455, 300, 230], width=3)
        i = 0
        for loc, expense in current_locations:
            if expense != 0:
                if conversion:
                    money = f'{expense} PHP'
                else:
                    money = f'{(expense)/55:.2f} USD'
                expenseTxt = get_font(20).render(f'{loc}: {money}', True, textColor)
                screen.blit(expenseTxt, expenseTxt.get_rect(bottomleft=(55, 493 + 30 * i)))
                i += 1

        baselineX = 355
        baselineY = 460
        frequentTxt = get_font(30).render("Most Frequented Area", True, textColor)
        screen.blit(frequentTxt, frequentTxt.get_rect(topleft=(baselineX + 315, baselineY)))
        mostArea = get_font(20).render(f'{max(accounts[lastuserTxt].expenses.get(dateTxt, {}), key=accounts[lastuserTxt].expenses.get(dateTxt, {}).get, default="")}', True, textColor)
        screen.blit(mostArea, mostArea.get_rect(center=(baselineX + 430, baselineY + 50)))
        spendingTxt = get_font(25).render("Spending Overview for ", True, textColor)
        screen.blit(spendingTxt, spendingTxt.get_rect(topleft=(baselineX, baselineY)))
        newTxt = get_font(20).render(f"Input New Spendings", True, textColor)
        screen.blit(newTxt, newTxt.get_rect(topleft=(baselineX, baselineY + 40)))
        if conversion:
            money = f'{accounts[lastuserTxt].remaining}'
        else:
            money = f'{accounts[lastuserTxt].remaining/55:.2f}'
        balanceTxt = get_font(20).render(f"Balance: {money}", True, textColor)
        screen.blit(balanceTxt, balanceTxt.get_rect(topleft=(baselineX + 150, baselineY + 40)))
        removeTxt = get_font(20).render(f"Remove Spendings", True, textColor)
        screen.blit(removeTxt, removeTxt.get_rect(topleft=(baselineX, baselineY + 140)))

        pygame.draw.line(screen, textColor, (baselineX, 580), (baselineX + 300, 580), width=3)

        for button in [addlocsB, removelocsB, addExpenseB, removeExpenseB, dateB]:
            button.border(screen, textColor)
            button.update(screen)

        sendAddB.update(screen)
        sendRemoveB.update(screen)
        
        for loc in locs:
            if loc.picked:
                loc.circle(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in range(len(locs)):
                        if locs[i].check(mouse) and pick:
                            for loc in locs:
                                if loc.picked:
                                    loc.picked = False
                                    break
                            current_loc = locationlist[i]
                            locs[i].picked = True
                            pick = False
                        elif locs[i].check(mouse) and not pick:
                            pass
                    if sendAddB.check(mouse) and current_loc != "":
                        if addExpenseTxt == "":
                            addExpenseTxt = "0"
                        if conversion:
                            accounts[lastuserTxt].remaining -= float(addExpenseTxt)
                            accounts[lastuserTxt].spent += float(addExpenseTxt)
                            accounts[lastuserTxt].expenses[dateTxt][current_loc] = accounts[lastuserTxt].expenses.setdefault(dateTxt, {}).setdefault(current_loc, 0) + float(addExpenseTxt)
                        else:
                            accounts[lastuserTxt].remaining -= float(addExpenseTxt) * 55
                            accounts[lastuserTxt].spent += float(addExpenseTxt) * 55
                            accounts[lastuserTxt].expenses[dateTxt][current_loc] = accounts[lastuserTxt].expenses.setdefault(dateTxt, {}).setdefault(current_loc, 0) + float(addExpenseTxt) * 55
                        addExpenseTxt = ""
                        if conversion:
                            addExpenseB.text_input = " PHP"
                        else:
                            addExpenseB.text_input = " USD"
                        addExpenseB.txt()
                    elif sendRemoveB.check(mouse) and current_loc != "":
                        if removeExpenseTxt == "":
                            removeExpenseTxt = "0"
                        if conversion:
                            accounts[lastuserTxt].remaining += float(removeExpenseTxt)
                            accounts[lastuserTxt].spent -= float(removeExpenseTxt)
                            accounts[lastuserTxt].expenses[dateTxt][current_loc] = accounts[lastuserTxt].expenses.setdefault(dateTxt, {}).setdefault(current_loc, 0) - float(removeExpenseTxt)
                        else:
                            accounts[lastuserTxt].remaining += float(removeExpenseTxt) * 55
                            accounts[lastuserTxt].spent -= float(removeExpenseTxt) * 55
                            accounts[lastuserTxt].expenses[dateTxt][current_loc] = accounts[lastuserTxt].expenses.setdefault(dateTxt, {}).setdefault(current_loc, 0) - float(removeExpenseTxt) * 55
                        
                        removeExpenseTxt = ""
                        if conversion:
                            removeExpenseB.text_input = " PHP"
                        else:
                            removeExpenseB.text_input = " USD"
                        removeExpenseB.txt()                    
                    elif addlocsB.check(mouse) or removelocsB.check(mouse):
                        pick = True
                    elif addExpenseB.check(mouse):
                        addExpenseB.base_color = textColor
                        addBool = True
                        removeBool = False
                        dateBool = False
                        addExpenseB.text_input = addExpenseTxt
                    elif removeExpenseB.check(mouse):
                        removeExpenseB.base_color = textColor
                        addBool = False
                        removeBool = True
                        dateBool = False
                        removeExpenseB.text_input = removeExpenseTxt
                    elif dateB.check(mouse):
                        dateTxt = ""
                        dateB.base_color = textColor
                        addBool = False
                        removeBool = False
                        dateBool = True
                        dateB.text_input = dateTxt
                    elif homeB.check(mouse):
                        frame = "menu"
                        for loc in locs:
                            if loc.picked:
                                loc.picked = False
                                break
                    else:
                        if not is_valid_date_format(dateTxt, "%m/%d/%y"):
                            dateTxt = formatted_time
                            dateB.text_input = dateTxt
                            dateB.txt()
                            dateBool = False
                if event.button == 5:
                    if index < len(accounts[lastuserTxt].expenses.get(dateTxt, {})) - 7:
                        index += 1
                elif event.button == 4:
                    if index > 0:
                        index -= 1
            elif event.type == pygame.KEYDOWN:
                if dateBool:
                    if len(dateTxt) == 8 and keyboardinput(event) != "del":
                        pass
                    elif keyboardinput(event) == None:
                        pass
                    elif keyboardinput(event) == "del":
                        dateTxt = dateTxt[:-1]
                    elif keyboardinput(event) not in "1234567890/":
                        pass
                    else:
                        dateTxt += keyboardinput(event)
                    dateB.text_input = dateTxt
                    dateB.txt()
                elif addBool:
                    if len(addExpenseTxt) == 7 and keyboardinput(event) != "del":
                        pass
                    elif keyboardinput(event) == "del":
                        addExpenseTxt = addExpenseTxt[:-1]
                    elif keyboardinput(event) == None:
                        pass
                    elif keyboardinput(event) not in "1234567890.":
                        pass
                    else:
                        try:
                            if conversion and float(addExpenseTxt + keyboardinput(event)) <= accounts[lastuserTxt].remaining:
                                addExpenseTxt += keyboardinput(event)
                            elif float(addExpenseTxt + keyboardinput(event)) <= accounts[lastuserTxt].remaining / 55:
                                addExpenseTxt += keyboardinput(event)
                        except:
                            try:
                                if conversion and float(addExpenseTxt + keyboardinput(event) + "0") <= accounts[lastuserTxt].remaining:
                                    addExpenseTxt += keyboardinput(event)
                                elif float(addExpenseTxt + keyboardinput(event) + "0") <= accounts[lastuserTxt].remaining / 55:
                                    addExpenseTxt += keyboardinput(event)
                            except:
                                pass
                    if conversion:
                        currency = " PHP"
                    else:
                        currency = " USD"
                    addExpenseB.text_input = addExpenseTxt + currency
                    addExpenseB.txt()
                elif removeBool:
                    if len(removeExpenseTxt) == 7 and keyboardinput(event) != "del":
                        pass
                    elif keyboardinput(event) == "del":
                        removeExpenseTxt = removeExpenseTxt[:-1]
                    elif keyboardinput(event) == None:
                        pass
                    elif keyboardinput(event) not in "1234567890.":
                        pass
                    else:
                        try:
                            if conversion and float(removeExpenseTxt + keyboardinput(event)) <= accounts[lastuserTxt].expenses[dateTxt].get(current_loc, 0):
                                removeExpenseTxt += keyboardinput(event)
                            elif float(removeExpenseTxt + keyboardinput(event)) <= accounts[lastuserTxt].expenses[dateTxt].get(current_loc, 0) / 55:
                                removeExpenseTxt += keyboardinput(event)
                        except:
                            try:
                                if conversion and float(removeExpenseTxt + keyboardinput(event) + "0") <= accounts[lastuserTxt].expenses[dateTxt].get(loc, 0):
                                    removeExpenseTxt += keyboardinput(event)
                                elif float(removeExpenseTxt + keyboardinput(event) + "0") <= accounts[lastuserTxt].expenses[dateTxt].get(current_loc, 0)/ 55:
                                    removeExpenseTxt += keyboardinput(event)
                            except:
                                pass

                    if conversion:
                        currency = " PHP"
                    else:
                        currency = " USD"
                    removeExpenseB.text_input = removeExpenseTxt + currency
                    removeExpenseB.txt()
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
                                lastuserTxt = ""
                            elif deleteButtons[1].check(mouse):
                                del accounts[keys[index + 1]]
                                lastuserTxt = ""
                            elif deleteButtons[2].check(mouse):
                                del accounts[keys[index + 2]]
                                lastuserTxt = ""
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
                            for user in accounts.values():
                                if user.chosen:
                                    user.chosen = False
                            accounts[inp[0]] = User(inp[0], int(inp[1]), 0, chosen=True)
                            lastuserTxt = inp[0]
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
