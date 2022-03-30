def game_main():
    ### IMPORTS ###
    import colorama
    from colorama import Fore
    from engine import engineScript
    from engine import clearScript

    from os import environ
    environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
    import pygame

    ### ENGINE INITIALIZATION ###
    settings = ["width", "height"]
    engineScript.InitEngine(Fore, settings)
    pygame.init()
    
    ### PROGRAM TERMINATED ###
    clearScript.run()

if __name__ == "__main__":
    game_main()