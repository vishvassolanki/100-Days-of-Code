from calendar import firstweekday

print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("You are at a beach want to wait for a boat and swim for the island")
first = input("Type wait or swim for action: ")

if first == "swim":
    print("Oops you eaten by Shark, Game Over!")
elif first == "wait":
    print("The boat arrived and you are at Treasure Island")
    second = input("Want to go left or right? Type L or R for left right: ")
    if second == "L":
        print("Oops you choose the wrong side, Game Over!")
    elif second == "R":
        print("You are at a three door place: Red, Green, Yellow")
        third = input("Select the door Red, Green, Yellow: ")
        if third == "Red":
            print("You choose wrong door, Game Over!")
        elif third == "Green":
            print("Wrong door, Game Over!")
        elif third == "Yellow":
            print("You won!, The Treasure is yours")
    else:
        print("Please type valid input")
else:
    print("Please type valid input")
