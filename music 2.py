#!/usr/bin/env python

import random
name = input ("Please fill your name before we start:")
print("Please fill your name before we start:", name)
start = input ("Lets Start Our Games By Click Enter Button")
print (start)

def main():
    """Start a song guessing game."""
    print("Guess the song (Lagu Negeri):")

    song = [
        "Kelantan",
        "Pulau Pinang",
        "Kedah",
        "Perak",
        "Terengganu",
        "Pahang",
        "Selangor",
        "Negeri Sembilan",
        "Melaka",
        "Johor",
        "Sabah",
        "Serawak",
        "Perlis",
        ]
    
    x = random.choice(song)
    guess = None

    while x != guess:

        guess = str(input("What song am I thinking of (Lagu Negeri?) "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))


main()