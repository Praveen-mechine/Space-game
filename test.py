import pygame


    
for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit
        if event.type == pygame.KEYDOWN:
            check_keydown_events(events,ai_settings,bullets,ship)
        if event.key == pygame.K_RIGHT:
            #ship.moving_right = True
            #ship.rect.centerx +=1
            print("lgjg")
        elif event.key == pygame.K_LEFT:
                print("reu")
                #ship.moving_left = True
                
            

