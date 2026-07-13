import random
playing = True
number = str(random.randint(0, 50))
print("welcome to this  game plz guess the number")
while  playing:
    guess = input('enter your guess ')

    if guess==number:
        print("well done for guessing the number")
        print("the number was", number)

    else:
       print("plz try again")