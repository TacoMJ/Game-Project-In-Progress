import pygame
import sys
from classes import *

def gameWindow():
    pygame.init()
    clock = pygame.time.Clock()
    background_x, background_y = 400, 300
    MOVEMENT_SPEED = 15 #Movement speed of the background or movement speed of player
    original_screen_width = 800
    original_screen_height = 600
    screen = pygame.display.set_mode((original_screen_width, original_screen_height), pygame.RESIZABLE)
    # ------------------------------Initializing characters-----------------------------------------
    userCharacter = characters_list()[0]
    current_frame = 0
    last_update = pygame.time.get_ticks()
    ANIMATION_SPEED = 100 #how fast to loop through the different images of walking
    #============================================================================================




    #-------------------------------Initiialize map-------------------------------------------------
    world_map = map()
    #-------------------------------Heads up display Health-----------------------------------------
    Health = heads_up_display()
    #-----------------------------------------------------------------------------------------------
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                width, height = event.w, event.h
                background_x -= (original_screen_width - width) // 2   #Makes it so that when the window is resized, the character is still in the center of the window
                background_y -= (original_screen_height - height) // 2 #But it is also in the same spot in the map as before
                original_screen_width = width
                original_screen_height = height
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            elif event.type == pygame.KEYUP: #Sets the texture to a resting texture right after playing the walking animations
                if event.key == pygame.K_w:
                    userCharacter.update_image(player_Walk_Up_Images()[0])
                    update_window(screen, world_map, background_x, background_y, userCharacter, original_screen_width, original_screen_height, Health)
                if event.key == pygame.K_s:
                    userCharacter.update_image(player_Walk_Down_Images()[0])
                    update_window(screen, world_map, background_x, background_y, userCharacter, original_screen_width, original_screen_height, Health)
                if event.key == pygame.K_a:
                    userCharacter.update_image(player_Walk_Left_Images()[0])
                    update_window(screen, world_map, background_x, background_y, userCharacter, original_screen_width, original_screen_height, Health)
                if event.key == pygame.K_d:
                    userCharacter.update_image(player_Walk_Right_Images()[0])
                    update_window(screen, world_map, background_x, background_y, userCharacter, original_screen_width, original_screen_height, Health)
        #--------How fast the animation plays--------------
        keys = pygame.key.get_pressed()
        now = pygame.time.get_ticks()
        #--------------------------------------------------
        #Move Up
        if keys[pygame.K_w]:
            for i in range(12):
                if now - last_update > ANIMATION_SPEED:  # Check if enough time has passed
                    current_frame = (current_frame + 1) % len(player_Walk_Up_Images())
                    userCharacter.update_image(player_Walk_Up_Images()[current_frame])
                    last_update = now
            background_y += MOVEMENT_SPEED
        #Move Down
        if keys[pygame.K_s]:
            for i in range(12):
                if now - last_update > ANIMATION_SPEED:  # Check if enough time has passed
                    current_frame = (current_frame + 1) % len(player_Walk_Down_Images())
                    userCharacter.update_image(player_Walk_Down_Images()[current_frame])
                    last_update = now
            background_y -= MOVEMENT_SPEED
        #Move Left
        if keys[pygame.K_a]:
            for i in range(12):
                if now - last_update > ANIMATION_SPEED:  # Check if enough time has passed
                    current_frame = (current_frame + 1) % len(player_Walk_Left_Images())
                    userCharacter.update_image(player_Walk_Left_Images()[current_frame])
                    last_update = now
            background_x += MOVEMENT_SPEED
        #Move Right
        if keys[pygame.K_d]:
            for i in range(12):
                if now - last_update > ANIMATION_SPEED:  # Check if enough time has passed
                    current_frame = (current_frame + 1) % len(player_Walk_Right_Images())
                    userCharacter.update_image(player_Walk_Right_Images()[current_frame])
                    last_update = now
            background_x -= MOVEMENT_SPEED
        if keys[pygame.K_l]:
            Health.lower_health(10, 20)

        clock.tick(80)
        update_window(screen, world_map, background_x, background_y, userCharacter, original_screen_width, original_screen_height, Health)
        """
        screen.fill((255, 255, 255))
        world_map.draw_map(screen, background_x - 300, background_y - 300)
        userCharacter.draw_main_character(screen, original_screen_width / 2, original_screen_height / 2)
        Health.draw(screen)
        pygame.display.flip() """

    pygame.quit()
    sys.exit()


gameWindow()
