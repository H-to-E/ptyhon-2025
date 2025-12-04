import pygame

print('초기화 전 출력')

pygame.init()
print('파이게임 초기화 후 출력')

width=600
height=400
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('My Game')

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
            x-=speed
    if keys[pygame.K_RIGHT]:
            x+=speed
    if keys[pygame.K_UP]:
            y-=speed
    if keys[pygame.K_DOWN]:
            y+=speed

    if x<0:
        x=0
    if x>width-size:
        x=width-size
    if y<0:
        y=0
    if y>height-size:
        y=width-size
        
    screen.fill((200,200,200))
    pygame.draw.rect(screen,(0,0,255),(x,y,size,size))
        
    pygame.display.flip()





pygame.quit()
print('파이게임 종료 후 출력')

