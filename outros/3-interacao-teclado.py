import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 400
altura = 350
x = (largura - 25)/2
y = (altura - 30)/2
relogio = pygame.time.Clock()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Primeira animação')

while True:
    relogio.tick(30)
    tela.fill((0,0,0)) #rgb
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''if event.type == KEYDOWN:
            if event.key == K_a:
                x += -20
            if event.key == K_d:
                x += 20
            if event.key == K_w:
                y += -20
            if event.key == K_s:
                y += 20'''
                                      #   para as setas
    if pygame.key.get_pressed()[K_a]: # K_LEFT
        x += -10
    if pygame.key.get_pressed()[K_d]: # K_RIGHT
        x += 10
    if pygame.key.get_pressed()[K_w]: # K_UP
        y += -10
    if pygame.key.get_pressed()[K_s]: # K_DOWN
        y += 10

    pygame.draw.rect(tela, (200, 0, 0), (x, y, 25, 30))
  

    pygame.display.update()