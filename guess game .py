import random

number = random.randint(1, 50)
guesses_left = 5

print('Guess the number between 1 and 50. You have 5 guesses.')

while guesses_left > 0:
    try:
        guess = int(input(f'You have {guesses_left} guesses left. Enter your guess: '))
    except ValueError:
        print('Please enter a valid number.')
        continue

    if guess>number:
        print('Your guess is too high.')
    elif guess<number:
        print('Your guess is too low.')

    if guess < 1 or guess > 50:
        print('Your guess must be between 1 and 50.')
        continue

    if guess == number:
        print('Correct! You guessed the number.')
        break
 

    guesses_left -= 1

if guesses_left == 0 and guess != number:
    print(f'Sorry, you ran out of guesses. The number was {number}.')
