import pygame
import random
from pygame.locals import *
import time

pygame.init()
pygame.font.init()
fonte_t = pygame.font.Font('fonte2.ttf', 44)

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

pygame.mixer.music.set_volume(0.90)
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play(-1)

largura = 1000
altura = 600

fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("TUIF")
tamanho = (largura, altura)
imagem_original = pygame.image.load('./paginainicial.png').convert()
imagem = pygame.transform.scale(imagem_original, tamanho)
fundo.blit(imagem, (0, 0))
imagemgameover = pygame.image.load('imagemdematricula.png')
imagemgameover = pygame.transform.scale(imagemgameover, tamanho)

p = 60
relogio = pygame.time.Clock()
contador = 0
segundos = 120

pygame.display.flip()
sair_fundo_entrada = False
click = False

while not sair_fundo_entrada:
    fundo.blit(imagem, (0, 0))
    mx, my = pygame.mouse.get_pos()

    button_start = pygame.Rect(430, 380, 120, 120)
    if button_start.collidepoint((mx, my)):
        start_imagem = pygame.image.load('start cortado2.png')
        if click:
            sair_fundo_entrada = True
    else:
        start_imagem = pygame.image.load('start cortado.png')
    fundo.blit(start_imagem, ((160, 160)))
    event = pygame.event.poll()
    if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
            click = True

    pygame.display.update()

fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("TUIF")
tamanho = (largura, altura)
imagem_original = pygame.image.load('./nivel1.png').convert()
imagem = pygame.transform.scale(imagem_original, tamanho)
fundo.blit(imagem, (0, 0))

pygame.display.flip()
sair_fundo_entrada = False
while not sair_fundo_entrada:
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN:
        sair_fundo_entrada = event.key == pygame.K_RIGHT 
    pygame.display.flip()
fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("TUIF")
tamanho = (largura, altura)
imagem_original = pygame.image.load('./nivel1-2.png').convert()
imagem = pygame.transform.scale(imagem_original, tamanho)
fundo.blit(imagem, (0, 0))


pygame.display.flip()
sair_fundo_entrada = False
while not sair_fundo_entrada:
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN:
        sair_fundo_entrada = event.key == pygame.K_RIGHT
      
fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("TUIF")
tamanho = (largura, altura)
imagem_original = pygame.image.load('./nivel1-3.png').convert()
imagem = pygame.transform.scale(imagem_original, tamanho)
fundo.blit(imagem, (0, 0))

pygame.display.flip()
sair_fundo_entrada = False
while not sair_fundo_entrada:
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN:
        sair_fundo_entrada = event.key == pygame.K_RIGHT

pygame.mixer.music.set_volume(0.80)
fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("TUIF")
tamanho = (largura, altura)
imagem_original = pygame.image.load('./nivel1palavra (1).png').convert()
imagem = pygame.transform.scale(imagem_original, tamanho)
fundo.blit(imagem, (0, 0))

palavrasnivel1 = ['FEDERAL', 'QUADRA', 'CAMPO', 'INFOWEB', 'REFEITORIO', 'DIATINF', 'MINORA', 'DANI', 'GINASIO','TAPETE VERMELHO','AUDITORIO','PISCINAS','AREIA','ROSQUINHAS','CNAT','DIAREN','DIACON','DIACIN']
tentativas_de_letras = [' ', '-']
palavra_escolhida = ''
palavra_camuflada = ' '
sair = True
chance = 0
letra = ''
acertos=0

def sobre(texto, fundo, cor, largura):
    fonte_name = pygame.font.get_default_font()
    fonte = pygame.font.Font(fonte_name, 40)
    texto = fonte.render(texto, True, branco)
    texto_retangulo = texto.get_rect()
    texto_retangulo.center = (460, 200)
    fundo.blit(texto, texto_retangulo)
  
def elida(texto, fundo, cor, largura):
    fonte_name = pygame.font.get_default_font()
    fonte = pygame.font.Font(fonte_name, 15)
    texto = fonte.render(texto, True, cor)
    texto_retangulo = texto.get_rect()
    texto_retangulo.center = (890, 290)
    fundo.blit(texto, texto_retangulo)

def acerto(texto, fundo, cor, largura):
    fonte_name = pygame.font.get_default_font()
    fonte = pygame.font.Font(fonte_name, 40)
    texto = fonte.render(texto, True, cor)
    texto_retangulo = texto.get_rect()
    texto_retangulo.center = (220, 540)
    fundo.blit(texto, texto_retangulo)


