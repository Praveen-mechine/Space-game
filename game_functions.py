import sys

import pygame
from bullets import Bullet



def check_keydown_events(event,ai_settings,screen,ship,bullets):    
    if event.key == pygame.K_RIGHT:
        ship.moving_right=True
        
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings,ship,bullets):
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,ship,bullets)
        if event.key == pygame.K_RIGHT:
                ship.moving_right = True
                ship.rect.centerx +=1
        elif event.key == pygame.K_LEFT:
                
                ship.moving_left = True
                
            
def update_screen(ai_settings, screen, ship,bullets):
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
