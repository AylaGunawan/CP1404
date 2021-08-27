"""
CP1404 - Practical 05
Hex Colours
"""

COLOUR_TO_CODE = {"black": "#000000", "beige": "#f5f5dc", "chocolate": "#d2691e", "coral": "#ff7f50",
                  "darkkhaki": "#bdb76b", "darkorange": "#ff8c00", "darkorchid": "#9932cc", "darksalmon": "#e9967a",
                  "dimgray": "#696969", "gray": "#bebebe"}

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    if colour_name in COLOUR_TO_CODE:
        print(f"{colour_name} is {COLOUR_TO_CODE[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()