def escreve(texto, fundo, cor, largura):
    fonte_name = pygame.font.get_default_font()
    fonte = pygame.font.Font(fonte_name, 40)
    texto = fonte.render(texto, True, cor)
    texto_retangulo = texto.get_rect()
    texto_retangulo.center = (180, 500)
    fundo.blit(texto, texto_retangulo)


def desenho_da_forca(fundo, chance):
    if chance >= 6:
        imagem_original = pygame.image.load('./xvermelho.png')
        imagem = pygame.transform.scale(imagem_original, (75, 75))
        fundo.blit(imagem, (190, 350))
    if chance >= 5:
        imagem_original = pygame.image.load('./xvermelho.png')
        imagem = pygame.transform.scale(imagem_original, (75, 75))
        fundo.blit(imagem, (110, 350))
    if chance >= 4:
        imagem_original = pygame.image.load('./xvermelho.png')
        imagem = pygame.transform.scale(imagem_original, (75, 75))
        fundo.blit(imagem, (20, 350))
    if chance >= 3:
        imagem_original = pygame.image.load('./xvermelho.png')
        imagem = pygame.transform.scale(imagem_original, (75, 75))
        fundo.blit(imagem, (190, 235))
    if chance >= 2:
        imagem_original = pygame.image.load('./xvermelho.png')
        imagem = pygame.transform.scale(imagem_original, (75, 75))
        fundo.blit(imagem, (110, 235))
    if chance >= 1:
        imagem_original = pygame.image.load('./xvermelho.png')
        imagem = pygame.transform.scale(imagem_original, (75, 75))
        fundo.blit(imagem, (20, 235))


def botao_de_novamente(fundo, tempo_restante):
    if chance >= 6:
        imagem_original = pygame.image.load('./imagemdegameover.png')
        imagem = pygame.transform.scale(imagem_original, (largura, altura))
        fundo.blit(imagem, (0, 0))


def sorteando_palavra(palavrasnivel1, palavra_escolhida, sair, dica):
    if sair == True:
        palavra_n = random.randint(0, len(palavrasnivel1) - 1)
        palavra_escolhida = palavrasnivel1[palavra_n]
        sair = False
    return palavra_escolhida, sair


def camuflando_palavra(palavra_escolhida, palavra_camuflada,
                       tentativas_de_letras):
    palavra_camuflada = palavra_escolhida
    for n in range(len(palavra_camuflada)):
        if palavra_camuflada[n:n + 1] not in tentativas_de_letras:
            palavra_camuflada = palavra_camuflada.replace(
                palavra_camuflada[n], "*")
    return palavra_camuflada


def tentando_uma_letra(tentativas_de_letras, palavra_escolhida, letra, chance):
    if letra not in tentativas_de_letras:
        tentativas_de_letras.append(letra)
        if letra not in palavra_escolhida:
            chance += 1
    elif letra in tentativas_de_letras:
        pass
    return tentativas_de_letras, chance


def palavra_do_jogo(fundo, palavra_camuflada):
    fonte_name = pygame.font.get_default_font()
    fonte = pygame.font.Font(fonte_name, 50)
    palavra = fonte.render(palavra_camuflada, True, branco)
    fundo.blit(palavra, (300, 350))


def botao_do_final(palavra_camuflada, sair, chance, letra,
                   tentativas_de_letras):
    if chance >= 6:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                tentativas_de_letras = [' ', '-']
                sair = True
                chance = 0
                letra = ' '
    return sair, chance, tentativas_de_letras, letra


def proximo_nivel(palavra_camuflada, sair, fundo, chance, letra,
                  tentativas_de_letras,acertos):
    count = 0
    limite = len(palavra_camuflada)
    for n in range(len(palavra_camuflada)):
        if palavra_camuflada[n] != '*':
            count += 1
    if count == limite:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                tentativas_de_letras = [' ', '-']
                sair = True
                chance = 0
                letra = ' '
    return sair, chance, tentativas_de_letras, letra

def final(acertos):
  if acertos>=10:
    pygame.mixer.music.set_volume(0.90)
    imagem_original = pygame.image.load('./imagemdeparabens.png')
    imagem = pygame.transform.scale(imagem_original, (largura, altura))
    fundo.blit(imagem, (0, 0))


tempo_restante = 0

#hora = "3:00"
#fonte_t = pygame.font.Font('fonte2.ttf', 44)
#temptela = fonte_t.render(hora, 1, preto)

