'''
Write a Python program to guess a number between 1 to 9
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is
correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
'''
import random

on = True
number = random.randint(1,9)

while on:
    user_guess = input("Enter your guess: ")

    if int(user_guess) == number:
        print ("You won!")
        on = False
    else:
        print ('Try again')
