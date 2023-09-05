import pygame
from pygame.locals import *
from sys import exit
import button
import random


pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
x = 1100
y = 960

pygame.font.get_fonts()

tela = pygame.display.set_mode((x, y))
pygame.display.set_caption('image')
image = pygame.image.load('img/fundo.jpg')

# Carregar imagem carta
cartaPedra_img = pygame.image.load('img/Pedra.png').convert_alpha()
cartaPapel_img = pygame.image.load('img/Papel.png').convert_alpha()
cartaTesoura_img = pygame.image.load('img/Tesoura.png').convert_alpha()
cartaLagarto_img = pygame.image.load('img/Lagarto.png').convert_alpha()
cartaSpock_img = pygame.image.load('img/Spock.png').convert_alpha()
cartaVirada_img = pygame.image.load('img/back.png').convert_alpha()
vencedor1_img = pygame.image.load('img/Jogador1.png').convert_alpha()
vencedor2_img = pygame.image.load('img/Jogador2.png').convert_alpha()
empate_img = pygame.image.load('img/empate.png').convert_alpha()
play_img = pygame.image.load('img/Play.png').convert_alpha()
restart_img = pygame.image.load('img/Restart.png').convert_alpha()
UmJogador_img = pygame.image.load('img/1jogador.png').convert_alpha()
DoisJogadores_img = pygame.image.load('img/2jogadores.png').convert_alpha()
Voltar_img = pygame.image.load('img/Voltar.png').convert_alpha()


# criar button
PedraButton = button.Button(80, 700, cartaPedra_img)
PapelButton = button.Button(280, 700, cartaPapel_img)
TesouraButton = button.Button(480, 700, cartaTesoura_img)
LagartoButton = button.Button(680, 700, cartaLagarto_img)
SpockButton = button.Button(880, 700, cartaSpock_img)
CartaVirada = button.Button(300, 300, cartaVirada_img)
CartaVirada2 = button.Button(680, 300, cartaVirada_img)
vencedor1 = button.Button(415, 50, vencedor1_img)
vencedor2 = button.Button(415, 50, vencedor2_img)
PedraButtonVencedorP1 = button.Button(300, 300, cartaPedra_img)
PedraButtonVencedorP2 = button.Button(650, 300, cartaPedra_img)
TesouraButtonVencedorP1 = button.Button(300, 300, cartaTesoura_img)
TesouraButtonVencedorP2 = button.Button(650, 300, cartaTesoura_img)
LagartoButtonVencedorP1 = button.Button(300, 300, cartaLagarto_img)
LagartoButtonVencedorP2 = button.Button(650, 300, cartaLagarto_img)
SpockButtonVencedorP1 = button.Button(300, 300, cartaSpock_img)
SpockButtonVencedorP2 = button.Button(650, 300, cartaSpock_img)
PapelButtonVencedorP1 = button.Button(300, 300, cartaPapel_img)
PapelButtonVencedorP2 = button.Button(650, 300, cartaPapel_img)
Empate = button.Button(412, 50, empate_img)
PlayButton = button.Button(455, 400, play_img)
Restart = button.Button(475, 560, restart_img)
UmJogador = button.Button(330, 400, UmJogador_img)
DoisJogadores = button.Button(600, 400, DoisJogadores_img)
Voltar = button.Button(10, 10, Voltar_img)
pontosJ1 = 0
pontosJ2 = 0


def placar():
    global pontosJ1
    global pontosJ2

    fonte = pygame.font.SysFont('javanesetext', 40, False, False)
    mensagem1 = f'{pontosJ1}'
    mensagem2 = f'{pontosJ2}'
    texto1 = fonte.render(mensagem1, False, (white))
    texto2 = fonte.render(mensagem2, False, (white))
    tela.blit(texto1, (200, 200))
    tela.blit(texto2, (870, 200))


