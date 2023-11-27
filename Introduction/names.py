import sys

names = [
    "Bill",
    "Charlie",
    "Fred",
    "George",
    "Ginny",
    "Percy",
    "Ron",
    "Elsa",
    "Anna",
    "Swen",
    "Olaf",
    "Agnar",
    "Cristof",
]

name = input("Name: ")

for n in names:
    if name == n:
        print("Found")
        sys.exit()

print("Not found")
sys.exit()
