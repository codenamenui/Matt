import pygame

class Button:
    def __init__(self, image, pos, font, text_input = "", base_color = "#FFFFFF", hovering_color = "black", color="white"):
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
        
    def update(self, screen):
        if isinstance(self.image, pygame.Surface):
            screen.blit(self.image, self.rect)
        if isinstance(self.image, pygame.Rect):
            pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text, self.text_rect)

    def check(self, position):
        return self.rect.collidepoint(position)
    
    def changeColor(self, position):
        if self.rect.collidepoint(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
    
