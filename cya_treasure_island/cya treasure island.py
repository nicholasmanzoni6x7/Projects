print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


first=input("You come to the fork in the jungle. Will you go left or right?")
nu_first=first.lower()
if nu_first != "right":
	print("Game Over.")
else: 
	print("You come to a river.")
	second=input("Will you swim or wait for a boat?")
	nu_second=second.lower()
	if nu_second != "wait":
		print("You're a strong swimmer, but not stronger than the things in the water. Game Over.")
	else:
		print("A boat arrives. You board it and sail to the island. After walking for a minute you come to a dilapidated mansion. This is where Old Grumbly said the treasure would be! There are three doors...")
		third = input("Which color door do you enter? Red, yellow, or blue?")
		nu_third=third.lower()

		if nu_third == "red":
			print("You open the red door and walk inside. You are quickly surrounded by zombie pirates and eaten. Game Over.")
		elif nu_third == "yellow":
			print("There's more treasure here than you can possibly carry. You win!")
		elif nu_third == "blue":
			print("You open the blue door and walk inside. You hear a whispering coming from deeper in the mansion. You creep towards it. The door behind you slams shut on the last sunlight you will ever see. The whispering turns into wicked laughter. Game Over.")
		else:
			print("You feel a pinch on your leg and are suddenly very tired. Looking down, you see a blue and gold spider staring back at you. Your weakened legs give out and you fall to the ground. There are dozens of these spiders crawling toward you now. Game over.")