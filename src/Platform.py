import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()  
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
