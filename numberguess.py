import random
def play_game(max_number,max_attempts):
    number = random.randint(1,max_number)
    count = 0
    print(f"Max_Attempts: {max_attempts}")
    while count < max_attempts:
         try:
             guess = int(input(f"Guess the number in the range of 1 to {max_number} : "))
             if not 1 <= guess <= max_number:
                print(f"Guess between (1-{max_number})")
                continue
         except ValueError:
             print("Enter a Valid Number: ")
             continue
         count += 1
         if guess == number:
            print("Congratulations! You guessed the number.")
            print(f" Number of Attempts: {count}")
            print("Thanks for Playing!")
            play_again()
            break
         elif count == max_attempts:
             print(f"Game Over... , Maximum Number of Attempts is {max_attempts}")
             print(f"The number was: {number}")
             play_again()
             break        
         elif guess < number:
            print("Too Low!")
         else:
            print("Too High!")

def choose_level():
    level = input("Enter level (Easy/Medium/Hard):")
    level = level.lower()
    if level == "easy":
        print("Easy Level")
        play_game(100,7)
    elif level == "medium":
        print("Medium Level")
        play_game(500,10)
    elif level == "hard":
        print("Hard Level")
        play_game(1000,12)
    else:
        print("Invalid Level")

def play_again():
       option = input(" Do you want to Replay?exit(yes/no):").lower()
       if option == "yes":
            choose_level()
       else:                  
            print("Exit the Game")

choice = input("Enter (Start/Exit):").lower()
if choice == "start":
    print("Play the Game")
    choose_level()
elif choice == "exit":
    print("Exit the game")
else:
    print("Invalid Choice")