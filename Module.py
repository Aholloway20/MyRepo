def is_num():
    while True:
        try:
            num = int(input("Please give me a number: "))
            break
        except ValueError:
            print("This is not a number")
            continue
    return num


my_list = []


# var.append()10
my_list.append(is_num())
my_list.append(4)
my_list.append(5)
my_list.append(6)

length = len(my_list)
count = 0
while count < length:
    print(my_list[count])
    count += 1
for i in my_list:
    print(i)
