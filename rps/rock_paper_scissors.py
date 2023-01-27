import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


plays = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors"))

print(plays[player_choice])

com_choice = random.randint(0,2)

print("Computer chose:")
print(plays[com_choice])

if player_choice == 0:
	if com_choice == 0:
		print("Draw")
	elif com_choice == 1:
		print("You Lose!")
	else:
		print("You win!")
elif player_choice == 1:
	if com_choice == 0:
		print("You win!")
	elif com_choice == 1:
		print("Draw")
	else:
		print("You lose!")
else:
	if com_choice == 0:
		print("You lose!")
	elif com_choice == 1:
		print("You win!")
	else:
		print("Draw")