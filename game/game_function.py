import pygame
import sys


def check_events(ship):
    """

    Responde a eventos de pressionamento de teclas 
    """

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    ship.moving_left = False
                    

           
            

def update_screen(ai_settings, screen, ship):
    """

    Atualiza as imagens na tela e alterna para a nova tela (atualiza)
    """
    screen.fill(ai_settings.bg_color) # setta a cor no fundo da tela
    ship.blitme() # nave sendo atualiazada...
    pygame.display.flip() # display sendo atualizado...
