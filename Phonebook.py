
q = "y"


while q == 'y' or q == "":
    name = (input("What is the name?\n "))
    number = input("What is phone number?\n ")
    email = (input("What is the email?\n "))
    with open("contacts.txt", "a") as file:
        file.write(f"Name: {name}, number: {number}, email: {email}\n")
    while True:
        q = input("Add another? Y|n").lower()
        if q == "y" or q == "" or q == "n":
            break
        else:
            print("Please use a 'y' or a 'n' ")


