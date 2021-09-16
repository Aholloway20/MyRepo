from VIM_Num import is_num
name = []
food = []

q = 'y'

while q == 'y' or q == '':
    name.append(input("what is your name?: "))
    food.append(is_num("How much did your food cost?: "))
    while True:
        q = (input("add another? y|n ")).lower()
        if q == 'y' or q == '' or q == 'n':
            break

total = sum(food)
people = len(name)
avg = total/people
print(name)
print(food)
print(f"the average is {avg}")

length = len(food)
middle_index = length // 2

first_half = food[:middle_index]
second_half = food[middle_index:]

if food[0] > avg:
    print(name[0],"your food is higher than the average")
