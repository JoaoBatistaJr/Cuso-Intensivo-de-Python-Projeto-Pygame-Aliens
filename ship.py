import pygame
 
class Ship:
    """Classe que controla a espaçonave."""
 
    def __init__(self, ai_game):
        """Inicializa a espaçonave e a coloca na posição."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Carrega a imagem da espaçonave e posiciona em rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Iniciar a nava na parte inferior central da tela.
        self.rect.midbottom = self.screen_rect.midbottom

        # Armazena um valor descimal para a posição horizontal da espaçonave.
        self.x = float(self.rect.x)

        # Flags de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Atualiza a posição da nave com base nas flags de movimento"""
        # Atualiza o valor x da nave e nao o de rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Atualiza o rect do self.x
        self.rect.x = self.x

    def blitme(self):
        """Desenha a nave na posição atual"""
        self.screen.blit(self.image, self.rect)