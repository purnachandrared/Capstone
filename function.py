from random import randint

Easy_level_turn = 10
Hard_level_turn = 5
turns = 0
def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too High")
        return turns -1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns -1
    else:
        print(f"you got it! The answer was {user_guess}.")

def set_difficulity():
    choose_difficulity = input("choose difficulty. Type 'Easy' or 'hard':")
    if choose_difficulity == "Easy":
        return Easy_level_turn
    else:
        return Hard_level_turn


def game():
    print("welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1,100)
    print(f"print the actual answer is {answer}")
    turns = set_difficulity()

    guess = 0
    while  guess!= answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        turns =check_answer(guess, answer, turns)
        if turns == 0:
            print("you've have run out of guesses. you lose")
            return
        elif guess != answer:
            print("Guess again")
game()