import pygame
import time

def play_custom_sound(volume=1.0):
    # Use a raw string literal for paths
    sound_file = '999-social-credit-siren.wav'

    try:
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)

        # Set the volume (value between 0.0 and 1.0)
        pygame.mixer.music.set_volume(volume)

        pygame.mixer.music.play()
        time.sleep(5)  # Adjust the sleep time if needed
    except Exception as e:
        print(f"Error playing sound: {e}")

if __name__ == '__main__':
    # Adjust the volume level as needed (e.g., 0.5 for half volume)
    play_custom_sound(volume=100)
