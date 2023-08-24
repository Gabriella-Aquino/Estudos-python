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

pontos = 0
fonte = pygame.font.SysFont('arial', 25, True, False) #'nome_fonte', tamanho_px, negrito_TF, italico_TF

relogio = pygame.time.Clock()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Gerando Textos')

while True:
    relogio.tick(30)
    tela.fill((0,0,0)) #rgb
    mensagem = f'pontos: {pontos}'
    txt_formatado = fonte.render(mensagem, True, (255,255,255)) #var_mensagem, !pixelado_TF, rgb
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
                                      
    if pygame.key.get_pressed()[K_a]: 
        x += -10
    if pygame.key.get_pressed()[K_d]: 
        x += 10
    if pygame.key.get_pressed()[K_w]: 
        y += -10
    if pygame.key.get_pressed()[K_s]: 
        y += 10

    rect_vermelho = pygame.draw.rect(tela, (200, 0, 0), (x, y, 25, 30))
    rect_azul = pygame.draw.rect(tela, (0,0,200), (x_azul, y_azul, 25, 30))

    if rect_vermelho.colliderect(rect_azul):
        x_azul = randint(40, 360) 
        y_azul = randint(50, 300)
        pontos += 1

    tela.blit(txt_formatado, (250, 10)) #var_txt_formatado, (x,y)
    pygame.display.update()