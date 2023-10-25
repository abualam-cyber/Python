### NUMBER GUESSING GAME ###
import random
from Logo import logo

print(logo)

def choose_difficulty():
    max_attempts = 0
    difficulty_level = input("Choose difficulty. Type 'e' for easy, 'h' for hard!\n")
    if difficulty_level == 'e':
        max_attempts = 10
    elif difficulty_level == 'h':
        max_attempts = 5
        
    return max_attempts



def compare_guess(max_attempts):
    computer_guess = random.randint(1, 100)
    user_attempts = 0
    print(f"You have {max_attempts} attempts to guess the number!")
    
    while user_attempts < max_attempts:
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))
            user_attempts += 1
            if user_guess < computer_guess:
                print("Guess too low!")
                print(f"You have {max_attempts - user_attempts} attempts remaining!")
            elif user_guess > computer_guess:
                print("Guess too high!")
                print(f"You have {max_attempts - user_attempts} attempts remaining!")
            elif user_guess == computer_guess:
                print(f"You WON! You guessed {user_guess}, and computer guessed {computer_guess}")
                break
        except ValueError:
            print("Invalid input. Please try again!")
            
    if (user_guess != computer_guess) and (user_attempts >= max_attempts):
        print(f"Sorry, max attempts reached. Computer guess was {computer_guess}")
 
def play_game():
    while True:
        playGame = input("Press 'p' to play, 'x' to exit!\n")
        if playGame.lower() == 'x':
            print("Thank you for playing!")
            break
        elif playGame.lower() == 'p':
            compare_guess(choose_difficulty())
            
play_game()
    
        
    