def menu():
    tela.fill(white)
    tela.blit(image, (0, 0))
    PlayButton.draw(tela)
    Voltar.clicked = False
    UmJogador.clicked = False
    DoisJogadores.clicked = False
    PlayButton.clicked = False
    global pontosJ2
    global pontosJ1
    pontosJ1 = 0
    pontosJ2 = 0

    while True:

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:
                if PlayButton.Click():
                    menu2()
                    PlayButton.clicked = False

            if event.type == QUIT:
                pygame.quit()
                exit()

        pygame.display.update()


def menu2():
    tela.fill(white)
    tela.blit(image, (0, 0))
    UmJogador.draw(tela)
    DoisJogadores.draw(tela)
    Voltar.draw(tela)
    Voltar.clicked = False
    UmJogador.clicked = False
    DoisJogadores.clicked = False
    PlayButton.clicked = False
    global pontosJ2
    global pontosJ1
    pontosJ1 = 0
    pontosJ2 = 0

    while True:

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:
                if UmJogador.Click():
                    playBot()
                    UmJogador.clicked = False
                elif DoisJogadores.Click():
                    play()
                    Voltar.clicked = False
                    UmJogador.clicked = False
                    DoisJogadores.clicked = False
                    PlayButton.clicked = False
                elif Voltar.Click():
                    menu()
                    Voltar.clicked = False
                    Voltar.clicked = False
                    UmJogador.clicked = False
                    DoisJogadores.clicked = False
                    PlayButton.clicked = False

            if event.type == QUIT:
                pygame.quit()
                exit()

        pygame.display.update()


