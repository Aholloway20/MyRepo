from VIM_Num import is_num

shopping_cart = []


while True:
    shopping_cart.append(is_num("Enter the price of your item: $"))
    response = input("Add more items to your cart? Y|n: ")
    if response == "y" or response == "":
        continue
    elif response == "n":
        break
    else:
        print("Please enter a 'Y' for yes or a 'N' for no: ")


if len(shopping_cart) > 23:
    total = sum(shopping_cart)
if len(shopping_cart) > 11:
    total = sum(shopping_cart) * 0.85
if len(shopping_cart) < 24:
    total = sum(shopping_cart) * 0.75
tax = total * 1.08
print(f"The total is: ${tax:.{2}f}.")