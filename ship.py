import pygame

class Ship():
    
    """Inicializa a espaçonave e define sua posição inicial"""
    def __init__(self, ai_settings, screen):  
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('imagens/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        super().__init__()
        
        # Flag de movimento
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Atualiza a posição da espaçonave de acordo com a flag de movimento."""
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
            
            # Atualiza o objeto rect de acordo com self.center
            self.rect.centerx = self.center
        
        """Desenha a espaçonave em sua posição atual"""
    def blitme(self):
        self.screen.blit(self.image, self.rect)