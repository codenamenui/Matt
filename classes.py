import pygame

class Button:
    def __init__(self, image, pos, font, text_input = "", base_color = "#FFFFFF", hovering_color = "black", color="white", picked=False):
        self.image = image
        self.color = color
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        elif isinstance(self.image, pygame.Surface):
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        elif isinstance(self.image, pygame.Rect):
            self.rect = self.image
            self.rect.center = (self.x_pos, self.y_pos)
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.picked = picked

    def txt(self):
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        if isinstance(self.image, pygame.Surface):
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        if isinstance(self.image, pygame.Rect):
            self.rect = self.image
            self.rect.center = (self.x_pos, self.y_pos)
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        
    def update(self, screen, color=None):
        if isinstance(self.image, pygame.Surface):
            screen.blit(self.image, self.rect)
        elif isinstance(self.image, pygame.Rect) and color == None:
            pygame.draw.rect(screen, self.color, self.rect)
        elif isinstance(self.image, pygame.Rect) and color != None:
            pygame.draw.rect(screen, color, self.rect)
        screen.blit(self.text, self.text_rect)

    def check(self, position):
        return self.rect.collidepoint(position)
    
    def changeColor(self, position):
        if self.rect.collidepoint(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    def border(self, screen, color):
        rect = self.rect
        rect.top -= 3
        rect.left -= 3
        rect.width += 6
        rect.height += 6
        pygame.draw.rect(screen, color, rect)
        rect.width -= 6
        rect.height -= 6
        rect.top += 3
        rect.left += 3

    def circle(self, screen, color="red"):
        circle = self.rect.center
        pygame.draw.circle(screen, color, circle, 15, width=4)

class User:
    def __init__(self, username, remaining, spent, chosen=False, expenses={}):
        self.username = username
        self.remaining = remaining
        self.spent = spent
        self.chosen = chosen
        self.expenses = expenses