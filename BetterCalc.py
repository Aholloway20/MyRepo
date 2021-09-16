class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a +self.b
    def dub(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b
a = int(input("Enter a number: "))
b = int(input("Enter the second number: "))
obj=cal(a,b)

while True:
    def menu():
        x = 1.('Add\n2 Sub \n3. multiply \n4. Divide')
        print(x)
        menu()
    choice=int(input("Please select one of the following: 1:Add 2.Subtract 3.Multiply 4.Divide "))
    if choice ==1:
        print("Result",obj.add())
    elif choice == 2:
        print("Result", obj.sub())
    elif choice == 3:
        print("Result", obj.multiply())
    elif choice == 4:
        print("Result", obj.divide())
    elif choice == 0:
        print("Try again with one of the choices")
        break
    else:
        print("Invalid input")
print()