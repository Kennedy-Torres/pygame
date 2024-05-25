import pygame
import sys
from settings import Settings
from ship import Ship
import game_function as gf # apelidando

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,
         ai_settings.screen_height))
    #screen.fill(ai_settings.bg_color)
    pygame.display.set_caption("Nome do jogo")
    bg_color = (230,230,230)
    
    ship = Ship(screen)

    #captura das acoes dentro do jogo
    while True: 
        gf.check_events(ship)
        #ship.blitme() # nave sendo atualiazada...
        #pygame.display.flip() # display sendo atualizado...
        ship.update()
        gf.update_screen(ai_settings, screen, ship)   
        

run_game()
