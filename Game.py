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

        player = Player.Player(x=400, y=580)
        self.__players.add(player)
        self.__running = True
        self.createPlatforms()

        self.__camera_offset = 0
    

    def playground(self):
        self.__screen.fill("lightblue")

    def createPlatforms(self):
        platy = 600
        last_x = 640  # Center of the screen
        for _ in range(60):  # Increased from 30 to 60
            min_x = max(200, last_x - 150)
            max_x = min(1080, last_x + 150)
            x = random.randint(min_x, max_x)
            platform = Platform.Platform((0, 128, 0), 100, 20, x=x, y=platy)
            self.__platforms.add(platform)
            platy -= random.randint(70, 110)
            last_x = x

    def showGameOverScreen(self):
        font       = pygame.font.SysFont(None, 72)
        small_font = pygame.font.SysFont(None, 48)
        text  = font.render("You Died", True, (255, 0, 0))
        info  = small_font.render("Press Enter to Respawn", True, (255, 255, 255))

        waiting = True
        while waiting and self.__running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                    waiting = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        waiting = False

            self.__screen.fill("black")
            self.__screen.blit(text, (640 - text.get_width() // 2, 300))
            self.__screen.blit(info, (640 - info.get_width()  // 2, 400))
            pygame.display.flip()
            self.__clock.tick(15)

        if self.__running:
            print("→ Respawning…")
            self.respawn()

                
    def respawn(self):
        self.__platforms.empty()
        self.__players.empty()
        ground = Platform.Platform((0,128,0), 1280, 40, x=0, y=680)
        self.__platforms.add(ground)
        self.createPlatforms()
        player = Player.Player(x=640, y=580)
        self.__players.add(player)
        self.__camera_offset = 0

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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
    
            self.playground()
            self.__players.update(self.__dt, self.__platforms)
    
            player = next(iter(self.__players))
            if player.rect.top < 360:
                diff = 360 - player.rect.top
                self.__camera_offset += diff
                for sprite in self.__platforms:
                    sprite.rect.y += diff
                for sprite in self.__players:
                    sprite.rect.y += diff
    
            if player.rect.top > 720:
                self.showGameOverScreen()
    
            self.__platforms.draw(self.__screen)
            self.__players.draw(self.__screen)
    
            pygame.display.flip()
            self.__dt = self.__clock.tick(60) / 1000
    
        pygame.quit()



if __name__ == "__main__":
    game = Game()
    game.startGame()