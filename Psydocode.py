import time
count = 5
num1 = int(input("Input a number"))
while count <= num1:
    print(count)
    count = count + 5
    time.sleep(.5)
print("Goodbye my friend")