def play():
    tela.fill(black)
    tela.blit(image, (0, 0))
    PapelButton.draw(tela)
    TesouraButton.draw(tela)
    LagartoButton.draw(tela)
    SpockButton.draw(tela)
    PedraButton.draw(tela)
    Voltar.draw(tela)
    Voltar.clicked = False
    UmJogador.clicked = False
    DoisJogadores.clicked = False
    PlayButton.clicked = False

    NumeroJogadas = 0
    JogadaUm = ""
    JogadaDois = ""

    def vencedor():
        global pontosJ1
        global pontosJ2
        if (JogadaUm == 'Pedra'):
            if (JogadaDois == 'Tesoura'):
                vencedor1.draw(tela)
                PedraButtonVencedorP1.draw(tela)
                TesouraButtonVencedorP2.draw(tela)
                pontosJ1 = pontosJ1+1

            elif (JogadaDois == 'Papel'):
                vencedor2.draw(tela)
                PapelButtonVencedorP2.draw(tela)
                PedraButtonVencedorP1.draw(tela)
                pontosJ2 = pontosJ2+1
            elif (JogadaDois == 'Spock'):
                vencedor2.draw(tela)
                PedraButtonVencedorP1.draw(tela)
                SpockButtonVencedorP2.draw(tela)
                pontosJ2 = pontosJ2+1
            elif (JogadaDois == 'Lagarto'):
                vencedor1.draw(tela)
                PedraButtonVencedorP1.draw(tela)
                LagartoButtonVencedorP2.draw(tela)
                pontosJ1 = pontosJ1+1
            elif (JogadaDois == 'Pedra'):
                Empate.draw(tela)
                PedraButtonVencedorP1.draw(tela)
                PedraButtonVencedorP2.draw(tela)
        elif (JogadaUm == 'Papel'):
            if (JogadaDois == 'Pedra'):
                vencedor2.draw(tela)
                PapelButtonVencedorP1.draw(tela)
                PedraButtonVencedorP2.draw(tela)
                pontosJ2 = pontosJ2+1
            elif (JogadaDois == 'Tesoura'):
                vencedor2.draw(tela)
                TesouraButtonVencedorP2.draw(tela)
                PapelButtonVencedorP1.draw(tela)
                pontosJ2 = pontosJ2+1
            elif (JogadaDois == 'Lagarto'):
                vencedor2.draw(tela)
                LagartoButtonVencedorP2.draw(tela)
                PapelButtonVencedorP1.draw(tela)
                pontosJ2 = pontosJ2+1
            elif (JogadaDois == 'Spock'):
                vencedor1.draw(tela)
                SpockButtonVencedorP2.draw(tela)
                PapelButtonVencedorP1.draw(tela)
                pontosJ1 = pontosJ1+1
            elif (JogadaDois == 'Papel'):
                Empate.draw(tela)
                PapelButtonVencedorP2.draw(tela)
                PapelButtonVencedorP1.draw(tela)
        elif (JogadaUm == 'Tesoura'):
            if (JogadaDois == 'Tesoura'):
                Empate.draw(tela)
                TesouraButtonVencedorP1.draw(tela)
                TesouraButtonVencedorP2.draw(tela)
            elif (JogadaDois == 'Pedra'):
                vencedor2.draw(tela)
                TesouraButtonVencedorP1.draw(tela)
                PedraButtonVencedorP2.draw(tela)
                pontosJ2 = pontosJ2+1
            elif (JogadaDois == 'Papel'):
                vencedor1.draw(tela)
                TesouraButtonVencedorP1.draw(tela)
                PapelButtonVencedorP2.draw(tela)
                pontosJ1 = pontosJ1+1
            elif (JogadaDois == 'Lagarto'):
                vencedor1.draw(tela)
                TesouraButtonVencedorP1.draw(tela)
                LagartoButtonVencedorP2.draw(tela)
                pontosJ1 = pontosJ1+1
            elif (JogadaDois == 'Spock'):
                vencedor1.draw(tela)
                TesouraButtonVencedorP1.draw(tela)
                SpockButtonVencedorP2.draw(tela)
                pontosJ1 = pontosJ1+1
        elif (JogadaUm == 'Lagarto'):
            if (JogadaDois == 'Lagarto'):
                Empate.draw(tela)
                LagartoButtonVencedorP1.draw(tela)
                LagartoButtonVencedorP2.draw(tela)
            elif (JogadaDois == 'Tesoura'):
                vencedor2.draw(tela)
                LagartoButtonVencedorP1.draw(tela)
                TesouraButtonVencedorP2.draw(tela)
                pontosJ2 = pontosJ2+1
            elif (JogadaDois == 'Pedra'):
                vencedor2.draw(tela)
                LagartoButtonVencedorP1.draw(tela)
                PedraButtonVencedorP2.draw(tela)
                pontosJ2 = pontosJ2+1
            elif (JogadaDois == 'Spock'):
                vencedor1.draw(tela)
                LagartoButtonVencedorP1.draw(tela)
                SpockButtonVencedorP2.draw(tela)
                pontosJ1 = pontosJ1+1
            elif (JogadaDois == 'Papel'):
                vencedor1.draw(tela)
                LagartoButtonVencedorP1.draw(tela)
                PapelButtonVencedorP2.draw(tela)
                pontosJ1 = pontosJ1+1
        elif (JogadaUm == 'Spock'):
            if (JogadaDois == 'Spock'):
                Empate.draw(tela)
                SpockButtonVencedorP1.draw(tela)
                SpockButtonVencedorP2.draw(tela)
            elif (JogadaDois == 'Lagarto'):
                vencedor2.draw(tela)
                SpockButtonVencedorP1.draw(tela)
                LagartoButtonVencedorP2.draw(tela)
                pontosJ2 = pontosJ2+1
            elif (JogadaDois == 'Papel'):
                vencedor2.draw(tela)
                SpockButtonVencedorP1.draw(tela)
                PapelButtonVencedorP2.draw(tela)
                pontosJ2 = pontosJ2+1
            elif (JogadaDois == 'Pedra'):
                vencedor1.draw(tela)
                SpockButtonVencedorP1.draw(tela)
                PedraButtonVencedorP2.draw(tela)
                pontosJ1 = pontosJ1+1
            elif (JogadaDois == 'Tesoura'):
                vencedor1.draw(tela)
                SpockButtonVencedorP1.draw(tela)
                TesouraButtonVencedorP2.draw(tela)
                pontosJ1 = pontosJ1+1

        Restart.draw(tela)
        placar()

    while True:

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:
                if PedraButton.Click():
                    if NumeroJogadas < 1:
                        CartaVirada.draw(tela)
                        NumeroJogadas += 1
                        JogadaUm = 'Pedra'
                        PedraButton.clicked = False

                    else:
                        NumeroJogadas += 1
                        JogadaDois = "Pedra"
                        PedraButton.clicked = False
                        vencedor()

                elif PapelButton.Click():
                    if NumeroJogadas < 1:
                        CartaVirada.draw(tela)
                        NumeroJogadas += 1
                        JogadaUm = "Papel"
                        PapelButton.clicked = False

                    else:
                        NumeroJogadas += 1
                        JogadaDois = "Papel"
                        PapelButton.clicked = False
                        vencedor()

                elif TesouraButton.Click():
                    if NumeroJogadas < 1:
                        CartaVirada.draw(tela)
                        NumeroJogadas += 1
                        JogadaUm = "Tesoura"
                        TesouraButton.clicked = False
                    else:
                        NumeroJogadas += 1
                        JogadaDois = "Tesoura"
                        TesouraButton.clicked = False
                        vencedor()

                elif LagartoButton.Click():
                    if NumeroJogadas < 1:
                        CartaVirada.draw(tela)
                        NumeroJogadas += 1
                        JogadaUm = "Lagarto"
                        LagartoButton.clicked = False
                    else:
                        NumeroJogadas += 1
                        JogadaDois = "Lagarto"
                        LagartoButton.clicked = False
                        vencedor()

                elif SpockButton.Click():
                    if NumeroJogadas < 1:
                        CartaVirada.draw(tela)
                        NumeroJogadas += 1
                        JogadaUm = "Spock"
                        SpockButton.clicked = False
                    else:
                        NumeroJogadas += 1
                        JogadaDois = "Spock"
                        SpockButton.clicked = False
                        vencedor()
                elif Voltar.Click():
                    menu2()
                    Voltar.clicked = False
                    UmJogador.clicked = False
                    DoisJogadores.clicked = False
                    PlayButton.clicked = False

                elif Restart.Click():
                    play()
                    Restart.clicked = False
                    Voltar.clicked = False
                    UmJogador.clicked = False
                    DoisJogadores.clicked = False
                    PlayButton.clicked = False

            if event.type == QUIT:
                pygame.quit()
                exit()

        pygame.display.update()


