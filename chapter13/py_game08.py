import pygame

print('초기화 전 출력')

pygame.init()
print('파이게임 초기화 후 출력')

width=600
height=400
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('My Game')

clock=pygame.time.Clock()
img=pygame.image.load('chapter13\dukbird.png')
img=pygame.transform.scale(img,(50,50))
rect=img.get_rect()
rect.center=(width//2,height//2)
x,y=width//2,height//2
speed=1
size=40

running = True
while running==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print('event:quit')
            running=False
        if event.type==pygame.KEYDOWN:
            print('event:keydown',event.key)
        if event.type==pygame.KEYUP:
            print('event:ketup',event.key)
        if event.type==pygame.MOUSEBUTTONDOWN:
            print('event:mousebuttondown',event.pos)
        
    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
            rect.x-=speed
    if keys[pygame.K_RIGHT]:
            rect.x+=speed
    if keys[pygame.K_UP]:
            rect.y-=speed
    if keys[pygame.K_DOWN]:
            rect.y+=speed

    if rect.left<0:
        rect.left=0
    if rect.right>width:
        rect.right=width
    if rect.top<0:
        rect.top=0
    if rect.bottom>height:
        rect.bottom=height
        
    screen.fill((170,200,255))
    screen.blit(img,rect)

    pygame.draw.rect(screen,(80,170,80),(0,height-60,width,60))
    pygame.draw.rect(screen,(255,80,80),(50,280,40,40))
    pygame.draw.circle(screen,(0,255,0),(450,150),20)
    pygame.draw.line(screen,(0,0,0),(300,300),(500,300),5)


        
    pygame.display.flip()
    clock.tick(60)





pygame.quit()
print('파이게임 종료 후 출력')

