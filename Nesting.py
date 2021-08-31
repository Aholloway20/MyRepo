import time

count = 0
num = int(input("Give me any number: "))
if num < 0:
    print("your number is negative")
elif num > 0:
    while count < num:
        count = count + 1
        time.sleep(1)
        print(count)