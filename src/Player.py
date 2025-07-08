import pygame

class Player:
    def __init__(self):
        pass

    def shape(self, screen, player_pos):
        return pygame.draw.circle(screen, "red", player_pos, 40)