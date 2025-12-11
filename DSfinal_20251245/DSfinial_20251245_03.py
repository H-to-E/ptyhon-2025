import pygame
import sys
import random

pygame.init()


screen_width = 800
screen_height = 600


blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)




lives = 5
kill_count = 0
game_over = False


font = pygame.font.SysFont(None, 24)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('DSfinal_20251245\dukbird.png')
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 10
        self.speed_x = 0

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
            
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('DSfinal_20251245\\apple.png')
        self.image = pygame.transform.scale(self.image,(40,40))

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-50, -10)
        self.speed_y = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > screen_height:
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y = random.randint(-50, -10)
            self.speed_y = random.randint(1, 3)
            

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


def reset_game():
    global lives, kill_count, game_over, all_sprites, apples, bullets, player

    lives = 3                 
    kill_count = 0             
    game_over = False         

   
    all_sprites.empty()
    apples.empty()
    bullets.empty()

   
    player = Player()
    all_sprites.add(player)


    for _ in range(10):
        apple= Apple()
        all_sprites.add(apple)
        apples.add(apple)


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Apple")


all_sprites = pygame.sprite.Group()
apples = pygame.sprite.Group()
bullets = pygame.sprite.Group()

reset_game()  

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()

       
        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
                elif event.key == pygame.K_LEFT:
                    player.speed_x = -5
                elif event.key == pygame.K_RIGHT:
                    player.speed_x = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.speed_x = 0

  
    if not game_over:
        all_sprites.update()

       
        hits = pygame.sprite.groupcollide(apples, bullets, True, True)
        for hit in hits:
            apple = Apple()
            all_sprites.add(apple)
            apples.add(apple)
            kill_count += 1       

        
        if pygame.sprite.spritecollide(player, apples, True):
            lives -= 1            
            if lives <= 0:
                game_over = True  
       


    screen.fill((170,200,255))
    pygame.draw.rect(screen,(80,170,80),(0,screen_height-60,screen_width,60))

    all_sprites.draw(screen)


    ui_text = font.render(f"Scores: {kill_count}", True, black)
    screen.blit(ui_text, (10, 10))

    ui_text1 = font.render(f"Lives: {lives}", True, black)
    screen.blit(ui_text1, (700, 10))

 
    if game_over:
        over_text = font.render("GAME OVER(Press R to Reset)", True, red)
        x = (screen_width - over_text.get_width()) // 2
        y = (screen_height - over_text.get_height()) // 2
        screen.blit(over_text, (x, y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()