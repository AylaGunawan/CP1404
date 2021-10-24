"""
CP1404 - Practical 09
Sort Files 1
"""

import shutil
import os

CURRENT_DIRECTORY = "FilesToSort"


def main():
    """Program that makes folders to sort files by extension (Version 1)."""
    extensions = []

    os.chdir(CURRENT_DIRECTORY)

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        if extension not in extensions:
            extensions.append(extension)
        # extensions = set(extensions)  instructions say to use sets, but solutions don't?

        for extension in extensions:  # os.rename(filename, "{}/{}".format(extension, filename))
            if filename.endswith(extension):
                print(f"Moved {filename}.{extension} to {extension} folder")
                shutil.move(filename, extension)


main()
