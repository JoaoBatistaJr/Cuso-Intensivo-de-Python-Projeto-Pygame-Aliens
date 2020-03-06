class Settings:
    """Classa que armazena todas as configurações do jogo"""

    def __init__(self):
        """Inicializa as configurações do jogo."""
        # Configuraçoes da tela.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Configurações da Nave.
        self.ship_speed = 1.5

        # Configuração dos projéteis.
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3