# GUI and main entry point for the CHIP-8 Emulator

# Turn off the pygame support message by setting the enviroment variable to any value
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

# Module's imports
import pygame
import sys
import time

import computer
import screen
import keyboard
import debug
import profiles

# Exit CHIP-8 and PyGame 
def exit(chip8, profile):
    if profile["debugging"] == "True":
        debug.dump(chip8)
    pygame.quit()
    sys.exit()

# Create the main window
def main(file, profile):
    
    # PyGame and CHIP-8 initialisation
    pygame.init()
    pygame.display.set_caption("CHIP-8 Emulator")
    canvas = pygame.display.set_mode( (64*profile["zoom"], 32*profile["zoom"]) )
    canvas.fill(profile["background_color"])
    pygame.display.update()

    chip8 = computer.CHIP8()
    chip8.file_open(file)

    # cycles is used to store how many CPU cycles has been counted
    cycles = 0
   
    # Main loop
    while chip8.register_PC < len(chip8.system_memory):

        # Execute an instruction 
        chip8.cpu_cycle()
    
        # Check for keyboard input
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                keyboard.key_pressed(chip8, event)
            elif event.type == pygame.QUIT:
                exit(chip8, profile)

        # Update the screen
        if chip8.video_draw_flag == 1:
            screen.frame_draw(chip8,canvas,profile)
            pygame.display.update()
            
        # Increase the loop cycles counter
        cycles += 1

        # A speed delay of 10/1000 seconds happens every time a certain amount of loops
        # equal to profile["speed"] is reached
        if cycles == profile["speed"]:
            time.sleep(10/1000)
            cycles = 0

    # Exit CHIP-8 if system's memory last location is reached
    exit(chip8, profile)
    
# Entry point
if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], profiles.profile_get(sys.argv[2]))
    else:
        print("Usage: python main.py <ROM Name> <profile>")
        print("Executing with default values: python main.py INVADERS normal")

        main("INVADERS", profiles.profile_get("normal"))
