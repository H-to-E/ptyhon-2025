import pygame
import random # 랜덤 위치/움직임을 위해 필수

pygame.init()
pygame.mixer.init() # 사운드 초기화

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Final Exam Prep: Sprite Interaction")

clock = pygame.time.Clock()

# --- 사운드 로드 (파일이 없으면 에러가 나므로 예외처리 함) ---
try:
    # 실제 wav 파일이 있다면 경로를 적어주세요.
    coin_sound = pygame.mixer.Sound("coin.wav") 
    hit_sound = pygame.mixer.Sound("hit.wav")
except:
    print("사운드 파일이 없습니다. 소리 없이 실행됩니다.")
    coin_sound = None
    hit_sound = None

# 1. 플레이어 클래스
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 이미지 로드 (없을 경우를 대비해 초록색 사각형으로 대체 코드 작성)
        try:
            self.image = pygame.image.load("dukbird.png")
            self.image = pygame.transform.scale(self.image, (50, 50))
        except:
            self.image = pygame.Surface((50, 50))
            self.image.fill((0, 255, 0)) # 녹색 네모
            
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5
        self.hp = 3 # 플레이어 체력 변수

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        
        self.rect.clamp_ip(screen.get_rect())

# 2. 아이템(사과) 클래스: 가만히 있고 획득하면 사라짐
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 빨간색 사과 (이미지 대신 색상으로 표현)
        self.image = pygame.Surface((20, 20)) 
        self.image.fill((255, 0, 0)) 
        self.rect = self.image.get_rect()
        
        # 화면 내 랜덤한 위치에 생성
        self.rect.x = random.randrange(0, WIDTH - 20)
        self.rect.y = random.randrange(0, HEIGHT - 20)

# 3. 적(Enemy) 클래스: 스스로 움직이고 벽에 튕김
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 파란색 적
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        
        # 랜덤 위치
        self.rect.x = random.randrange(0, WIDTH - 40)
        self.rect.y = random.randrange(0, HEIGHT - 40)
        
        # 랜덤 속도 (방향: -3 ~ 3 사이, 0 제외)
        self.dx = random.choice([-3, -2, -1, 1, 2, 3])
        self.dy = random.choice([-3, -2, -1, 1, 2, 3])

    def update(self):
        # 스스로 움직임
        self.rect.x += self.dx
        self.rect.y += self.dy

        # 벽에 닿으면 방향 반대로 (튕기기)
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.dx *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.dy *= -1

# --- 그룹 생성 ---
all_sprites = pygame.sprite.Group()
items = pygame.sprite.Group()   # 충돌 체크를 편하게 하기 위해 별도 그룹 생성
enemies = pygame.sprite.Group() # 적 그룹

# 플레이어 생성
player = Player()
all_sprites.add(player)

# 사과 10개 생성 (for문 사용)
for i in range(10):
    a = Apple()
    all_sprites.add(a)
    items.add(a)

# 적 5마리 생성
for i in range(5):
    e = Enemy()
    all_sprites.add(e)
    enemies.add(e)

# 게임 변수
score = 0
running = True

# --- 게임 루프 ---
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 1. 모든 스프라이트 움직임 갱신 (player, apple, enemy 모두 호출됨)
    all_sprites.update()

    # 2. 충돌 처리 (핵심!)
    
    # (A) 플레이어 vs 사과 (True: 닿으면 사과(item)를 삭제함)
    # spritecollide(대상, 그룹, 삭제여부)
    hits_list = pygame.sprite.spritecollide(player, items, True)
    for hit in hits_list:
        # 충돌한 개수만큼 점수 증가
        score += 10
        print(f"사과 획득! 현재 점수: {score}")
        if coin_sound: coin_sound.play() # 사운드 재생

    # (B) 플레이어 vs 적 (False: 닿아도 적을 삭제하지 않음)
    hits_enemy = pygame.sprite.spritecollide(player, enemies, False)
    if hits_enemy:
        # 적과 닿았을 때 로직
        player.hp -= 1
        print(f"충돌! 체력 감소: {player.hp}")
        if hit_sound: hit_sound.play()
        
        # 충돌 후 플레이어를 안전한 곳(중앙)으로 옮기거나 잠시 무적 시간을 주는 등의 처리
        player.rect.center = (WIDTH // 2, HEIGHT // 2)
        
        if player.hp <= 0:
            print("GAME OVER")
            running = False

    # --- 그리기 ---
    screen.fill((170, 200, 255))
    
    all_sprites.draw(screen) # 모든 스프라이트(플레이어, 사과, 적) 한번에 그리기

    # 점수 표시 (간단히 윈도우 제목에 표시, 시험에선 폰트 사용 요구할 수도 있음)
    pygame.display.set_caption(f"Score: {score} | HP: {player.hp}")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
