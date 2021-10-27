"""
CP1404 - Practical 09
Sort Files 2
"""

import os

CURRENT_DIRECTORY = "FilesToSort"


def main():
    """Program that makes folders to sort files by extension (Version 2)."""
    extension_to_category = {}
    # categories = []  instructions says to use lists, but solutions don't?

    os.chdir(CURRENT_DIRECTORY)

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        if extension not in extension_to_category:
            category = input(f"What category would you like to sort {extension} files into? ")
            extension_to_category[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

        print(f"Moved {filename}.{extension} to {extension_to_category[extension]}")
        os.rename(filename, "{}/{}".format(extension_to_category[extension], filename))


main()
