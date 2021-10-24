"""
CP1404 - Practical 09
Sort Files 1
"""

import shutil
import os

CURRENT_DIRECTORY = "FilesToSort"


def main():
    """Program that makes folders to sort files by extension."""
    extensions = []

    os.chdir(CURRENT_DIRECTORY)

    for filename in os.listdir('.'):  # when messing with files, does SRP apply?
        if os.path.isdir(filename):
            continue
        extension_index = filename.find(".")
        extension = filename[extension_index + 1:]  # extension = filename.split('.')[-1]
        extensions.append(extension)
    extensions = set(extensions)  # instructions say to use sets, but solutions don't?

    for extension in extensions:
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass

    for filename in os.listdir('.'):
        for extension in extensions:
            if filename.endswith(extension):
                shutil.move(filename, extension)  # os.rename(filename, "{}/{}".format(extension, filename))


main()
