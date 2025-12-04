import pygame

print('초기화 전 출력')

pygame.init()
print('파이게임 초기화 후 출력')

width=600
height=400
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('My Game')

clock=pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('chapter13\dukbird.png')
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()
        self.rect.center=(width//2,height//2)
        self.speed=1
    def update(self):
        keys=pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x-=self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x+=self.speed
        if keys[pygame.K_UP]:
            self.rect.y-=self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y+=self.speed

        self.rect.clamp_ip(screen.get_rect())

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.Surface((40,40))
        self.image.fill((255,80,80))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.spped_x=2

    def update(self):
        self.rect.x+=self.spped_x
        if self.rect.left<50 or self.rect.right>200:
            self.spped_x*=-1

all_sprites=pygame.sprite.Group()
enemy_group=pygame.sprite.Group()

player=Player()
all_sprites.add(player)

enemy=Enemy(50,260)
all_sprites.add(enemy)
enemy_group.add(enemy)

coin_rect=pygame.Rect(430,130,40,40)
score=0

running = True
game_over = False

while running==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
   
    if not game_over:
        all_sprites.update()

        if player.rect.colliderect(coin_rect):
            score+=1
            if score%2==0:
                coin_rect.x=430
            else:
                coin_rect.x=350
        hits=pygame.sprite.spritecollide(player,enemy_group,False)
        if hits:
            print('적과 충돌! 게임 오버')
            game_over=True

    screen.fill((170,200,255))
    pygame.draw.rect(screen,(80,170,80),(0,height-60,width,60))
    
    
    pygame.draw.circle(screen,(0,255,0),(coin_rect.x + coin_rect.width // 2, coin_rect.y + coin_rect.height // 2),20)
    pygame.draw.line(screen,(0,0,0),(300,300),(500,300),5)

    font=pygame.font.SysFont(None,24)
    text=font.render(f'Score:{score}',True,(0,0,0))
    screen.blit(text,(10,10))

    all_sprites.draw(screen)
        
    pygame.display.flip()
    clock.tick(60)





pygame.quit()
print('파이게임 종료 후 출력')

