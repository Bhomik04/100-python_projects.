import random

# Visual representation for the game
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

# List of choices for easy access
choices = [rock, paper, scissors]

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        return "You win!"
    else:
        return "You lose!"

# Main game logic
print("Let's play Rock, Paper, Scissors!")

result = ""
while result != "You lose!":
    user_input = int(input("What would you choose? Write 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))

    if user_input < 0 or user_input > 2:
        print("Invalid input. Please enter 0, 1, or 2.")
    else:
        print("You chose:")
        print(choices[user_input])

        random_values = random.randint(0, 2)
        print("Computer chose:")
        print(choices[random_values])

        result = determine_winner(user_input, random_values)
        print(result)

print("Game over, you lose.")