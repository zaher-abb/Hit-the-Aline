import pygame
from pygame.locals import *
from pygame.sprite import *
import random
pygame.init()

# Display configuration
pygame.display.set_caption('Hit the Aline')
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.mixer.init()
pygame.mixer.music.load('mvrasseli_play_the_game.ogg')
pygame.mixer.music.play(-1)
# define color
RED = (255, 0, 0)

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('p1_jump.png')
        self.rect = self.image.get_rect()
        self.rect.left=random.randint(0,620)
        self.rect.top=random.randint(0,460)

    def hit(self, XY):
        return self.rect.collidepoint(XY)

    def update(self):
        self.rect.left = random.randint(0, 600)
        self.rect.top = random.randint(0, 400)


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('meteorBrown_big2.png')
        self.rect = self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


alien = Alien()
meteor = Meteor()

All_Sprite = pygame.sprite.Group()
All_Sprite.add(alien)
All_Sprite.add(meteor)



# Entities
background = pygame.image.load('bHiPMju.png')
background=pygame.transform.scale(background,size)

second_bg = pygame.image.load('ET-The-Extra-Terre_1498982c.jpg')
second_bg=pygame.transform.scale(second_bg,size)

font_name=pygame.font.match_font('arial')
font = pygame.font.Font(font_name, 20)


Keepgoing=True

Hits_number = 0
clock = pygame.time.Clock()
pygame.time.set_timer(USEREVENT, 200)
#while schleife
while Keepgoing:

    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            Keepgoing  =False
            break

        elif event.type == MOUSEBUTTONDOWN:
            if alien.hit(pygame.mouse.get_pos()):
                Hits_number += 1
                screen.blit(second_bg,(0,0))
                break

        elif event.type == USEREVENT:
                alien.update()
                pygame.time.set_timer(USEREVENT, 1000)
                screen.blit(background,(0,0))
                All_Sprite.update()
                All_Sprite.draw(screen)
                score_value = font.render('Hits_number= '+str(Hits_number), True, RED)
                screen.blit(score_value,(300,10))
    pygame.display.flip()

pygame.quit()