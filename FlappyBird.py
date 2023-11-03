import pygame
from sys import exit

def bird_animation():
    global bird_index, bird_surf

    bird_index += 0.2
    if bird_index >= len(bird_frames): bird_index = 0
    bird_surf = bird_frames[int(bird_index)]

pygame.init()
game_active = False
clock = pygame.time.Clock()

# Screen and display
screen = pygame.display.set_mode((288, 512))
pygame.display.set_caption("Flappy Bird")
background_surf = pygame.image.load('Art/background-day.png').convert_alpha()

# Game font
flappy_font = pygame.font.Font('Font/flappy-font.ttf', 40)

# Score: PARA VALE
score_surf = flappy_font.render('Flappy Bird!', False, 'White').convert_alpha()
score_rect = score_surf.get_rect(center = (144, 20))

# Main screen message
main_message_surf = pygame.image.load('Art/main_message.png').convert_alpha()
main_message_rect = main_message_surf.get_rect(center = (144, 125))

# 'Press space' instruction
press_space_surf = flappy_font.render('Press space!', False, 'Black').convert_alpha()
press_space_rect = press_space_surf.get_rect(center = (144, 370))

# Ground
ground_surf = pygame.image.load('Art/base.png').convert_alpha()
ground_rect = ground_surf.get_rect(topleft = (0, 400))

# Bird
bird_frame_1 = pygame.image.load('Art/yellowbird-downflap.png').convert_alpha()
bird_frame_2 = pygame.image.load('Art/yellowbird-midflap.png').convert_alpha()
bird_frame_3 = pygame.image.load('Art/yellowbird-upflap.png').convert_alpha()
bird_frame_4 = pygame.image.load('Art/yellowbird-midflap.png').convert_alpha()
bird_frames = [bird_frame_1, bird_frame_2, bird_frame_3, bird_frame_4]
bird_index = 0
bird_surf = bird_frames[bird_index]
bird_rect = bird_surf.get_rect(center = (100, 270))

while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            screen.blit(score_surf, score_rect)
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()

    # Things to display whether the game is active or not
    if game_active:
        screen.blit(background_surf, (0, 0))
        screen.blit(score_surf, (0, 0))
        screen.blit(ground_surf, ground_rect)

        # Making the ground move to the left
        ground_rect.right -= 2
        if ground_rect.right <= 288: ground_rect.right = 336
    else:
        screen.blit(background_surf, (0, 0))
        screen.blit(main_message_surf, main_message_rect)
        screen.blit(press_space_surf, press_space_rect)
        screen.blit(ground_surf, ground_rect)
        bird_animation()
        screen.blit(bird_surf, bird_rect)

        # Making the ground move to the left
        ground_rect.right -= 2
        if ground_rect.right <= 288: ground_rect.right = 336

        # Making the bird slightly move up and down
        # To-do by Fabrizio

    pygame.display.update()
    clock.tick(60) # this game shouldn't run faster than 60 fps