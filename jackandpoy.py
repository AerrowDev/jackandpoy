import random

# ASCII art for each choice
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
---.__(___)`
'''

choices = [rock, paper, scissors]
choice_names = ["Rock", "Paper", "Scissors"]

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("What do you choose?")
    print("Type 0 for Rock, 1 for Paper, or 2 for Scissors.")

    try:
        user_choice = int(input("Your choice: "))
        if user_choice < 0 or user_choice > 2:
            print("Invalid number! You must enter 0, 1, or 2.")
            return
    except ValueError:
        print("Invalid input! Please enter a number (0, 1, or 2).")
        return

    computer_choice = random.randint(0, 2)

    print("\nYou chose:")
    print(choices[user_choice])
    print(f"({choice_names[user_choice]})")

    print("\nComputer chose:")
    print(choices[computer_choice])
    print(f"({choice_names[computer_choice]})")

    # Determine the winner
    if user_choice == computer_choice:
        print("\nIt's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("\nYou win!")
    else:
        print("\nYou lose!")

# Run the game
if __name__ == "__main__":
    play_game()
