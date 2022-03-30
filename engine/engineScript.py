def InitEngine(Fore, settings):
    from configparser import ConfigParser
    config = ConfigParser()
    config.read('engine/config.ini')

    print(Fore.GREEN + "[SYSTEM] > [InitEngine] > INITIALIZING")    
    # Obtain resolution
    try: 
        # Obtain resolution from file
        try: 
            print(Fore.GREEN + "[SYSTEM] > [InitEngine] > " + Fore.WHITE + "Checking the settings file (config.ini)" + Fore.RESET)
            WIN_WIDTH = config.getint('engine', 'WIN_WIDTH')
            WIN_HEIGHT = config.getint('engine', 'WIN_HEIGHT')
            print(Fore.GREEN + "[SYSTEM] > [InitEngine] > " + Fore.WHITE + "Obtained " + Fore.CYAN + f"{WIN_WIDTH}x{WIN_HEIGHT}" + Fore.WHITE + " from file.")
        # Obtain resolution from system
        except:
            print(Fore.YELLOW + f"[!WARN!] > [InitEngine] > Failed to obtain settings. Trying to obtain monitor native resolution.")
            from win32api import GetSystemMetrics
            WIN_WIDTH = GetSystemMetrics(0)
            WIN_HEIGHT = GetSystemMetrics(1)
            print(Fore.GREEN + "[SYSTEM] > [InitEngine] > " + Fore.WHITE + "Set to fullscreen mode " + Fore.CYAN + f"{WIN_WIDTH}x{WIN_HEIGHT}" + Fore.WHITE + ".")

    # Set resolution to default mode
    except:
        print(Fore.RED + "[ERROR] > [InitEngine] > An error occurred. Failed to obtain monitor info. Setting to " + Fore.CYAN + "800x600" + Fore.RED + ".")
        WIN_WIDTH = 800
        WIN_HEIGHT = 600

    # Save the settings to file
    try:
        config.add_section("engine")
    except:
        pass
    config.set('engine', 'WIN_WIDTH', f"{WIN_WIDTH}")
    config.set('engine', 'WIN_HEIGHT', f"{WIN_HEIGHT}")
    with open('engine/config.ini', 'w') as configfile:
        config.write(configfile)
    settings[0] = WIN_WIDTH
    settings[1] = WIN_HEIGHT
    
    # Return to main function
    print(Fore.GREEN + "[SYSTEM] > [InitEngine] > COMPLETE!" + Fore.WHITE)