import pygame
import random
from src import Player
from src import Platform

class Game:

    def __init__(self):
        self.__screen = pygame.display.set_mode((1280, 720))
        self.__clock = pygame.time.Clock()

        self.__platforms = pygame.sprite.Group()
        self.__players = pygame.sprite.Group()

        ground = Platform.Platform((0,128,0), 1280, 40, x=0, y=680)
        self.__platforms.add(ground)

        self.__dt = 0

        player = Player.Player(x=100, y=100)
        self.__players.add(player)
        self.__running = True
        self.createPlatforms()
    

    def playground(self):
        self.__screen.fill("lightblue")

    def createPlatforms(self):
        for i in range(20):
            platform = Platform.Platform((0, 0, 0), 100, 20, x=random.uniform(100, 1000), y=random.uniform(40, 600))
            self.__platforms.add(platform)

    #def outOfBounce(self):
    #    if self.__player_pos.x >= 1280:
    #        self.__player_pos.x = 1
    #    if self.__player_pos.x <= 0:
    #        self.__player_pos.x = 1279

    #def gravity(self):
    #    if self.__player_pos.y <= 610:
    #        self.__player_pos.y += 500 * self.__dt


    def startGame(self):
        pygame.init()
        while self.__running:
            for event in  pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False


            self.playground()
            #self.outOfBounce()
            self.__players.update(self.__dt, self.__platforms)
            self.__platforms.draw(self.__screen)
            self.__players.draw(self.__screen)



            pygame.display.flip()
            self.__dt = self.__clock.tick(60) / 1000  

        pygame.quit()



if __name__ == "__main__":
    game = Game()
    game.startGame()