uncle_sam = 1.08
Pay_the_server = 1.15
Food_stuff = float(input("How much was your meal?"))
Corprate_cut = uncle_sam * Food_stuff
pocket_book_pain = Corprate_cut * Pay_the_server
print("You need to leave " + str(pocket_book_pain) + " on the table to cover tax and tip.")
