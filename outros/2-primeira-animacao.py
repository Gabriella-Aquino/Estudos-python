import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 400
altura = 350
x = (largura - 25)/2
y = 0
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

    pygame.draw.rect(tela, (200, 0, 0), (x, y, 25, 30))
    y += 2.5
    if y >= altura:
        y = 0

    pygame.display.update()