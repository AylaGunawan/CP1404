"""
CP1404 - Practical 09
Sort Files 2
"""

import shutil
import os

CURRENT_DIRECTORY = "FilesToSort"


def main():
    """"""
    extensions = {}
    categories = []

    os.chdir(CURRENT_DIRECTORY)

    for filename in os.listdir('.'):  # when messing with files, does SRP apply?
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        if extension not in extensions:
            category = input(f"What category would you like to sort {extension} files into? ")
            extensions[extension] = category
            categories.append(category)
            print(extensions)
            print(categories)


main()
