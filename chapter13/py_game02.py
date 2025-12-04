import pygame

print('초기화 전 출력')

pygame.init()
print('파이게임 초기화 후 출력')

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('My Game')


pygame.quit()
print('파이게임 종료 후 출력')

