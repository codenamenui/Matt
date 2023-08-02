import pygame, sys, json
from classes import Button
from datetime import datetime

# Date Time
def is_valid_date_format(date_string, date_format):
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False

# Set the Font Style and Size to be Used
def get_font(size):
    return pygame.font.Font("Milky Again.ttf", size)

def keyboardinput(event):
    if (event.unicode.isalpha() or event.unicode.isdigit()):
        return event.unicode
    elif event.key == pygame.K_BACKSPACE:
        return "del"
    elif event.key == pygame.K_SPACE:
        return ' '
    elif event.key == pygame.K_PERIOD:
        return '.'
    elif event.key == pygame.K_COMMA:
        return ','
    elif event.key == pygame.K_EXCLAIM:
        return '!'
    elif event.key == pygame.K_QUESTION:
        return '?'
    elif event.key == pygame.K_COLON:
        return ':'
    elif event.key == pygame.K_SEMICOLON:
        return ';'
    elif event.key == pygame.K_QUOTE:
        return "'"
    elif event.key == pygame.K_QUOTEDBL:
        return '"'
    elif event.key == pygame.K_MINUS:
        return '-'
    elif event.key == pygame.K_UNDERSCORE:
        return '_'
    elif event.key == pygame.K_SLASH:
        return '/'
    elif event.key == pygame.K_HASH:
        return '#'
    elif event.key == pygame.K_AT:
        return '@'

