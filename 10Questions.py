import random

x = 0

while True:
    name = input("What is your name?")
    break
Questions = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
print(" CAUTION! ANSWERS ARE CASE SENSITIVE")
answers1 = ["Green", "Blue", "Yellow", "Purple"]
random.shuffle(answers1)
print(answers1)
Question_1 = input("QUESTION 1: What is the color of grass?: ")
if Question_1 == "Green" or "green":
    x = x+10

answers2 = ["Two", "Five", "Ten", "Twelve"]
random.shuffle(answers2)
print(answers2)
Question_2 = input("QUESTION 2: How many hands do people normally have? (type the numbers out please): ")
if Question_2 == "Two" or "two":
    x = x+10

answers3 = ["Earth", "Jupiter", "Mars", "Neptune"]
random.shuffle(answers3)
print(answers3)
Question_3 = input("QUESTION 3: What planet do we live on?: ")
if Question_3 == "Earth" or "earth":
    x = x+10

answers4 = ["Lord of the Rings", "Star Wars", "Star Trek", "Harry Potter"]
random.shuffle(answers4)
print(answers4)
Question_4 = input("QUESTION 4: What is the better movie series?: ")
if Question_4 == "Lord of the Rings":
    x = x+10
    print("Anything else is wrong")

answers5 = ["Cyber Security", "Interior Design", "Home Ec","Gym"]
random.shuffle(answers5)
print(answers5)
Question_5 = input("QUESTION 5: What course are we in: ")
if Question_5 == "Cyber Security" or "cyber security" or "Cyber security" or "cyber Security":
    x = x+10

answers6 = ["Twelve", "Ten", "Seven", "Twenty Four", "One Hundred"]
random.shuffle(answers6)
print(answers6)
Question_6 = input("QUESTION 6: How many months are in a year? (Type out the number): ")
if Question_6 == "Twelve":
    x = x+10

answers7 = ["Four", "Six", "Five", "Three"]
random.shuffle(answers7)
print(answers7)
Question_7 = input("QUESTION 7: How many days of class do we have a week? (Type out the number): ")
if Question_7 == "Four":
    x=x+10

answers8 = ["10", "12", "8", "25"]
random.shuffle(answers8)
print(answers8)
Question_8 = input("QUESTION 8: What is 5+5? (Input the actual number): ")
if Question_8 == "10":
    x=x+10

answers9 = ["2", "3", "4", "6"]
random.shuffle(answers9)
print("Number 9 Answers " + answers9)
Question_9 = input("QUESTION 9: What is 12/6? (Input the actual number): ")
if Question_9 == "2":
    x=x+10

answers10 = ["12", "10", "24", "16"]
random.shuffle(answers10)
print(answers10)
Question_10 = input("QUESTION 10: What is the square root of 144? (Input the actual number): ")
if Question_10 == "12":
    x=x+10
if x == 100:
    print("you got 100! A+++++++")
if x == 90:
    print("You got 90% A")
if x == 80:
    print("You got 80% B")
if x == 70:
    print("You got 70% C")
if x == 60:
    print("You got 60% D")
if x <= 59:
    print("You failed, Try again")