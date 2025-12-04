import pygame

print('초기화 전 출력')

pygame.init()
print('파이게임 초기화 후 출력')

screen=pygame.display.set_mode((600,400))
pygame.display.set_caption('My Game')

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



screen.fill((200,200,200))
pygame.display.flip()

pygame.quit()
print('파이게임 종료 후 출력')

