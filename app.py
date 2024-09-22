import random

def play_round():
    options = ['rock', 'paper', 'scissors']
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    if user_choice not in options:
        print("Invalid input. Try again.")
        return None, None
    
    program_choice = random.choice(options)
    print(f"The program chose: {program_choice}")
    
    if user_choice == program_choice:
        print("Tie!")
        return 0, 0
    elif (user_choice == 'rock' and program_choice == 'scissors') or \
         (user_choice == 'scissors' and program_choice == 'paper') or \
         (user_choice == 'paper' and program_choice == 'rock'):
        print("You won!")
        return 1, 0
    else:
        print("You lost!")
        return 0, 1

def play():
    user_score = 0
    program_score = 0
    
    while True:
        user_result, program_result = play_round()
        
        if user_result is not None:
            user_score += user_result
            program_score += program_result
        
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break
    
    print(f"Final score - You: {user_score}, Program: {program_score}")

if __name__ == "__main__":
    play()