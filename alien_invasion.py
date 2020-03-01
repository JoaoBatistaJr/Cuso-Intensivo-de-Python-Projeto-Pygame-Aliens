import pygame

from settings import Settings
from ship import Ship
from game_functions as gf

# Inicializa o jogo, as configurações e o objeto screen
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)) 
    pygame.display.set_caption("Alien Invasion")
    
    # Cria uma espaçonave
    ship = Ship(screen)
    
    # Define a cor do fundo
    bg_color = (230,230,230)
    
    # Inicia o laço principal do jogo
    while True:
        gf.check_events()
        
        
        
run_game()