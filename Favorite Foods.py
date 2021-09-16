my_list = []
while True:
    question = input("Would you like to add a food to your list??:\nY|n ").lower()
    if question == "y":
        my_list.append(input("What kinds of food do you like? : "))

        continue
    elif question == "n":
        break
    else:
        print("You did not select y or n")

for i in my_list:
    print(i + " is one of my favorite foods")