def add(bufname1, bufname2, screen, S_WIDTH, clock, textColor, bgColor, darkMode):
    bufbool1 = False
    bufbool2 = False
    buftxt1 = ""
    buftxt2 = ""
    if darkMode:
        hover = (200, 200, 200)
    else:
        hover = textColor
    buf1 = Button(pygame.Rect(0, 0, 300, 50), (S_WIDTH//2, 260), get_font(
        20), bufname1, (100, 100, 100), color=bgColor, hovering_color=hover)
    buf2 = Button(pygame.Rect(0, 0, 300, 50), (S_WIDTH//2, 360), get_font(
        20), bufname2, (100, 100, 100), color=bgColor, hovering_color=hover)
    cancel = Button(pygame.Rect(0, 0, 30, 40), (632, 191), get_font(
        20), color=bgColor)
    submit = Button(pygame.Rect(0, 0, 100, 50), (S_WIDTH//2, 470), get_font(
        20), "Submit", textColor, color=bgColor, hovering_color=hover)

    bufborder1 = Button(pygame.Rect(0, 0, 310, 60), (S_WIDTH//2, 360), get_font(
        20), "", (100, 100, 100), color=textColor)
    bufborder2 = Button(pygame.Rect(0, 0, 310, 60), (S_WIDTH//2, 260), get_font(
        20), "", (100, 100, 100), color=textColor)
    submitborder = Button(pygame.Rect(0, 0, 110, 60), (S_WIDTH//2, 470), get_font(
        20), "", color=textColor)

    con = True
    while con:
        border = pygame.Rect(0, 0, 410, 410)
        border.center = (S_WIDTH//2, 360)
        pygame.draw.rect(screen, textColor, border)
        box = pygame.Rect(0, 0, 400, 400)
        box.center = (S_WIDTH//2, 360)
        pygame.draw.rect(screen, bgColor, box)

        # Getting Mouse Coords
        mouse_pos = pygame.mouse.get_pos()

        for button in [bufborder1, bufborder2, submitborder, buf1, buf2, submit]:
             button.changeColor(mouse_pos)
             button.update(screen)

        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
             if event.type == pygame.MOUSEBUTTONDOWN:
                 if cancel.check(mouse_pos):
                     pygame.display.flip()
                     return None
                 elif buf1.check(mouse_pos):
                     buf1.base_color = textColor
                     bufbool1 = True
                     bufbool2 = False
                     buf1.text_input = buftxt1
                 elif buf2.check(mouse_pos):
                     buf2.base_color = textColor
                     bufbool1 = False
                     bufbool2 = True
                     buf2.text_input = buftxt2
                 elif submit.check(mouse_pos) and len(buftxt1) > 0 and len(buftxt2) > 0:
                     return (buftxt1, buftxt2)
             if event.type == pygame.KEYDOWN:
                 if bufbool1:
                     if len(buftxt1) == 20 and keyboardinput(event) != "del":
                         pass
                     elif keyboardinput(event) == None:
                         pass
                     elif keyboardinput(event) != "del":
                         buftxt1 += keyboardinput(event)
                     else:
                         buftxt1 = buftxt1[:-1]
                     buf1.text_input = buftxt1
                     buf1.txt()
                 elif bufbool2:
                     print(keyboardinput(event))
                     if len(buftxt2) == 7 and keyboardinput(event) != "del":
                         pass
                     elif keyboardinput(event) == "del":
                         buftxt2 = buftxt2[:-1]
                     elif keyboardinput(event) == None:
                         pass
                     elif keyboardinput(event) not in "1234567890":
                         pass
                     elif keyboardinput(event) != "del":
                         buftxt2 += keyboardinput(event)
                     buf2.text_input = buftxt2
                     buf2.txt()
        
        if darkMode:
            screen.blit(pygame.transform.scale(pygame.image.load("cross-white.svg"), (30, 40)), (617, 171))
        else:
            screen.blit(pygame.transform.scale(pygame.image.load("cross.svg"), (30, 40)), (617, 171))
        # Update Screen
        clock.tick(60)
        pygame.display.flip()

def prompt(txt, screen, S_WIDTH, clock, textColor, bgColor):
    con = True
    while con:
        t1 = get_font(25).render(txt, True, textColor)
        t2 = t1.get_rect(center=(S_WIDTH//2, 360))
        border = pygame.Rect(0,0, S_WIDTH//2 - 40, 90)
        border.center = (S_WIDTH//2, 360)
        pygame.draw.rect(screen, textColor, border)
        temprect = pygame.Rect(0,0, S_WIDTH//2 - 50, 80)
        temprect.center = (S_WIDTH//2, 360)
        pygame.draw.rect(screen, bgColor, temprect)
        screen.blit(t1, t2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return
        # Limit Updates per Second to 300
        clock.tick(60)
        # Update Screen
        pygame.display.flip()

def split_description(description, words_per_chunk=5):
    words = description.split()
    return [' '.join(words[i:i+words_per_chunk]) for i in range(0, len(words), words_per_chunk)]

def save(accounts):
    accounts = {key: user.__dict__ for key, user in accounts.items()}
    with open("accounts.json", "w") as f:
        json.dump(accounts, f, indent=4)

def saveSettings(conversion, tutorial, darkMode):
    settings = {'conversion' : conversion, 'tutorial' : tutorial, 'darkMode' : darkMode}
    with open("settings.json", "w") as f:
        json.dump(settings, f, indent=4)

def tutor(num, texts, screen, S_WIDTH, clock, textColor, bgColor):
    con = True
    while con:
        border = pygame.Rect(0,0, S_WIDTH//2 - 40, 300)
        border.center = (S_WIDTH//2, 360)
        pygame.draw.rect(screen, textColor, border)
        temprect = pygame.Rect(0,0, S_WIDTH//2 - 50, 290)
        temprect.center = (S_WIDTH//2, 360)
        pygame.draw.rect(screen, bgColor, temprect)
        if num == 1:
            for i, txt in enumerate(texts):
                t1 = get_font(15).render(txt, True, textColor)
                t2 = t1.get_rect(center=(S_WIDTH//2, 260 + 50 * i))
                screen.blit(t1, t2)
        elif num == 2:
            for i, txt in enumerate(texts):
                t1 = get_font(15).render(txt, True, textColor)
                t2 = t1.get_rect(center=(S_WIDTH//2, 260 + 35 * i))
                screen.blit(t1, t2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return
        # Limit Updates per Second to 300
        clock.tick(60)
        # Update Screen
        pygame.display.flip()