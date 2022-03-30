def run():
    import os
    import sys
    import shutil

    # Get directory name
    mydir= "./engine/__pycache__"

    try:
        shutil.rmtree(mydir)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
