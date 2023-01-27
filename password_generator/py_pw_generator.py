import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

ez_pw = ""
for letter in range(0, nr_letters):
	l = len(letters) -1
	n = random.randint(0, l)
	ez_pw += letters[n]

for symbol in range(0, nr_symbols):
	l = len(symbols) -1
	n = random.randint(0, l)
	ez_pw += symbols[n]

for number in range(0, nr_numbers):
	l = len(numbers) - 1
	n = random.randint(0, l)
	ez_pw += numbers[n]

shuffled = list(ez_pw)
random.shuffle(shuffled)
print("".join(shuffled))