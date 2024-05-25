import pygame

class Ship:
    def __init__(self, screen):
        """

        Inicializa a espaçonave e define sua posição inicial
        """

        self.screen = screen
        self.image = pygame.image.load('img/spaceship.png')
        self.image_size = (70,70)
        self.image = pygame.transform.scale(self.image, self.image_size) # reduz o tamanho da img
        self.rect = self.image.get_rect() # trabalhando a img como retangulo
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx # x da tela
        self.rect.bottom = self.screen_rect.bottom # y da tela or centery
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """

        Para fazer o movimento continuo
        """
        if self.moving_right and self.rect.right < self.screen_rect.right: 
            self.rect.centerx +=1
        if self.moving_left and self.rect.left>0:
            self.rect.centerx -=1


    def blitme(self):
        """

        Desenha a espaçonave em sua posição inicial
        """
        self.screen.blit(self.image, self.rect)