while True:

    relogio.tick(p)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            letra = str(pygame.key.name(event.key)).upper()
            print(letra)
        fala=str(" ")
        dica = str(" ")
        if palavra_escolhida == str("FEDERAL"):
            dica = str("O IF é um instituto...")
            fala = str(" Essa é facil!")
        if palavra_escolhida == str("QUADRA") or palavra_escolhida == str("AREIA") :
            dica = str("O volei pode ser praticado na...")
            fala = str("Gosto muito rsrs")
        if palavra_escolhida == str("CAMPO"):
            dica = str("Local onde o futebol pode ser pratiado.")
            fala = str("Olha o pombo :p")
        if palavra_escolhida == str("INFOWEB"):
            dica = str("Melhor curso")
            fala = str("Amo muito <3")
        if palavra_escolhida == str("REFEITORIO"):
            dica = str("Local do campus onde comemos")
            fala = str("A melhor hora do dia=]")
        if palavra_escolhida == str("DIAREN") or palavra_escolhida == str("DIACON") or palavra_escolhida == str("DIACIN"):
            dica = str("Uma diretoria do integrado")
            fala = str("Não sabe? chuta")
        if palavra_escolhida == str("DIATINF"):
            dica = str("Uma diretoria do integrado")
            fala = str("Melhor diretoria <3")
        if palavra_escolhida == str("MINORA"):
            dica = str("Melhor professor da DIATINF")
            fala = str("Progamadora =p")
        if palavra_escolhida == str("DANI"):
            dica = str("Melhor professora da DIATINF")
            fala = str("A maior:)")
        if palavra_escolhida == str("GINASIO"):
            dica = str("Acontece varias apresentações e jogos")
            fala = str("No centro do CNAT;)")
        if palavra_escolhida==str('TAPETE VERMELHO'):
            dica = str("Perto da entrada")
            fala = str("É vermelho??")
        if palavra_escolhida==str('AUDITORIO'):
            dica = str("Usado pra reuniões e palestras")
            fala = str("É lindo e espaçoso")
        if palavra_escolhida==str('PISCINAS'):
            dica = str("Há competições de natação")
            fala = str("Espaço perfeito do CNAT")
        if palavra_escolhida==str('ROSQUINHAS'):
            dica = str("Local conhecido pelo seu apelido")
            fala = str("Usado para fofocar!")
        if palavra_escolhida==str('CNAT'):
            dica = str("Sigla do campus")
            fala = str("Facinho =)")
        
        

    fundo.blit(imagem, (0, 0))

    contador += 1
    if contador == 60:
        contador = 0
        segundos -= 1
    minutos_tela = str(segundos // 60)
    if (segundos % 60) < 10:
        segundos_tela = ':' + '0' + str(segundos % 60)
    else:
        segundos_tela = ':' + str(segundos % 60)

    tempo_tela = minutos_tela + segundos_tela
    temporizador = fonte_t.render(tempo_tela, 1, preto)
    fundo.blit(temporizador, (465, 10))

    if tempo_tela == '0:00':
      break
    count = 0
    limite = len(palavra_camuflada)
    for n in range(len(palavra_camuflada)):
        if palavra_camuflada[n] != '*':
            count += 1
    if count == limite:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                acertos+=0.5
            

    escreve(f"Tentativas:{chance}/6", fundo, branco, largura)
    acerto(f"Palavras corretas:{int(acertos)}/10", fundo, branco, largura)
    sobre(f"Dica: {dica}", fundo, branco, largura)
    elida(f"{fala}", fundo, preto, largura)
    palavra_escolhida, sair = sorteando_palavra(palavrasnivel1,
                                                palavra_escolhida, sair, dica)
    palavra_camuflada = camuflando_palavra(palavra_escolhida,
                                           palavra_camuflada,
                                           tentativas_de_letras)
    tentativas_de_letras, chance = tentando_uma_letra(tentativas_de_letras,
                                                      palavra_escolhida, letra,
                                                      chance)
    desenho_da_forca(fundo, chance)
    palavra_do_jogo(fundo, palavra_camuflada)
    botao_de_novamente(fundo, tempo_restante)
    sair, chance, tentativas_de_letras, letra = botao_do_final(
        palavra_camuflada, sair, chance, letra, tentativas_de_letras)
    sair, chance, tentativas_de_letras, letra = proximo_nivel(
        palavra_camuflada, sair, fundo, chance, letra, tentativas_de_letras,acertos)
    final(acertos)

    pygame.display.update()

fundo.blit(imagemgameover,(0,0))
time.sleep(5)
pygame.mixer.music.set_volume(0.90)
pygame.display.update()