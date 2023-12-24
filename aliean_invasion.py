import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
import bullets
def run_game(): 
    pygame.init()
    pygame.display.set_caption("space game")
    screen = pygame.display.set_mode((960,540))
    BG=pygame.transform.scale(pygame.image.load("Assets\R.jpeg"),(960,540))
    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    bullets = Group()
    
   
    
    pygame.display.update()
    
    
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
              run= False
        gf.check_events(ai_settings,ship,bullets)
        ship.update()
        bullets.update()
        
        
        gf.update_screen(ai_settings,screen,ship,bullets)
        for bullet in bullets.copy():
            if bullet.rect.bottom<=0:
                bullets.remove(bullet)
        print(len(bullets))
        
    
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullet.remove(bullet)
            print(len(bullet))
        gf.update_screen(ai_settings, screen, ship, bullets)
       
        screen.blit(BG,(1,1))                
        ship.blitme()

        pygame.display.flip()
    pygame.quit()
run_game()
