from random import shuffle as shuf
import os

os.system("cls" is os.name == "nt" else "clear")

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

my_list = ["Apple", "Banana", "Cherry", "Date", "Fig", "Gundam"]

element = my_list.index("Gundam")
print(element)
shuf(my_list)
print(my_list)
element = my_list.index("Gundam")
print(element)


