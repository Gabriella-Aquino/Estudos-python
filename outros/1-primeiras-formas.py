import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 500
altura = 400

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Primeiras Formas :3')

while True:
    for event in pygame.event.get():
        if event.type ==  QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(tela, (200, 0, 0), (100, 100, 200, 100))#tela rgb x,y,w,h
    pygame.draw.circle(tela, (0, 0, 200), (350, 300), 50) #tela rgb x,y raio
    pygame.draw.line(tela, (200, 200, 0), (450,350), (450,50), 3) #tela rgb p_inicial(x,y) P_final(x,y) espessura
    pygame.display.update()