"""
@author: Vlad
"""
import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        print(guess)
        if guess < random_number:
            print('Sorry, guess again. Too low')
        elif guess > random_number:
            print('Sorry, guess again. Too high')

    # print(f'Congrats, you guessed the number {random_number} !!')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high be cause low = high
        feedback = input(f'Is {guess} tii high (H), too low(L), or correct (C) ?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

        print(f'Congrats, computer guessed the number {guess} !!')


computer_guess(50)
