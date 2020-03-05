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