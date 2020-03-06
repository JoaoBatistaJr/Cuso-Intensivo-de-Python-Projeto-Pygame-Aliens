import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
# Classe principal que gerencia todo o comportamento do jogo.

def __init__(self):
  """Inicializa e cria os recursos do jogo."""
  pygame.init()
  self.settings = Settings()
  
  self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
  self.settings.screen_width = self.screen.get_rect().width
  self.settings.screen_height = self.screen.get_rect().height
  pygame.display.set_caption("Alien Invasion")
  
  self.ship = Ship(self)
  self.bullets = pygame.sprite.Grup()
  self.aliens = pygame.sprite.Grup()
  
  self._crate_fleet()
  
def run_game(self):
    """ Inicia o loop principal do jogo."""
    while True:
        self._check_events()
        self.ship.update()
        self._update_bullets()
        self._update_screen()
        
def _check_events(self):
    """ Responde ao precionar o teclado ou o mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            self._check_keydown_events(event)
        elif event.type == pygame.KEYUP:
            self._check_keydown_events(event)
            
def _check_events(self, event):
    """Responde ao precionamento das teclas"""
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        self._fire_bullet()
        
def _check_keyup_events(self, event):
    """Responde ao soltar as teclas"""
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = False
        
def _fire_bullet(self):
    """Atualiza a posição dos projéteis e retira os projéteis antigos"""
    #Atualiza a posições.
    self.bullets.update()
    
    #Apaga as balas que desaparecem.
    for bullet in self.bullets.copy():
        if bullet.rect.bottom <= 0:
            self.bullets.remove(bullet)
            
def _crate_fleet(self):
    """Cria a frota de aliens."""
    #Cria um alien e encontra o numeros de aliens seguintes.
    #O espaço entre os aliens é a largura (width) de cada alien.
    alien = Alien(self)
    alien_width, alien_height = alien.rect.size
    available_space_x = self.settings.screen_width - (2 * alien_width)
    number_alien_x = available_space_x // (2 * alien_width)
    
    #Determina o numero de linha de aliens que cabem na tela.
    ship_height = self.ship.rect.height
    available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = available_space_y //(2 * alien_height)
    
    #Cria uma frota completa de aliens.
    for row_number in range(number_rows):
        for alien_number in range (number_alien_x):
            self._create_alien(alien_number, row_number)
            
def _create_alien(self, alien_number, row_number):
    """Cria um alien e o coloca na linha"""
    alien = Alien(self)
    alien_width, alien_height = alien.rect.size
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    self.aliens.add(alien)
    
def _update_screen(self):
    """Atualiza as imagens da tela e muda para a proxima tela."""
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()
    for bullet in self.bullets.sprites():
        bullet.draw_bullet()
    self.aliens.draw(self.screen)

    pygame.display.flip()
    
if __name__ == '__main__':
    """Cria a instancia do jogo e inicia o jogo."""
    ai = AlienInvasion()
    ai.run_game()