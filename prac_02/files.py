"""
CP1404 - Practical 02
Files
"""

# 1

name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2

in_file = open("name.txt", "r")
content = in_file.read().strip()
print(f"Your name is {content}")
in_file.close()

# 3

in_file = open("numbers.txt", "r")
content = in_file.readlines()
print(int(content[0]) + int(content[1]))
in_file.close()

# number1 = int(in_file.readline())
# number2 = int(in_file.readline())

# 4

total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()

# number_of_lines = 0
# in_file = open("numbers.txt", "r")
# content = in_file.readlines()
# for line in content:
#     number_of_lines += 1
# print(number_of_lines)
