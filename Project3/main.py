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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
choice1 = input('You\'r at a crossroad. where do you want to go? Type "left",or "right" \n')
if choice1 == "left" or choice1 == "LEFT":
    choice2 = input('Yo\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for the boat.type "swim" to swim across\n')
    if choice2 == "wait" or choice2 == "WAIT":
       choice3 = input('You arrived at the island unharmd.There is a house with 3 doors, one "red",one "yellow" and one "blue".which one do you choose\n')
       if choice3 == "red" or choice3 == "RED":
           print("It is a room full of fire. Game Over")
       elif choice3 == "yellow" or choice3 == "YELLOW":
           print("You found the treasue! You win")
       elif choice3 == "blue" or choice3 == "BLUE":
           print("You enter the room with beasts. Game Over")
       else:
           print("You choosed the door that does not exist.Game Over!")
    else:
        print("you have been attacked by an angry shark,Game Over!")
else:
    print("you fell into the hole, Game Over!")

