# prompt: Rock-Paper-Scissors Game  - User Input: Prompt the user to choose rock, paper, or scissors.  Computer Selection: Generate a random choice (rock, paper, or scissors) for  the computer.  Game Logic: Determine the winner based on the user's choice and the  computer's choice.  Rock beats scissors, scissors beat paper, and paper beats rock. Display Result: Show the user's choice and the computer's choice.  Display the result, whether the user wins, loses, or it's a tie.  Score Tracking (Optional): Keep track of the user's and computer's scores for  multiple rounds.  Play Again: Ask the user if they want to play another round.  User Interface: Design a user-friendly interface with clear instructions and  feedback.

import random

# Function to get the user's choice
def get_user_choice():
  while True:
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if choice in ["rock", "paper", "scissors"]:
      return choice
    else:
      print("Invalid choice. Please try again.")

# Function to get the computer's choice
def get_computer_choice():
  choices = ["rock", "paper", "scissors"]
  return random.choice(choices)

# Function to determine the winner
def get_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "tie"
  elif user_choice == "rock" and computer_choice == "scissors":
    return "user"
  elif user_choice == "paper" and computer_choice == "rock":
    return "user"
  elif user_choice == "scissors" and computer_choice == "paper":
    return "user"
  else:
    return "computer"

# Function to display the result
def display_result(user_choice, computer_choice, winner):
  print(f"Your choice: {user_choice}")
  print(f"Computer's choice: {computer_choice}")
  if winner == "user":
    print("You win!")
  elif winner == "computer":
    print("Computer wins!")
  else:
    print("It's a tie!")

# Function to ask the user if they want to play again
def ask_to_play_again():
  while True:
    choice = input("Do you want to play again (y/n)? ").lower()
    if choice in ["y", "n"]:
      return choice
    else:
      print("Invalid choice. Please try again.")

# Main function
def main():
  user_score = 0
  computer_score = 0

  while True:
    # Get the user's choice
    user_choice = get_user_choice()

    # Get the computer's choice
    computer_choice = get_computer_choice()

    # Determine the winner
    winner = get_winner(user_choice, computer_choice)

    # Display the result
    display_result(user_choice, computer_choice, winner)

    # Update the scores
    if winner == "user":
      user_score += 1
    elif winner == "computer":
      computer_score += 1

    # Ask the user if they want to play again
    choice = ask_to_play_again()

    # Break out of the loop if the user does not want to play again
    if choice == "n":
      break

  # Print the final score
  print(f"Your score: {user_score}")
  print(f"Computer's score: {computer_score}")

if __name__ == "__main__":
  main()