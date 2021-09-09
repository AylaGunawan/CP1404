"""
CP1404 - Practical 06
Languages Client Code
"""

from programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(ruby)
print(python)
print(visual_basic)

languages = [ruby, python, visual_basic]
dynamic_language_names = [language.name for language in languages if language.is_dynamic()]

print("The dynamically typed languages are:")
# print([language.name for language in languages if language.is_dynamic()])
print("\n".join(dynamic_language_names))
