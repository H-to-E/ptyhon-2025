import pygame
import sys
import random

pygame.init()

screen_width = 800
screen_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

MAX_APPLES = 50
lives = 3
kill_count = 0
apple_count = 0
game_over = False

font = pygame.font.SysFont(None, 24)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('dukbird.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 10
        self.speed_x = 0

    def update(self):
        self.rect.x += self.speed_x
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, screen_width)

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('apple.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(0, screen_height - 60 - self.rect.height)
        self.rect.x = random.randint(-50, -10)
        self.speed_x = random.randint(1, 3)

    def update(self):
        self.rect.x += self.speed_x

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('alien.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(0, screen_height - 60 - self.rect.height)
        self.rect.x = random.randint(-50, -10)
        self.speed_x = random.randint(1, 3)

    def update(self):
        self.rect.x += self.speed_x

class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('spaceship.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(0, screen_height - 60 - self.rect.height)
        self.rect.x = random.randint(-50, -10)
        self.speed_x = random.randint(1, 3)

    def update(self):
        self.rect.x += self.speed_x


class MouseApple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('shot.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 20))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -2

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()


class Wall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, screen_height))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width - 60
        self.rect.y = 0


def spawn_apple():
    global apple_count
    if apple_count < MAX_APPLES:
        apple = Apple()
        all_sprites.add(apple)
        apples.add(apple)
        apple_count += 1
        spawn_alien()
        spawn_ship()
        
def spawn_alien():
    global apple_count
    if apple_count %5==0:
        alien = Alien()
        all_sprites.add(alien)
        aliens.add(alien)

def spawn_ship():
    global apple_count
    if apple_count %5==2:
        spaceship = Spaceship()
        all_sprites.add(spaceship)
        spaceships.add(spaceship)
        

def reset_game():
    global lives, kill_count, game_over, apple_count
    lives = 3
    kill_count = 0
    apple_count = 0
    game_over = False

    all_sprites.empty()
    apples.empty()
    bullets.empty()

    player = Player()
    wall = Wall()
    mouse_apple = MouseApple()

    all_sprites.add(player, wall, mouse_apple)

    for _ in range(10):
        spawn_apple()

    return player, wall, mouse_apple


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Apple Game")

pygame.mouse.set_visible(False)

all_sprites = pygame.sprite.Group()
apples = pygame.sprite.Group()
bullets = pygame.sprite.Group()
aliens=pygame.sprite.Group()
spaceships=pygame.sprite.Group()

player, wall, mouse_apple = reset_game()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player, wall, mouse_apple = reset_game()

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
                elif event.key == pygame.K_LEFT:
                    player.speed_x = -5
                elif event.key == pygame.K_RIGHT:
                    player.speed_x = 5

            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    player.speed_x = 0

            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for apple in apples:
                    if apple.rect.collidepoint(event.pos):
                        apple.kill()
                        kill_count += 1
                        spawn_apple()
                        break
                for alien in aliens:
                    if alien.rect.collidepoint(event.pos):
                        alien.kill()
                        break

    if not game_over:
        all_sprites.update()

        
        hits = pygame.sprite.groupcollide(apples, bullets, True, True)
        for _ in hits:
            kill_count += 1
            spawn_apple()
        
        hits_spaceship= pygame.sprite.groupcollide(spaceships,bullets,True,True)
        for _ in hits_spaceship:
            _.kill()

        
        for apple in list(apples):
            if apple.rect.right >= wall.rect.left:
                apple.kill()
                lives -= 1
                if lives <= 0:
                    game_over = True
                spawn_apple()
        for apple in list(aliens):
            if apple.rect.right >= wall.rect.left:
                apple.kill()
                lives -= 1
                if lives <= 0:
                    game_over = True
                spawn_apple()
        for apple in list(spaceships):
            if apple.rect.right >= wall.rect.left:
                apple.kill()
                lives -= 1
                if lives <= 0:
                    game_over = True
                spawn_apple()
    

    screen.fill((170, 200, 255))
    pygame.draw.rect(screen, (80, 170, 80),
                     (0, screen_height - 60, screen_width, 60))
    all_sprites.draw(screen)

    screen.blit(font.render(f"Score: {kill_count}", True, black), (10, 10))
    screen.blit(font.render(f"Lives: {lives}", True, black), (700, 10))
    screen.blit(font.render(f"Apples: {apple_count}/{MAX_APPLES}", True, black), (10, 30))

    if game_over and lives == 0 :
        text = font.render("GAME OVER (Press R)", True, red)
        screen.blit(text, (
            (screen_width - text.get_width()) // 2,
            (screen_height - text.get_height()) // 2
        ))
    if lives>=1 and len(apples) == 0:
        game_over= True
        text = font.render("GAME CLEAR!(Press R to replay)",True,black)
        screen.blit(text, (
            (screen_width - text.get_width()) // 2,
            (screen_height - text.get_height()) // 2
            
        ))
        

    pygame.display.flip()
    clock.tick(60) 

pygame.quit()
   