def playBot():
    tela.fill(black)
    tela.blit(image, (0, 0))

    PapelButton.draw(tela)
    TesouraButton.draw(tela)
    LagartoButton.draw(tela)
    SpockButton.draw(tela)
    PedraButton.draw(tela)
    Voltar.draw(tela)

    Voltar.clicked = False
    UmJogador.clicked = False
    DoisJogadores.clicked = False
    PlayButton.clicked = False

    Lista = ['Papel', 'Pedra', 'Tesoura', 'Lagarto', 'Spock']
    Bot = random.choice(Lista)

    NumeroJogadas = 1
    JogadaUm = Bot
    JogadaDois = ""

    def vencedor():
        global pontosJ1
        global pontosJ2
        if (JogadaUm == 'Pedra'):
            if (JogadaDois == 'Tesoura'):
                vencedor1.draw(tela)
                PedraButtonVencedorP1.draw(tela)
                TesouraButtonVencedorP2.draw(tela)
                pontosJ1 = pontosJ1+1

            elif (JogadaDois == 'Papel'):
                vencedor2.draw(tela)
                PapelButtonVencedorP2.draw(tela)
                PedraButtonVencedorP1.draw(tela)
                pontosJ2 = pontosJ2+1
            elif (JogadaDois == 'Spock'):
                vencedor2.draw(tela)
                PedraButtonVencedorP1.draw(tela)
                SpockButtonVencedorP2.draw(tela)
                pontosJ2 = pontosJ2+1
            elif (JogadaDois == 'Lagarto'):
                vencedor1.draw(tela)
                PedraButtonVencedorP1.draw(tela)
                LagartoButtonVencedorP2.draw(tela)
                pontosJ1 = pontosJ1+1
            elif (JogadaDois == 'Pedra'):
                Empate.draw(tela)
                PedraButtonVencedorP1.draw(tela)
                PedraButtonVencedorP2.draw(tela)
        elif (JogadaUm == 'Papel'):
            if (JogadaDois == 'Pedra'):
                vencedor2.draw(tela)
                PapelButtonVencedorP1.draw(tela)
                PedraButtonVencedorP2.draw(tela)
                pontosJ2 = pontosJ2+1
            elif (JogadaDois == 'Tesoura'):
                vencedor2.draw(tela)
                TesouraButtonVencedorP2.draw(tela)
                PapelButtonVencedorP1.draw(tela)
                pontosJ2 = pontosJ2+1
            elif (JogadaDois == 'Lagarto'):
                vencedor2.draw(tela)
                LagartoButtonVencedorP2.draw(tela)
                PapelButtonVencedorP1.draw(tela)
                pontosJ2 = pontosJ2+1
            elif (JogadaDois == 'Spock'):
                vencedor1.draw(tela)
                SpockButtonVencedorP2.draw(tela)
                PapelButtonVencedorP1.draw(tela)
                pontosJ1 = pontosJ1+1
            elif (JogadaDois == 'Papel'):
                Empate.draw(tela)
                PapelButtonVencedorP2.draw(tela)
                PapelButtonVencedorP1.draw(tela)
        elif (JogadaUm == 'Tesoura'):
            if (JogadaDois == 'Tesoura'):
                Empate.draw(tela)
                TesouraButtonVencedorP1.draw(tela)
                TesouraButtonVencedorP2.draw(tela)
            elif (JogadaDois == 'Pedra'):
                vencedor2.draw(tela)
                TesouraButtonVencedorP1.draw(tela)
                PedraButtonVencedorP2.draw(tela)
                pontosJ2 = pontosJ2+1
            elif (JogadaDois == 'Papel'):
                vencedor1.draw(tela)
                TesouraButtonVencedorP1.draw(tela)
                PapelButtonVencedorP2.draw(tela)
                pontosJ1 = pontosJ1+1
            elif (JogadaDois == 'Lagarto'):
                vencedor1.draw(tela)
                TesouraButtonVencedorP1.draw(tela)
                LagartoButtonVencedorP2.draw(tela)
                pontosJ1 = pontosJ1+1
            elif (JogadaDois == 'Spock'):
                vencedor1.draw(tela)
                TesouraButtonVencedorP1.draw(tela)
                SpockButtonVencedorP2.draw(tela)
                pontosJ1 = pontosJ1+1
        elif (JogadaUm == 'Lagarto'):
            if (JogadaDois == 'Lagarto'):
                Empate.draw(tela)
                LagartoButtonVencedorP1.draw(tela)
                LagartoButtonVencedorP2.draw(tela)
            elif (JogadaDois == 'Tesoura'):
                vencedor2.draw(tela)
                LagartoButtonVencedorP1.draw(tela)
                TesouraButtonVencedorP2.draw(tela)
                pontosJ2 = pontosJ2+1
            elif (JogadaDois == 'Pedra'):
                vencedor2.draw(tela)
                LagartoButtonVencedorP1.draw(tela)
                PedraButtonVencedorP2.draw(tela)
                pontosJ2 = pontosJ2+1
            elif (JogadaDois == 'Spock'):
                vencedor1.draw(tela)
                LagartoButtonVencedorP1.draw(tela)
                SpockButtonVencedorP2.draw(tela)
                pontosJ1 = pontosJ1+1
            elif (JogadaDois == 'Papel'):
                vencedor1.draw(tela)
                LagartoButtonVencedorP1.draw(tela)
                PapelButtonVencedorP2.draw(tela)
                pontosJ1 = pontosJ1+1
        elif (JogadaUm == 'Spock'):
            if (JogadaDois == 'Spock'):
                Empate.draw(tela)
                SpockButtonVencedorP1.draw(tela)
                SpockButtonVencedorP2.draw(tela)
            elif (JogadaDois == 'Lagarto'):
                vencedor2.draw(tela)
                SpockButtonVencedorP1.draw(tela)
                LagartoButtonVencedorP2.draw(tela)
                pontosJ2 = pontosJ2+1
            elif (JogadaDois == 'Papel'):
                vencedor2.draw(tela)
                SpockButtonVencedorP1.draw(tela)
                PapelButtonVencedorP2.draw(tela)
                pontosJ2 = pontosJ2+1
            elif (JogadaDois == 'Pedra'):
                vencedor1.draw(tela)
                SpockButtonVencedorP1.draw(tela)
                PedraButtonVencedorP2.draw(tela)
                pontosJ1 = pontosJ1+1
            elif (JogadaDois == 'Tesoura'):
                vencedor1.draw(tela)
                SpockButtonVencedorP1.draw(tela)
                TesouraButtonVencedorP2.draw(tela)
                pontosJ1 = pontosJ1+1

        Restart.draw(tela)
        placar()

    while True:

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:
                if PedraButton.Click():
                    if NumeroJogadas < 1:
                        CartaVirada.draw(tela)
                        NumeroJogadas += 1
                        JogadaUm = 'Pedra'
                        PedraButton.clicked = False

                    else:
                        NumeroJogadas += 1
                        JogadaDois = "Pedra"
                        PedraButton.clicked = False
                        vencedor()

                elif PapelButton.Click():
                    if NumeroJogadas < 1:
                        CartaVirada.draw(tela)
                        NumeroJogadas += 1
                        JogadaUm = "Papel"
                        PapelButton.clicked = False

                    else:
                        NumeroJogadas += 1
                        JogadaDois = "Papel"
                        PapelButton.clicked = False
                        vencedor()

                elif TesouraButton.Click():
                    if NumeroJogadas < 1:
                        CartaVirada.draw(tela)
                        NumeroJogadas += 1
                        JogadaUm = "Tesoura"
                        TesouraButton.clicked = False
                    else:
                        NumeroJogadas += 1
                        JogadaDois = "Tesoura"
                        TesouraButton.clicked = False
                        vencedor()

                elif LagartoButton.Click():
                    if NumeroJogadas < 1:
                        CartaVirada.draw(tela)
                        NumeroJogadas += 1
                        JogadaUm = "Lagarto"
                        LagartoButton.clicked = False
                    else:
                        NumeroJogadas += 1
                        JogadaDois = "Lagarto"
                        LagartoButton.clicked = False
                        vencedor()

                elif SpockButton.Click():
                    if NumeroJogadas < 1:
                        CartaVirada.draw(tela)
                        NumeroJogadas += 1
                        JogadaUm = "Spock"
                        SpockButton.clicked = False
                    else:
                        NumeroJogadas += 1
                        JogadaDois = "Spock"
                        SpockButton.clicked = False
                        vencedor()

                elif Voltar.Click():
                    menu()
                    Voltar.clicked = False
                    UmJogador.clicked = False
                    DoisJogadores.clicked = False

                elif Restart.Click():
                    playBot()
                    Restart.clicked = False

            if event.type == QUIT:
                pygame.quit()
                exit()

        pygame.display.update()


menu()
