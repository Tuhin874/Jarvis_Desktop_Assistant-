import pygame
import os
import time
import eel

#Playing assistant sound function
@eel.expose
def playAssistantSound():
    pygame.mixer.init()

    music_dir = r"frontend/assets/audio/startSound.mp3"  # Raw string to avoid issues with backslashes

    if not os.path.isfile(music_dir):
        print(f"File not found: {music_dir}")
        return

    try:
        # Load the sound
        sound = pygame.mixer.Sound(music_dir)
        # Play the sound
        sound.play()
        # Wait for the sound to finish playing
        time.sleep(sound.get_length())
    except Exception as e:
        print(f"Error playing sound: {e}")