import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


choices = ["Rock", "Paper", "Scissors"]


# Start of the game
print("Welcome to the game!, chose 0 for Rock, 1 for Paper or 2 for Scissors")


# user choice
user_choice = int(input("Enter your choice: "))

# user choice print
if user_choice == 0:
    print(f"You choose: {rock}")
elif user_choice == 1:
    print(f"You choose: {paper}")
elif user_choice == 2:
    print(f"You choose: {scissors}")
else:
    print("Invalid choice! Please enter 0, 1, or 2.")


# Computer choice and print
computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print(f"Computer choose: {rock}")
elif computer_choice == 1:
    print(f"Computer choose: {paper}")
elif computer_choice == 2:
    print(f"Computer choose: {scissors}")
else:
    print("Invalid choice! Please enter 0, 1, or 2.")


# Final output
if user_choice == computer_choice:
    print("It's a draw!")
elif (
    (user_choice == 0 and computer_choice == 2)
    or (user_choice == 1 and computer_choice == 0)
    or (user_choice == 2 and computer_choice == 1)
):
    print("You win!")
else:
    print("You lose!")
# The game follows these steps:

# 1. Start of the game
# 2. User choice
# 3. User choice print
# 4. Compute choice and print
# 5. Print final output win or loose
