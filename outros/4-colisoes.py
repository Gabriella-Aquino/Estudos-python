import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 400
altura = 350
x = (largura - 25)/2
y = (altura - 30)/2

x_azul = randint(40, 360) 
y_azul = randint(50, 300)

relogio = pygame.time.Clock()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Colisão')

while True:
    relogio.tick(30)
    tela.fill((0,0,0)) #rgb
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
                                      #   para as setas
    if pygame.key.get_pressed()[K_a]: # K_LEFT
        x += -10
    if pygame.key.get_pressed()[K_d]: # K_RIGHT
        x += 10
    if pygame.key.get_pressed()[K_w]: # K_UP
        y += -10
    if pygame.key.get_pressed()[K_s]: # K_DOWN
        y += 10

    rect_vermelho = pygame.draw.rect(tela, (200, 0, 0), (x, y, 25, 30))
    rect_azul = pygame.draw.rect(tela, (0,0,200), (x_azul, y_azul, 25, 30))

    if rect_vermelho.colliderect(rect_azul):
        x_azul = randint(40, 360) 
        y_azul = randint(50, 300)

    pygame.display.update()