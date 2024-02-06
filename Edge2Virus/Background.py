import pygame
import itertools

def create_blue_screen():
    # Initialize the pygame
    pygame.init()

    # Set resolution higher than the computer resolution so it is full screen and windows can overlap
    screen = pygame.display.set_mode((3840, 2160), pygame.RESIZABLE)

    # Initialize the mixer for audio
    pygame.mixer.init()

    # Load and play the song
    pygame.mixer.music.load('song.mp3')
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

    # Feel free to add more colors
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (255, 255, 255), (0, 0, 0)]
    color_iterator = itertools.cycle(colors)

    # current color
    current_color = next(color_iterator)

    screen.fill(current_color)

    # Update the display
    pygame.display.flip()

    start_ticks = pygame.time.get_ticks()

    running = True
    while running:
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        if seconds > 0.01:  # 0.01 seconds
            current_color = next(color_iterator)
            screen.fill(current_color)
            pygame.display.flip()
            start_ticks = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Stop the music and quit
    pygame.mixer.music.stop()
    pygame.quit()

create_blue_screen()
