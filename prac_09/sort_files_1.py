"""
CP1404 - Practical 09
Sort Files 1
"""

import shutil
import os

CURRENT_DIRECTORY = "FilesToSort"


def main():
    """Program that sorts files by extension."""
    extensions = []

    os.chdir(CURRENT_DIRECTORY)

    for filename in os.listdir('.'):  # when messing with files, does SRP apply?
        if os.path.isdir(filename):
            continue
        extension_index = filename.find(".")
        extension = filename[extension_index + 1:]
        extensions.append(extension)
    extensions = set(extensions)

    for extension in extensions:
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass

    for filename in os.listdir('.'):
        for extension in extensions:
            if filename.endswith(extension):
                shutil.move(filename, extension)


main()
