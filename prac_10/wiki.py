"""
CP1404 - Practical 10
Wiki
"""

import wikipedia


def main():
    """Prompt the user for a search phrase, then print the page summary."""
    search_phrase = input("Search Phrase: ")
    while search_phrase != "":
        try:
            page = wikipedia.page(search_phrase, auto_suggest=False)
            print(page.title)
            print("-" * len(page.title))  # prints an underline as long as the title
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.PageError:
            print(f"Could not find any pages matching '{search_phrase}'")
        except wikipedia.exceptions.DisambiguationError as disambiguation_pages:
            print("Found several pages matching '{search_phrase}'")
            for option in disambiguation_pages.options:
                print(option)
        print()
        search_phrase = input("Search Phrase: ")
    print("Finished")


main()
