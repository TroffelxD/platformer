import pygame 

GRAVITY = 1500  
JUMP_VELOCITY = -600

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width=50, height=50, color=(200,50,50)):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

        self.vel = pygame.Vector2(0, 0)
        self.on_ground = False

    def update(self, dt, platforms):
        if not self.on_ground:
            self.vel.y += GRAVITY * dt

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.vel.x = -300
        elif keys[pygame.K_d]:
            self.vel.x = 300
        else:
            self.vel.x = 0

        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel.y = JUMP_VELOCITY
            self.on_ground = False

        self.rect.x += int(self.vel.x * dt)
        self._check_collision(platforms, dx=True)
        self.rect.y += int(self.vel.y * dt)
        self.on_ground = False
        self._check_collision(platforms, dx=False)
    
    def _check_collision(self, platforms, dx):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        for platform in hits:
            if dx:
                if self.vel.x > 0:
                    self.rect.right = platform.rect.left
                elif self.vel.x < 0:
                    self.rect.left = platform.rect.right
                self.vel.x = 0
            else:
                if self.vel.y > 0:
                    self.rect.bottom = platform.rect.top
                    self.on_ground = True
                elif self.vel.y < 0:
                    self.rect.top = platform.rect.bottom
                self.vel.y = 0