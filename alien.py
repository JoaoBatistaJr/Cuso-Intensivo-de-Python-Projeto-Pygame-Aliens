import pygame
from pygame.sprite import Sprite
 
class Alien(Sprite):
    """Classe que repesenta um alienigena da frota"""

    def __init__(self, ai_game):
        """Inicializa o alien e define sua posição inicial."""
        super().__init__()
        self.screen = ai_game.screen

        # Carrega a imagem do alien e difine seu atributo rect  .
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Inicializa cada novo alien no canto superio esquerdo da tela.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição horizontal exata do alien
        self.x = float(self.rect.x)